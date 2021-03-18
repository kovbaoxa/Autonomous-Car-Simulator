import time
import pygame
import numpy as np


class TimeEventBrain:
    def __init__(self, database):
        self.database = database
        self.command_queue = dict()

    def run(self, cv=None, bcv=None):
        with open("input.txt") as input_commands:
            for line in input_commands:
                # discard comment lines or empty lines
                line = line.rstrip('\n')
                if not line or line.startswith('#'):
                    continue
                self.parse_input(line)

        while self.isRunning():
            with cv:
                cv.wait()

            timestamp = self.database.timestamp

            if timestamp in self.command_queue.keys():
                for cmd, val in self.command_queue[timestamp]:
                    if cmd == "faster":
                        self.faster(val)
                    elif cmd == "slower":
                        self.slower(val)
                    elif cmd == "left":
                        self.left(val)
                    elif cmd == "right":
                        self.right(val)

            with bcv:
                bcv.notifyAll()

    ####################################################################
    # READ COMMANDS
    ####################################################################
    def parse_input(self, line):
        args = line.split('-')
        if len(args) != 2:
            print("Command {} is not correct".format(line))
        else:
            try:
                timestamp = int(args[0])
                command, value = args[1].split()
                if command in ("faster", "slower", "left", "right"):
                    if timestamp in self.command_queue.keys():
                        self.command_queue[timestamp].append((command, int(value)))
                    else:
                        self.command_queue[timestamp] = list()
                        self.command_queue[timestamp].append((command, int(value)))
                else:
                    print("Unknown command {}".format(line))
            except:
                print("Command {} is not correct".format(line))

    ####################################################################
    # CAR CONTROL
    ####################################################################

    def faster(self, val: int = 5):
        self.database.control.faster(val)

    def slower(self, val: int = 5):
        self.database.control.slower(val)

    def right(self, val: int = 10):
        self.database.control.right(val)

    def left(self, val: int = 10):
        self.database.control.left(val)

    ####################################################################
    # CAR SENSORS
    ####################################################################
    def getCarPosition(self):
        return self.database.car.position

    def getCarSpeed(self):
        return self.database.car.speed

    def getCarDirection(self):
        return self.database.car.direction

    def getLidarData(self):
        return self.database.lidar.data

    ####################################################################
    # SIMULATION INFO
    ####################################################################
    def isRunning(self):
        return not self.database.stop

    def getRunTime(self):
        return self.database.run_time

    def getRunDistance(self):
        return self.database.run_dist
