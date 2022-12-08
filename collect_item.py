import pygame
import random
from pygame.sprite import Sprite



class Item(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/collect.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 600), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.top > 640:
            self.rect.top = 0
            self.rect.center = (random.randint(0, 640), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
