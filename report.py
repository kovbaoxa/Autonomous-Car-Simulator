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
from src.Tracks import Map0, Map1, Map2, Map3
from src.Database import Database
from src.Game import Game
from src.LiDAR import LiDAR


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

        ################################################################
        ### test 1
        ################################################################
        test_data = dict()
        ### test info
        test_data["map"]    = 1
        test_data["mode"]   = "simple"
        test_data["brain"]  = None
        test_data["infile"] = input_file
        ### test results
        test_data["complete"] = False # win condition status
        test_data["time"]     = None  # total time
        test_data["dist"]     = None  # total distance
        test_data["ckpt"]     = None  # checkpoints

        print("### Test 1 : Map {} - Mode {}".format(test_data["map"], test_data["mode"]))

        if test_data["infile"] is not None:
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
        
        result_struct[participant].append(test_data)
        time.sleep(2)
        ################################################################
        ### test 2
        ################################################################
        test_data = dict()
        ### test info
        test_data["map"]    = 1
        test_data["mode"]   = "advanced"
        test_data["brain"]  = brain_module_1
        test_data["infile"] = None
        ### test results
        test_data["complete"] = False # win condition status
        test_data["time"]     = None  # total time
        test_data["dist"]     = None  # total distance
        test_data["ckpt"]     = None  # checkpoints

        print("### Test 2 : Map {} - Mode {}".format(test_data["map"], test_data["mode"]))

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
        
        result_struct[participant].append(test_data)
        time.sleep(2)
        ################################################################
        ### test 3
        ################################################################
        test_data = dict()
        ### test info
        test_data["map"]    = 1
        test_data["mode"]   = "advanced"
        test_data["brain"]  = brain_module_2
        test_data["infile"] = None
        ### test results
        test_data["complete"] = False # win condition status
        test_data["time"]     = None  # total time
        test_data["dist"]     = None  # total distance
        test_data["ckpt"]     = None  # checkpoints

        print("### Test 3 : Map {} - Mode {}".format(test_data["map"], test_data["mode"]))

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
        
        result_struct[participant].append(test_data)
        time.sleep(2)
        ################################################################
        ### test 4
        ################################################################
        test_data = dict()
        ### test info
        test_data["map"]    = 2
        test_data["mode"]   = "advanced"
        test_data["brain"]  = brain_module_2
        test_data["infile"] = None
        ### test results
        test_data["complete"] = False # win condition status
        test_data["time"]     = None  # total time
        test_data["dist"]     = None  # total distance
        test_data["ckpt"]     = None  # checkpoints

        print("### Test 4 : Map {} - Mode {}".format(test_data["map"], test_data["mode"]))

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
        
        result_struct[participant].append(test_data)
        time.sleep(2)
        ################################################################
        ### test 5
        ################################################################
        test_data = dict()
        ### test info
        test_data["map"]    = 3
        test_data["mode"]   = "advanced"
        test_data["brain"]  = brain_module_2
        test_data["infile"] = None
        ### test results
        test_data["complete"] = False # win condition status
        test_data["time"]     = None  # total time
        test_data["dist"]     = None  # total distance
        test_data["ckpt"]     = None  # checkpoints

        print("### Test 5 : Map {} - Mode {}".format(test_data["map"], test_data["mode"]))

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
        
        result_struct[participant].append(test_data)
        time.sleep(2)


    result_file.write(json.dumps(result_struct, indent=4, cls = customEnc))
    result_file.close()

    return 0

def run_game(auto, map_idx, brain_module, infile = ''):
    if auto not in ("simple", "advanced"):
        print("Invalid auto mode")
        return (None, None, None, None)

    map_list = [Map0, Map1, Map2, Map3]
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
    dev_null = open('/dev/null', 'w')
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
