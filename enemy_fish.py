import pygame
import random
from pygame.sprite import Sprite

class Enemy(Sprite):
    enemyR = [pygame.image.load('assets/pufferfishR.png')]
    enemyL = [pygame.image.load('assets/pufferfishL.png')]

    def __init__(self, x, y, width, height, end):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]

        self.swimCount = 0
        self.vel = 4
        self.x = random.randint(0, 896)
        self.y = random.randint(64, 512)

    def draw(self, win):
        self.move()
        if self.swimCount + 1 >= 2:
            self.swimCount = 0
        if self.vel > 0:
            win.blit(self.enemyR[self.swimCount // 2], (self.x, self.y))

        else:
            win.blit(self.enemyL[self.swimCount // 2], (self.x, self.y))
            self.swimCount += 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.swimCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.swimCount = 0