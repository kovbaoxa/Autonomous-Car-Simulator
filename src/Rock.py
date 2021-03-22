import pygame
import numpy as np


class Rock(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        black_wall = 255 * np.ones((30,20,3))
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position
        self.image = self.normal #pygame.image.load(image)

    def update(self):
        pass
