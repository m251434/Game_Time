import pygame
from pygame.sprite import Sprite

class Fish(Sprite):
    def __init__(self):
        super().__init__()
        self.not_damaged_image = pygame.image.load('assets/mainR.png')
        self.slight_damaged_image = pygame.image.load('assets/main_1.png')
        self.very_damaged_image = pygame.image.load('assets/main_2.png')

        self.image = self.not_damaged_image
        self.rect = self.not_damaged_image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)
