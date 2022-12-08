import pygame
from pygame.sprite import Sprite

class Fish(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/mainR.png')
        self.rect = self.image.get_rect()

        self.lives = 1

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)
