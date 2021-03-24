import argparse
import copy
import json
import importlib
import os
import threading
import time
import pygame
import sys
import multiprocessing

from json import JSONEncoder
from src.TimeEventBrain import TimeEventBrain
from src.Control import Control
from src.Tracks import Map0, Map1, Map2, Map3, Map4, Map5
from src.Database import Database
from src.Game import Game
from src.LiDAR import LiDAR

# game thread notifies brain as soon as the LiDAR data is ready
g_sync_cv = threading.Condition()

# brain thread notifies game when its computation is finished
# - if computation is too long, game thread is unlocked to guarantee the
#   minimum framerate
g_brain_cv = threading.Condition()

class customEnc(JSONEncoder):
    def default(self, object):
        ret = ""
        try:
            ret = json.JSONEncoder.default(self, object)
        except:
            ret = object.__file__
        return ret

def load_brain_module(submission_dir_path, participant, module_name):
    sys.path.insert(0, submission_dir_path)
    path = os.path.join(submission_dir_path, participant, module_name + ".py")

    if (os.path.exists(path)):
        return importlib.import_module(participant + "." + module_name)
    else:
        return None

def run_game(auto, map_idx, brain_module, infile = ''):
    if auto not in ("simple", "advanced"):
        print("Invalid auto mode")
        return (None, None, None, None)

    map_list = [Map0, Map1, Map2, Map3, Map4, Map5]
    if map_idx not in range(len(map_list)):
        print("Invalid map index")
        return (None, None, None, None)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    walls, checkpoints, finish_line, rocks, car_origin, hud_pos = map_list[map_idx]

    car = copy.copy(car_origin)
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    game = Game(walls, checkpoints, finish_line, rocks, car, database, hud_pos=hud_pos, close_at_end=True)

    if auto == "simple" and infile is None:
        print("No input file to run evaluation")
        return (None, None, None, None)

    if auto == "advanced" and brain_module is None:
        print("No brain module to run evaluation")
        return (None, None, None, None)

    stdout = sys.stdout
    dev_null = open('nul', 'w')
    sys.stdout = dev_null

    brain = brain_module.Brain(database) if auto == "advanced" else TimeEventBrain(database, infile)
    print("Loaded brain module: {}".format(brain))
    brain_thread = threading.Thread(target=brain.run, args=(g_sync_cv, g_brain_cv,))
    brain_thread.start()

    res = game.runAuto(cv=g_sync_cv, bcv=g_brain_cv)

    brain_thread.join()

    sys.stdout = stdout

    return res

def run_test(test_name, map_idx, mode, submission_dir_path, participant, module_name, infile, test_results_queue):
    test_data = dict()
    ### test info
    test_data["map"]    = map_idx
    test_data["mode"]   = mode
    test_data["brain"]  = load_brain_module(submission_dir_path, participant, module_name)
    test_data["infile"] = infile
    ### test results
    test_data["complete"] = False # win condition status
    test_data["time"]     = None  # total time
    test_data["dist"]     = None  # total distance
    test_data["ckpt"]     = None  # checkpoints

    print("### Test {}: Map {} - Mode {}".format(test_name, test_data["map"], test_data["mode"]))

    if test_data["brain"] is not None:
        res_win, res_time, res_dist, res_ckpt = run_game(test_data["mode"], test_data["map"], test_data["brain"], test_data["infile"])
        test_data["complete"] = res_win is True
        test_data["time"] = "{:.03f}".format(res_time / 1000.0)
        test_data["dist"] = "{:.1f}".format(res_dist)
        test_data["ckpt"] = list()
        for k, v in res_ckpt.items():
            test_data["ckpt"].append({
                "name" : k,
                "time" : "{:.03f}".format(v["time"] / 1000.0),
                "dist" : "{:.1f}".format(v["distance"]),
            })
        print("### - Done")
    else:
        print("### - Skipped")
    
    test_results_json = json.dumps(test_data, indent=4, cls=customEnc)
    test_results_queue.put(test_results_json)
    return test_data

def run_tests(submission_dir_path, participant):
    input_file_path = None
    if os.path.exists(os.path.join(submission_dir_path, participant, "input.txt")):
        input_file_path = os.path.join(submission_dir_path, participant, "input.txt")
    else:
        print("### - Could not find input file")

    print("################################################################")

    test_results_queue = multiprocessing.Queue(maxsize=7)

    test_jobs = [ 
        multiprocessing.Process(target=run_test, args=("t1", 1, "simple", "", "", "", input_file_path, test_results_queue)),
        multiprocessing.Process(target=run_test, args=("t2", 1, "advanced", submission_dir_path, participant, "Brain_1", None, test_results_queue)),
        multiprocessing.Process(target=run_test, args=("t3", 1, "advanced", submission_dir_path, participant, "Brain_2", None, test_results_queue)),
        multiprocessing.Process(target=run_test, args=("t4", 2, "advanced", submission_dir_path, participant, "Brain_2", None, test_results_queue)),
        multiprocessing.Process(target=run_test, args=("t5", 3, "advanced", submission_dir_path, participant, "Brain_2", None, test_results_queue)),
        multiprocessing.Process(target=run_test, args=("t6", 4, "advanced", submission_dir_path, participant, "Brain_2", None, test_results_queue)),
        multiprocessing.Process(target=run_test, args=("t7", 5, "advanced", submission_dir_path, participant, "Brain_2", None, test_results_queue))
    ]
    for test_job in test_jobs: test_job.start()
    for test_job in test_jobs: test_job.join()

    test_results = list()
    while not test_results_queue.empty():
        test_result_json = test_results_queue.get()
        test_result = json.loads(test_result_json)
        test_results.append(test_result)

    return test_results

def log(test_results, evaluation_file_path):
    evaluation = json.dumps(test_results, indent=4, cls=customEnc)
    evaluation_file = open(evaluation_file_path, 'w')
    evaluation_file.write(evaluation)
    evaluation_file.close()

def main(submission_dir_path, evaluation_dir_path):
    sys.path.insert(0, submission_dir_path)
    participants = enumerate(sorted(os.listdir(submission_dir_path)))

    for i, participant in participants:
        print("################################################################")
        print("### Evaluation of participant {} ({} of {})".format(participant, i + 1, len(os.listdir(submission_dir_path))))
        print("################################################################")
        evaluation_file_path = os.path.join(evaluation_dir_path, participant + ".txt")
        test_results = run_tests(submission_dir_path, participant)
        log(test_results, evaluation_file_path)
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--submissions",
        help="Set path to submissions directory.",
        action="store",
        default="submissions"
    )
    parser.add_argument(
        "-e", "--evaluations",
        help="Set path to evaluations directory.",
        action="store",
        default="evaluations"
    )
    args = parser.parse_args()
    main(args.submissions, args.evaluations)