import argparse
import os
import threading

import pygame

from Brain import Brain
from TimeEventBrain import TimeEventBrain
from Control import Control
from Tracks import Map0, Map1, Map2, Map3
from Database import Database
from Game import Game
from LiDAR import LiDAR

# game thread notifies brain as soon as the LiDAR data is ready
g_sync_cv = threading.Condition()

# brain thread notifies game when its computation is finished
# - if computation is too long, game thread is unlocked to guarantee the
#   minimum framerate
g_brain_cv = threading.Condition()

def main(auto, wrap, map_idx):
    map_list = [Map0, Map1, Map2, Map3]
    if map_idx not in range(len(map_list)):
        print("Invalid map index")
        return

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    walls, checkpoints, finish_line, car, hud_pos = map_list[map_idx]
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    # Get LiDAR data, Set Control data
    brain = Brain(database) if not cmd_file else TimeEventBrain(database)
    # Get Control data Set LiDAR data
    game = Game(walls, checkpoints, finish_line, car, database, hud_pos=hud_pos)

    brain_thread = None
    if auto:
        brain_thread = threading.Thread(target=brain.run, args=(g_sync_cv, g_brain_cv,))
        brain_thread.start()

    res_win  = None # win condition status
    res_time = None # total time
    res_dist = None # total distance
    res_ckpt = None # checkpoints

    if auto:
        res_win, res_time, res_dist, res_ckpt = game.runAuto(cv=g_sync_cv, bcv=g_brain_cv)
    else:
        res_win, res_time, res_dist, res_ckpt = game.runManual()

    if brain_thread is not None:
        brain_thread.join()

    if res_win is not None:
        if res_win:
            print("Congrats! You won")
        else:
            print("Too bad! You lose")

        print("### REPORT ###")
        print("Running time: {:.3f}".format(res_time / 1000.0))
        print("Running dist: {:.1f}".format(res_dist))
        if res_ckpt.items():
            print("Checkpoints:")
            for k, v in res_ckpt.items():
                print("- {} : time {:.03f} - dist: {:.1f}".format(k, v["time"] / 1000.0, v["distance"]))
    else:
        print("Exit")

    pygame.quit()

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-a", "--auto",
            help="Do not use your keyboard command,\
                 but use pre-defined brain's command.",
            action="store_true",
            default=False
            # type=bool
        )
    parser.add_argument(
            "-m", "--map",
            help="Choose which map to run [options 0 - 3]",
            action="store",
            default=0
        )
    parser.add_argument(
            "-f", "--file",
            help="Do not use your keyboard command,\
                 but use input.txt file to control the car.",
            action="store_true",
            default=False
        )
    args = parser.parse_args()
    main(args.auto, int(args.map), args.file)
