import pygame


class TrophySprite(pygame.sprite.Sprite):
    def __init__(self, position, size = 70):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/trophy.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        x, y = position
        self.rect.x = x - size / 2
        self.rect.y = y - size / 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)
