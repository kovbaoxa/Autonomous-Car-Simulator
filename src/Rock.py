import pygame
import numpy as np


class Rock(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        black_wall = 255 * np.ones((30,30,3))
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect.center = position

        # self.original_pos = position
        # self.up = True


    def update(self):
        pass
        # pos = self.rect.center
        # if self.up:
        #     if pos[1] > self.original_pos[1] - 40:
        #         new_pos = (pos[0], pos[1] - 4)
        #     else:
        #         self.up = False
        #         new_pos = (pos[0], pos[1] + 4)
        # else:
        #     if pos[1] < self.original_pos[1] + 40:
        #         new_pos = (pos[0], pos[1] + 4)
        #     else:
        #         self.up = True
        #         new_pos = (pos[0], pos[1] - 4)
        # self.rect.center = new_pos
