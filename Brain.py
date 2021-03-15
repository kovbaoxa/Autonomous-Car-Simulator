import time
import pygame

class Brain:
    def __init__(self, database):
        self.database = database

    def run(self, cv=None, bcv=None):
        while self.isRunning():
            with cv:
                cv.wait()

            '''
            DO NOT CHANGE CODE ABOVE!!!!

            1. How can i get a lidar data?
                data = self.database.lidar.data

            2. How can i move a car?
                self.up(num)
                self.down(num)
                self.right(num)
                self.left(num)

                In one loop, you can only change the speed up to 5 and the angle up to 8

            3. How can i get a car status data?
                self.getCarSpeed()
                self.getCarDirection()

            '''
            ####################################################################
            # Implement Your Algorithm form HERE...
            ####################################################################

            # Simulation data
            print("Time: {:.3f} - Distance: {:.1f}".format(self.getRunTime() / 1000.0, self.getRunDistance()))

            # Car data
            print("Direction: {} - Speed: {}".format(self.getCarDirection(), self.getCarSpeed()))

            if self.getCarSpeed() <= 5:
                self.up(1)

            if(self.getCarDirection() > 0):
                self.right(1)
            else:
                self.left(1)

            ####################################################################
            # to HERE!!
            ####################################################################

            with bcv:
                bcv.notifyAll()

    ####################################################################
    # CAR CONTROL
    ####################################################################

    def up(self, num: int = 1):
        self.database.control.up(num)

    def down(self, num: int = 1):
        self.database.control.down(num)

    def right(self, num: int = 1):
        self.database.control.right(num)

    def left(self, num: int = 1):
        self.database.control.left(num)

    ####################################################################
    # SIMULATION INFO
    ####################################################################
    def isRunning(self):
        return not self.database.stop

    def getCarSpeed(self):
        return self.database.car.speed

    def getCarDirection(self):
        return self.database.car.direction

    def getRunTime(self):
        return self.database.run_time

    def getRunDistance(self):
        return self.database.run_dist

    def getLidarData(self):
        return self.database.lidar.data
