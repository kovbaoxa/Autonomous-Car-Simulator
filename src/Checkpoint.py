import pygame
import numpy as np


class CheckpointSprite(pygame.sprite.Sprite):

    def __init__(self, name, position, width = 80, height = 1, vertical=False):
        super(CheckpointSprite, self).__init__()
        self.name = name
        self.image = pygame.image.load('images/checkpoint.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        if vertical:
            self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        x, y = position

        if vertical:
            self.rect.x = int(x - height / 2)
            self.rect.y = int(y - width / 2)
        else:
            self.rect.x = int(x - width / 2)
            self.rect.y = int(y - height / 2)

    def update(self):
        pass


if __name__ == "__main__":
    pygame.init()
    w = CheckpointSprite((10, 2), 1, 1, "test_checkpoint")
