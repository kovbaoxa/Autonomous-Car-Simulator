import pygame
import numpy as np


class CheckpointSprite(pygame.sprite.Sprite):

    def __init__(self, position, width, height, name):
        super(CheckpointSprite, self).__init__()
        black_wall = 255 * np.ones((width, height, 3))
        self.name = name
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position
        self.image = self.normal

    def update(self):
        pass


if __name__ == "__main__":
    pygame.init()
    w = CheckpointSprite((10, 2), 1, 1, "test_checkpoint")
