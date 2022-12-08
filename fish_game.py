import sys
import pygame
from pygame import mixer
from fish import Fish
from enemy_test import Enemy
from collect_item import Item

TILE = 64
pygame.init()
screen = pygame.display.set_mode((TILE*10, TILE*8))

water = pygame.image.load('assets/water_tile.png')
water_rect = water.get_rect()
screen_rect = screen.get_rect()

fish = Fish()
enemy = Enemy()
item = Item()

game_objects = pygame.sprite.Group()
game_objects.add(enemy, fish, item)
num_tiles = screen_rect.width // water_rect.width

def draw_background():
    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(water, (x*water_rect.width, y*water_rect.height))

coordinate = (0, 0)
clock = pygame.time.Clock()

mixer.init()
mixer.music.load('assets/Nyan Cat!.mp3')
mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit()

    fish.move(coordinate)
    enemy.move(screen_rect.width, screen_rect.height)
    item.move()

    collision = pygame.sprite.collide_rect(fish, enemy)
    if collision:
        print("You Hit The Fish!")

    draw_background()
    fish.draw(screen)
    enemy.draw(screen)
    item.draw(screen)
    pygame.display.flip()
    clock.tick(70)
