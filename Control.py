import pygame

class Control:
    __MAX_SPEED_VARIATION = 5
    __MAX_TURNING_ANGLE   = 10

    def __init__(self):
        self.__speed_increase  = 0
        self.__speed_decrease  = 0
        self.__direction_left  = 0
        self.__direction_right = 0

    def faster(self, val:int = 1):
        self.__speed_increase = val if val <= self.__MAX_SPEED_VARIATION else self.__MAX_SPEED_VARIATION
        self.__speed_decrease = 0

    def slower(self, val:int = 1):
        self.__speed_increase = 0
        self.__speed_decrease = val if val <= self.__MAX_SPEED_VARIATION else self.__MAX_SPEED_VARIATION

    def left(self, val:int = 1):
        self.__direction_left = val if val <= self.__MAX_TURNING_ANGLE else self.__MAX_TURNING_ANGLE
        self.__direction_right = 0

    def right(self, val:int = 1):
        self.__direction_left  = 0
        self.__direction_right = val if val <= self.__MAX_TURNING_ANGLE else self.__MAX_TURNING_ANGLE

    def reset(self):
        self.__speed_increase  = 0
        self.__speed_decrease  = 0
        self.__direction_left  = 0
        self.__direction_right = 0

    def speed_variation(self):
        return self.__speed_increase - self.__speed_decrease

    def direction_variation(self):
        return self.__direction_left - self.__direction_right
