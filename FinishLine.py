import pygame


class FinishLineSprite(pygame.sprite.Sprite):
    def __init__(self, position, size = 80, vertical=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/finish_line.png')
        self.image = pygame.transform.scale(self.image, (size, int(size/4)))
        if vertical:
            self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        x, y = position
        if vertical:
            self.rect.x = int(x - size / 8)
            self.rect.y = int(y - size / 2)
        else:
            self.rect.x = int(x - size / 2)
            self.rect.y = int(y - size / 8)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
