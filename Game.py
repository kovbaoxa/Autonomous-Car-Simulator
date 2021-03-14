import copy
import math
import time

import numpy as np
import pygame
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP,
                           KEYDOWN, USEREVENT)

from Car import CarSprite
from Trophy import TrophySprite
from Wall import WallSprite

class Game:
    def __init__(self, walls, checkpoints, finish_line, 
                 car, database):
        self.init_args =\
            [
                copy.copy(walls),
                copy.copy(checkpoints),
                copy.copy(car),
                database
            ]
        pygame.init()
        self.car = car
        self.screen = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.win_condition = None
        self.wall_group = pygame.sprite.RenderPlain(*walls)
        self.checkpoint_group = pygame.sprite.RenderPlain(*checkpoints)
        self.finish_group = pygame.sprite.RenderPlain(*finish_line)
        self.car_group = pygame.sprite.RenderPlain(car)
        self.rect = self.screen.get_rect()
        self.running = False
        self.car_update = True
        self.database = database

    def draw_hud(self, time, distance, win):
        if win is None:
            time_overlay = self.font.render("Time: " + str(round(time/1000.0, 2)), True, (255, 255, 255))
            dist_overlay = self.font.render("Dist: " + str(round(distance, 2)), True, (255, 255, 255))
        else:
            if win:
                time_overlay = self.font.render("Time: " + str(round(time/1000.0, 2)), True, (0, 255, 0))
                dist_overlay = self.font.render("Dist: " + str(round(distance, 2)), True, (0, 255, 0))
            else:
                time_overlay = self.font.render("Time: " + str(round(time/1000.0, 2)), True, (255, 0, 0))
                dist_overlay = self.font.render("Dist: " + str(round(distance, 2)), True, (255, 0, 0))

        time_overlay_rect = time_overlay.get_rect()
        dist_overlay_rect = dist_overlay.get_rect()
        
        time_overlay_rect.center = (850,700)
        dist_overlay_rect.center = (850,750)

        self.screen.blit(time_overlay, time_overlay_rect)
        self.screen.blit(dist_overlay, dist_overlay_rect)

    def close(self):
        self.stop()
        self.running = False

    def stop(self):
        self.database.stop = True
        time.sleep(0.2)

    def run(self, auto=False):
        seconds = 0
        distance = 0.0
        checkpoint_time = dict()

        # Getting car initial position
        car_current_pos_x, car_current_pos_y = self.database.car.position

        self.running = True
        while self.running:
            ### generate new frame
            deltat = self.clock.tick_busy_loop(30)

            if self.win_condition is None:
                ### update running time
                seconds += self.clock.get_time()

                ### update car position
                car_new_pos_x, car_new_pos_y = self.database.car.position
                distance += np.sqrt((car_new_pos_x - car_current_pos_x) ** 2 + (car_new_pos_y - car_current_pos_y) ** 2)
                car_current_pos_x = car_new_pos_x
                car_current_pos_y = car_new_pos_y
            else:
                self.stop()

            events = pygame.event.get()

            if auto:
                self.car.k_right = self.car.k_left =\
                    self.car.k_up = self.car.k_down = 0
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()
                    break
                if auto:
                    if not hasattr(event, 'key'):
                        continue
                    if event.type != USEREVENT and (
                            event.key == K_RIGHT or
                            event.key == K_LEFT or
                            event.key == K_UP or
                            event.key == K_DOWN
                            ):
                        continue
                    if self.win_condition is None:
                        if event.key == K_RIGHT:
                            if self.car.k_right > -8:
                                self.car.k_right += -1
                        elif event.key == K_LEFT:
                            if self.car.k_left < 8:
                                self.car.k_left += 1
                        elif event.key == K_UP:
                            if self.car.k_up < 5:
                                self.car.k_up += 1
                        elif event.key == K_DOWN:
                            if self.car.k_down > -5:
                                self.car.k_down += -1
                        elif event.key == K_ESCAPE:
                            self.close()
                    elif self.win_condition is True and event.key == K_SPACE:
                        self.close()
                    elif self.win_condition is False and event.key == K_SPACE:
                        self.close()
                    elif event.key == K_ESCAPE:
                        self.close()
                else:
                    if not hasattr(event, 'key'):
                        continue
                    down = event.type == KEYDOWN
                    if self.win_condition is None:
                        if event.key == K_RIGHT:
                            self.car.k_right = down * -5
                        elif event.key == K_LEFT:
                            self.car.k_left = down * 5
                        elif event.key == K_UP:
                            self.car.k_up = down * 2
                        elif event.key == K_DOWN:
                            self.car.k_down = down * -2
                        elif event.key == K_ESCAPE:
                            self.close()
                    elif self.win_condition is True and event.key == K_SPACE:
                        self.close()
                    elif self.win_condition is False and event.key == K_SPACE:
                        self.close()
                    elif event.key == K_ESCAPE:
                        self.close()

            # RENDERING
            self.screen.fill((0, 0, 0))
            if self.car_update:
                self.car_group.update(deltat)
            
            self.draw_hud(seconds, distance, self.win_condition)

            collisions = pygame.sprite.groupcollide(
                self.car_group, self.wall_group, False, False, collided=None)
            if collisions != {}:
                self.car_update = False
                self.win_condition = False
                self.car.image = pygame.image.load('images/collision.png')
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                self.car.k_right = 0
                self.car.k_left = 0

            for checkpoint in self.checkpoint_group:
                if pygame.sprite.spritecollide(checkpoint, self.car_group, False, False):
                    if checkpoint.name not in checkpoint_time.keys():
                        print("Checkpoint ", checkpoint.name, ":", distance, " at ", seconds)
                        checkpoint_time[checkpoint.name] = {"distance" : distance, "time" : seconds}

            finish_collision = pygame.sprite.groupcollide(
                    self.car_group,
                    self.finish_group,
                    False,
                    False
                )

            if finish_collision != {}:
                self.win_condition = True
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0

            self.wall_group.update()
            self.checkpoint_group.update()

            self.wall_group.draw(self.screen)
            self.checkpoint_group.draw(self.screen)
            self.finish_group.draw(self.screen)
            self.car_group.draw(self.screen)
            # Counter Render
            pygame.display.flip()

            self.make_lidar_data()

        self.stop()

        if self.win_condition:
            print("You win!")
        else:
            print("You lose!")

        return seconds, distance, checkpoint_time

    def again(self, auto):
        self.__init__(*self.init_args)
        self.run(auto=auto)

    def make_lidar_data(self):
        lidar_data = np.zeros((360))
        L = 100
        array = pygame.surfarray.array3d(self.screen)
        car = self.database.car
        x, y = car.position

        car_direction = car.direction % 360

        lidar_x = int(x - 20 * math.sin(math.pi * car_direction / 180))
        lidar_y = int(y - 20 * math.cos(math.pi * car_direction / 180))

        for direction in range(-90 + car_direction, 90 + car_direction):
            direction = direction % 360

            x, y = lidar_x, lidar_y
            m = math.tan(math.pi * direction / 180)
            if direction == 0:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x = x
                    y -= 1
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (0 < direction < 45) or (315 <= direction < 360):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    y -= 1
                    x = (m) * (y - lidar_y) + lidar_x
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (45 <= direction < 90) or (90 < direction < 135):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x -= 1
                    y = (1 / m) * (x - lidar_x) + lidar_y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 90:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x -= 1
                    y = y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (135 <= direction < 180) or (180 < direction < 225):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    y += 1
                    x = (m) * (y - lidar_y) + lidar_x
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 180:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x = x
                    y += 1
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (225 <= direction < 270) or (270 < direction < 315):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x += 1
                    y = (1 / m) * (x - lidar_x) + lidar_y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 270:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x += 1
                    y = y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            else:
                print(f"Uncatched Case: {direction}")

            length = math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2)
            if length > L:
                length = L

            lidar_data[direction] = length

        lidar_data = np.concatenate(
            (lidar_data[-90:], lidar_data[:270]), axis=None
            )
        lidar_data = np.concatenate(
            (lidar_data, lidar_data), axis=None
            )
        lidar_data =\
            lidar_data[self.car.direction % 360:
                       self.car.direction % 360 + 180]
        self.database.lidar.data = lidar_data
