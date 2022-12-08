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

game_objects = pygame.sprite.Group()
game_objects.add(enemy, fish)
num_tiles = screen_rect.width // water_rect.width

fish_img = pygame.image.load('assets/main_2.png')
fish_mini_img = pygame.transform.scale(fish_img, (50, 50))


def draw_background():

    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(water, (x*water_rect.width, y*water_rect.height))


def draw_lives(surface, x, y, lives, img):

    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 35 * i
        img_rect.y = y
        surface.blit(img, img_rect)

coordinate = (0, 0)
clock = pygame.time.Clock()


mixer.init()
mixer.music.load('assets/Nyan Cat!.mp3')
mixer.music.play()

running = True
while True:
    collision1 = pygame.sprite.collide_rect(fish, enemy)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fish.move(coordinate)
    enemy.move(screen_rect.width, screen_rect.height)

    if collision1:
        fish.lives -= 1
        fish.kill()
        running = False

    draw_background()
    draw_lives(screen, screen_rect.width - 50, 10, fish.lives, fish_mini_img)
    fish.draw(screen)
    enemy.draw(screen)
    pygame.display.flip()
    clock.tick(70)
