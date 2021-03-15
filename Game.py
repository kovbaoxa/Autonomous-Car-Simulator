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

# default frame duration in seconds
DFT_FRAME_DURATION = 0.0333
# maximum frame duration
MAX_FRAME_DURATION = 0.5
# default simulation time
DFT_SIM_DELTA_TIME = 0.0333

class Game:
    def __init__(self, walls, checkpoints, finish_line, car, database,
                 frame_duration = DFT_FRAME_DURATION,
                 sim_delta      = DFT_SIM_DELTA_TIME,
                 hud_pos        = {"x" : 850, "y" : 700}
        ):
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
        # frame duration in secs (can't be more than MAX_FRAME_DURATION)
        self.frame_duration = frame_duration if frame_duration <= MAX_FRAME_DURATION else MAX_FRAME_DURATION
        # simulation step duration in ms
        self.simulation_step = sim_delta * 1000.0
        # hud position
        self.hud_pos = hud_pos

    def draw_hud(self, millisec, distance, win):
        if self.hud_pos is not None:
            if win is None:
                time_overlay = self.font.render("Time: {:.03f}".format(millisec/1000.0), True, (255, 255, 255))
                dist_overlay = self.font.render("Dist: {:.1f}".format(distance), True, (255, 255, 255))
            else:
                if win:
                    time_overlay = self.font.render("Time: {:.03f}".format(millisec/1000.0), True, (0, 255, 0))
                    dist_overlay = self.font.render("Dist: {:.1f}".format(distance), True, (0, 255, 0))
                else:
                    time_overlay = self.font.render("Time: {:.03f}".format(millisec/1000.0), True, (255, 0, 0))
                    dist_overlay = self.font.render("Dist: {:.1f}".format(distance), True, (255, 0, 0))

            time_overlay_rect = time_overlay.get_rect()
            dist_overlay_rect = dist_overlay.get_rect()
            
            time_overlay_rect.center = (self.hud_pos['x'], self.hud_pos['y'])
            dist_overlay_rect.center = (self.hud_pos['x'], self.hud_pos['y'] + 50)

            self.screen.blit(time_overlay, time_overlay_rect)
            self.screen.blit(dist_overlay, dist_overlay_rect)

    def close(self):
        self.stop()
        self.running = False

    def stop(self):
        self.database.stop = True
        time.sleep(0.2)

    def run(self, auto=False, wrap=False, cv=None, bcv=None):

        print("Running at {:.0f} fps".format(1.0/self.frame_duration))

        output_file = open("output.txt", "w")
        input_file = open("input.txt", "r")

        ### Init running time and running speed
        self.database.runTime = 0.0
        self.database.run_dist = 0.0
        checkpoint_time = dict()

        # Getting car initial position
        car_current_pos_x, car_current_pos_y = self.database.car.position

        # Start simulation
        self.running = True

        while self.running:
            start_time = time.time()

            if auto:
                with bcv:
                    bcv.wait(self.frame_duration)
            else:
                ### generate new frame
                self.clock.tick_busy_loop(30)

            if self.win_condition is None:
                ### update running time
                if auto:
                    self.database.run_time += self.simulation_step
                else:
                    self.database.run_time += self.clock.get_time()

                ### update car position
                car_new_pos_x, car_new_pos_y = self.database.car.position
                self.database.run_dist += np.sqrt((car_new_pos_x - car_current_pos_x) ** 2 + (car_new_pos_y - car_current_pos_y) ** 2)
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
                    if wrap:
                        if self.win_condition is None:
                            self.parse_input(input_file)
                
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
                self.car_group.update()
            
            self.draw_hud(self.database.run_time, self.database.run_dist, self.win_condition)

            collisions = pygame.sprite.groupcollide(
                self.car_group, self.wall_group, False, False, collided=None)
            if collisions != {}:
                self.win_condition = False
                self.car_update = False
                self.car.image = pygame.image.load('images/collision.png')
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                self.car.k_right = 0
                self.car.k_left = 0

            for checkpoint in self.checkpoint_group:
                if pygame.sprite.spritecollide(checkpoint, self.car_group, False, False):
                    if checkpoint.name not in checkpoint_time.keys():
                        checkpoint_time[checkpoint.name] = {"distance" : self.database.run_dist, "time" : self.database.run_time}

            finish_collision = pygame.sprite.groupcollide(
                    self.car_group,
                    self.finish_group,
                    False,
                    False
                )

            if finish_collision != {}:
                self.win_condition = True
                self.car_update = False
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
            
            # write to output file
            for s in self.database.lidar.data.tolist():
                output_file.write("%.1f " % s)
            output_file.write("\n\n")


            if auto:
                with cv:
                    cv.notifyAll()
            
            exec_time = time.time() - start_time

            if(exec_time < self.frame_duration):
                time.sleep(self.frame_duration - exec_time)
                
        output_file.close()
        self.stop()

        return self.win_condition, self.database.run_time, self.database.run_dist, checkpoint_time


    def parse_input(self, file):
        commands = iter(file.read().split())        
        while True:
            try:
                cmd = next(commands)
                if cmd == "up":
                    for i in range(int(next(commands))):
                        self.car.k_up += 1
                if cmd == "down":
                    for i in range(int(next(commands))):
                        self.car.k_down -= 1
                if cmd == "right":
                    for i in range(int(next(commands))):
                        self.car.k_right -= 1
                if cmd == "left":
                    for i in range(int(next(commands))):
                        self.car.k_left += 1
            except StopIteration:
                print("No more commands")
                break

    def make_lidar_data(self):
        lidar_data = np.zeros((360))
        L = 300
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
