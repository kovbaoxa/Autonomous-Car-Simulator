import pygame


class Control:
    __MAX_SPEED_VARIATION = 5
    __MAX_TURNING_ANGLE   = 10

    def __init__(self):
        self.__speed_variation     = 0
        self.__direction_variation = 0

    def faster(self, val:int = 1):
        if val >= 0:
            self.__speed_variation = val if val <= self.__MAX_SPEED_VARIATION else self.__MAX_SPEED_VARIATION

    def slower(self, val:int = 1):
        if val >= 0:
            self.__speed_variation = -val if val <= self.__MAX_SPEED_VARIATION else -self.__MAX_SPEED_VARIATION

    def left(self, val:int = 1):
        if val >= 0:
            self.__direction_variation = val if val <= self.__MAX_TURNING_ANGLE else self.__MAX_TURNING_ANGLE

    def right(self, val:int = 1):
        if val >= 0:
            self.__direction_variation = -val if val <= self.__MAX_TURNING_ANGLE else -self.__MAX_TURNING_ANGLE

    def reset(self):
        self.__speed_variation     = 0
        self.__direction_variation = 0

    def speed_variation(self):
        return self.__speed_variation

    def direction_variation(self):
        return self.__direction_variation
