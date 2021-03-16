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

            if self.getCarSpeed() < 5:
                self.faster(1)

            ####################################################################
            # to HERE!!
            ####################################################################

            with bcv:
                bcv.notifyAll()

    ####################################################################
    # CAR CONTROL
    ####################################################################

    def faster(self, val: int = 5):
        self.database.control.faster(val)

    def slower(self, val: int = 5):
        self.database.control.slower(val)

    def right(self, val: int = 8):
        self.database.control.right(val)

    def left(self, val: int = 8):
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
