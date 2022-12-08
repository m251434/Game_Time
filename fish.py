import pygame
from pygame.sprite import Sprite
from collect_item import Item

class Fish(Sprite):
    item = Item()
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/mainR.png')
        self.big_fish_image = pygame.image.load('assets/big_fish.png')
        self.rect = self.image.get_rect()

        self.lives = 1

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self, surface):
        surface.blit(self.image, self.rect)

