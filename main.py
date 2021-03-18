import argparse
import os
import threading

import pygame

from Control import Control
from Tracks import Map0
from Database import Database
from Game import Game
from LiDAR import LiDAR

# game thread notifies brain as soon as the LiDAR data is ready
g_sync_cv = threading.Condition()

# brain thread notifies game when its computation is finished
# - if computation is too long, game thread is unlocked to guarantee the
#   minimum framerate
g_brain_cv = threading.Condition()

def main():

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    walls, finish_line, car, hud_pos = Map0
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    game = Game(walls, finish_line, car, database, hud_pos=hud_pos)

    res_win  = None # win condition status
    res_time = None # total time
    res_dist = None # total distance

    res_win, res_time, res_dist = game.runManual()

    if res_win is not None:
        if res_win:
            print("Congrats! You won")
        else:
            print("Too bad! You lose")

        print("### REPORT ###")
        print("Running time: {:.3f}".format(res_time / 1000.0))
        print("Running dist: {:.1f}".format(res_dist))

    else:
        print("Exit")

    pygame.quit()

    return 0


if __name__ == "__main__":
    main()
