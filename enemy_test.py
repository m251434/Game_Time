import pygame
import random
from pygame.sprite import Sprite


class Enemy(Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/pufferfishR.png')
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 256

        self.direction = 1
        self.speed_x = 2
        self.speed_y = 2

    def move(self, WIDTH, HEIGHT):
        self.rect.left += self.speed_x
        self.rect.top += self.speed_y

        if self.rect.left < 0:
            self.direction *= -1
            self.speed_x = random.randint(1, 8) * self.direction
            # self.speed_y = random.randint(1, 8) * self.direction
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.direction *= -1
            self.speed_x = random.randint(1, 8) * self.direction
            # self.speed_y = random.randint(1, 8) * self.direction
            self.rect.right = WIDTH

        if self.rect.top < 0:
            self.direction *= -1
            # self.speed_x = random.randint(1, 8) * self.direction
            self.speed_y = random.randint(1, 8) * self.direction
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.direction *= -1
            # self.speed_x = random.randint(1, 8) * self.direction
            self.speed_y = random.randint(1, 8) * self.direction
            self.rect.bottom = HEIGHT

    def draw(self, surface):
        surface.blit(self.image, self.rect)

