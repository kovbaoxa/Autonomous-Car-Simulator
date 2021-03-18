import argparse
import os
import threading
import pygame

from Brain import Brain
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

def main(auto, map_idx):
    map_list = [Map0, Map1, Map2, Map3]
    if map_idx not in range(len(map_list)):
        print("Invalid map index")
        return

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    walls, checkpoints, finish_line, car, hud_pos = map_list[map_idx]
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    game = Game(walls, checkpoints, finish_line, car, database, hud_pos=hud_pos)

    brain_thread = None
    if auto is not None:
        brain = Brain(database) if auto == "advanced" else  TimeEventBrain(database)
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
            help="Use brain function to drive the car. "\
                "Choose between 'simple' (time based) and 'advanced'",
            action="store",
            default=None
        )
    parser.add_argument(
            "-m", "--map",
            help="Choose which map to run [options 0 - 3]",
            action="store",
            default=0
        )
    args = parser.parse_args()
    main(args.auto, int(args.map))
