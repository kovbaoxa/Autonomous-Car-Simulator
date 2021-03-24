import argparse
import copy
import json
import importlib
import os
import threading
import time
import pygame
import sys

from json import JSONEncoder
from src.TimeEventBrain import TimeEventBrain
from src.Control import Control
from src.Tracks import Map0, Map1, Map2, Map3, Map4, Map5
from src.Database import Database
from src.Game import Game
from src.LiDAR import LiDAR
from multiprocessing import Process


# game thread notifies brain as soon as the LiDAR data is ready
g_sync_cv = threading.Condition()

# brain thread notifies game when its computation is finished
# - if computation is too long, game thread is unlocked to guarantee the
#   minimum framerate
g_brain_cv = threading.Condition()

def main(folder):
    result_file = open("results.txt", 'w')
    result_struct = dict()

    for i, participant in enumerate(sorted(os.listdir(folder))):
        p = Process(target=process_results, args=(folder, result_struct, i, participant))
        p.start()

    result_file.write(json.dumps(result_struct, indent=4, cls = customEnc))
    result_file.close()

    return 0

def process_results(folder, result_struct, i, participant):
    result_struct[participant] = list()

    print("################################################################")
    print("### Evaluation of participant {} ({} of {})".format(participant, i + 1, len(os.listdir(folder))))
    print("################################################################")

    input_file     = None
    brain_module_1 = None
    brain_module_2 = None

    if os.path.exists(os.path.join(folder, participant, "input.txt")):
        input_file = os.path.join(folder, participant, "input.txt")
    else:
        print("### - Could not find input file")
    if os.path.exists(os.path.join(folder, participant, "Brain_1.py")):
        brain_module_1 = importlib.import_module(folder + '.' + participant + ".Brain_1")
    else:
        print("### - Could not find brain module 1")
    if os.path.exists(os.path.join(folder, participant, "Brain_2.py")):
        brain_module_2 = importlib.import_module(folder + '.' + participant + ".Brain_2")
    else:
        print("### - Could not find brain module 2")

    print("################################################################")

    result_struct[participant].append(test_case("t1", 1, "simple", None, input_file))
    time.sleep(2)
    result_struct[participant].append(test_case("t2", 1, "advanced", brain_module_1, None))
    time.sleep(2)
    result_struct[participant].append(test_case("t3", 1, "advanced", brain_module_2, None))
    time.sleep(2)
    result_struct[participant].append(test_case("t4", 2, "advanced", brain_module_2, None))
    time.sleep(2)
    result_struct[participant].append(test_case("t5", 3, "advanced", brain_module_2, None))
    time.sleep(2)
    result_struct[participant].append(test_case("t6", 4, "advanced", brain_module_2, None))
    time.sleep(2)
    result_struct[participant].append(test_case("t7", 5, "advanced", brain_module_2, None))
    time.sleep(2)
    return

def test_case(test_name, map_idx, mode, brain_module, infile):
    test_data = dict()
    ### test info
    test_data["map"]    = map_idx
    test_data["mode"]   = mode
    test_data["brain"]  = brain_module
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
    
    return test_data

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

class customEnc(JSONEncoder):
    def default(self, object):
        ret = ""
        try:
            ret = json.JSONEncoder.default(self, object)
        except:
            ret = object.__file__
        return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-f", "--folder",
            help="Set path to brain folders to execute",
            action="store",
            default="results"
        )
    args = parser.parse_args()
    main(args.folder)
