import pygame
import math
import inspect
import sys
import platform

from Authority import AuthorityExecption
from numpy import sqrt

class CarSprite(pygame.sprite.Sprite):
    __MAX_FORWARD_SPEED   = 15
    __MAX_REVERSE_SPEED   = 15

    def __init__(self, image, position, direction=0):
        pygame.sprite.Sprite.__init__(self)
        self.__src_image = pygame.image.load(image)
        self.__position = position
        self.__speed = 0
        self.__speed_variation = 0
        self.__dir_variation = 0
        self.__k_left = self.__k_right = self.__k_down = self.__k_up = 0
        self.__direction = direction
        self.update()

    def update(self, deltat=False):
        # SIMULATION
        self.__speed += (self.__speed_variation)
        if self.__speed > self.__MAX_FORWARD_SPEED:
            self.__speed = self.__MAX_FORWARD_SPEED
        if self.__speed < -self.__MAX_REVERSE_SPEED:
            self.__speed = -self.__MAX_REVERSE_SPEED
        self.__direction += (self.__dir_variation)
        self.__direction %= 360
        x, y = (self.__position)
        rad = self.__direction * math.pi / 180
        x += -self.__speed*math.sin(rad)
        y += -self.__speed*math.cos(rad)
        self.__position = (x, y)
        self.image =\
            pygame.transform.rotate(self.__src_image, self.__direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.__position

    def distance_from(self, point: tuple):
        return sqrt((self.__position[0] - point[0]) ** 2 + (self.__position[1] - point[1]) ** 2)

    def stop(self):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__speed           = 0
                self.__speed_variation = 0
                self.__dir_variation   = 0
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to \
                    change CarSprite.k_up at \'%s\'' % (
                        inspect.stack()[1][1].split('\\')[-1],
                        inspect.stack()[1][0])
                        )
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__speed           = 0
                self.__speed_variation = 0
                self.__dir_variation   = 0
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to \
                    change CarSprite.k_up at \'%s\'' % (
                        inspect.stack()[1][1].split('/')[-1],
                        inspect.stack()[1][0])
                        )

    @property
    def MAX_FORWARD_SPEED(self):
        return self.__MAX_FORWARD_SPEED

    @property
    def MAX_REVERSE_SPEED(self):
        return self.__MAX_REVERSE_SPEED

    @property
    def speed(self):
        return self.__speed

    @property
    def position(self):
        return self.__position

    @property
    def direction(self):
        return self.__direction

    @property
    def speed_variation(self):
        return self.__speed_variation

    @property
    def dir_variation(self):
        return self.__dir_variation

    @speed_variation.setter
    def speed_variation(self, val):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__speed_variation = val
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to \
                    change CarSprite.k_up at \'%s\'' % (
                        inspect.stack()[1][1].split('\\')[-1],
                        inspect.stack()[1][0])
                        )
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__speed_variation = val
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to \
                    change CarSprite.k_up at \'%s\'' % (
                        inspect.stack()[1][1].split('/')[-1],
                        inspect.stack()[1][0])
                        )

    @dir_variation.setter
    def dir_variation(self, val):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__dir_variation = val
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to \
                    change CarSprite.k_up at \'%s\'' % (
                        inspect.stack()[1][1].split('\\')[-1],
                        inspect.stack()[1][0])
                        )
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__dir_variation = val
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to \
                    change CarSprite.k_up at \'%s\'' % (
                        inspect.stack()[1][1].split('/')[-1],
                        inspect.stack()[1][0])
                        )
