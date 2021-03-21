import argparse
import copy
import json
import importlib
import os
import threading
import time
import pygame

# from Brain import Brain
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

    for f in os.listdir(folder):
        participant = f
        result_struct[participant] = list()
        # brain_module = __import__('Brain', folder + '.' + participant + ".Brain")
        brain_module = importlib.import_module(folder + '.' + participant + ".Brain")

        print("################################################################")
        print("Evaluation of participant {}".format(participant))
        print("################################################################")

        ################################################################
        ### test 1
        ################################################################
        test_res = dict()
        res_win  = None # win condition status
        res_time = None # total time
        res_dist = None # total distance
        res_ckpt = None # checkpoints

        res_win, res_time, res_dist, res_ckpt = run_game("simple", 1, brain_module, os.path.join(folder, participant, "input.txt"))

        test_res["complete"] = res_win is True
        test_res["time"] = "{:.03f}".format(res_time / 1000.0)
        test_res["dist"] = "{:.1f}".format(res_dist)
        test_res["ckpt"] = list()
        for k, v in res_ckpt.items():
            test_res["ckpt"].append({
                "name" : k,
                "time" : "{:.03f}".format(v["time"] / 1000.0),
                "dist" : "{:.1f}".format(v["distance"]),
            })
        
        result_struct[participant].append(test_res)
        time.sleep(2)
        ################################################################
        ### test 2
        ################################################################
        test_res = dict()
        res_win  = None # win condition status
        res_time = None # total time
        res_dist = None # total distance
        res_ckpt = None # checkpoints

        res_win, res_time, res_dist, res_ckpt = run_game("advanced", 1, brain_module)

        test_res["complete"] = res_win is True
        test_res["time"] = "{:.03f}".format(res_time / 1000.0)
        test_res["dist"] = "{:.1f}".format(res_dist)
        test_res["ckpt"] = list()
        for k, v in res_ckpt.items():
            test_res["ckpt"].append({
                "name" : k,
                "time" : "{:.03f}".format(v["time"] / 1000.0),
                "dist" : "{:.1f}".format(v["distance"]),
            })
        
        result_struct[participant].append(test_res)
        time.sleep(2)
        ################################################################
        ### test 3
        ################################################################
        test_res = dict()
        res_win  = None # win condition status
        res_time = None # total time
        res_dist = None # total distance
        res_ckpt = None # checkpoints

        res_win, res_time, res_dist, res_ckpt = run_game("advanced", 2, brain_module)

        test_res["complete"] = res_win is True
        test_res["time"] = "{:.03f}".format(res_time / 1000.0)
        test_res["dist"] = "{:.1f}".format(res_dist)
        test_res["ckpt"] = list()
        for k, v in res_ckpt.items():
            test_res["ckpt"].append({
                "name" : k,
                "time" : "{:.03f}".format(v["time"] / 1000.0),
                "dist" : "{:.1f}".format(v["distance"]),
            })
        
        result_struct[participant].append(test_res)
        time.sleep(2)
        ################################################################
        ### test 4
        ################################################################
        test_res = dict()
        res_win  = None # win condition status
        res_time = None # total time
        res_dist = None # total distance
        res_ckpt = None # checkpoints

        res_win, res_time, res_dist, res_ckpt = run_game("advanced", 3, brain_module)

        test_res["complete"] = res_win is True
        test_res["time"] = "{:.03f}".format(res_time / 1000.0)
        test_res["dist"] = "{:.1f}".format(res_dist)
        test_res["ckpt"] = list()
        for k, v in res_ckpt.items():
            test_res["ckpt"].append({
                "name" : k,
                "time" : "{:.03f}".format(v["time"] / 1000.0),
                "dist" : "{:.1f}".format(v["distance"]),
            })
        
        result_struct[participant].append(test_res)
        time.sleep(2)

    result_file.write(json.dumps(result_struct, indent=4))
    result_file.close()

    return 0

def run_game(auto, map_idx, brain_module, infile = ''):
    map_list = [Map0, Map1, Map2, Map3]
    if map_idx not in range(len(map_list)):
        print("Invalid map index")
        return

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    walls, checkpoints, finish_line, car_origin, hud_pos = map_list[map_idx]

    car = copy.copy(car_origin)
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    game = Game(walls, checkpoints, finish_line, car, database, hud_pos=hud_pos, close_at_end=True)

    brain_thread = None
    if auto is not None:
        brain = brain_module.Brain(database) if auto == "advanced" else TimeEventBrain(database, infile)
        print("Loaded brain module: {}".format(brain))
        brain_thread = threading.Thread(target=brain.run, args=(g_sync_cv, g_brain_cv,))
        brain_thread.start()

    res = None

    if auto:
        res = game.runAuto(cv=g_sync_cv, bcv=g_brain_cv)
    else:
        res = game.runManual()

    if brain_thread is not None:
        brain_thread.join()

    return res


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
