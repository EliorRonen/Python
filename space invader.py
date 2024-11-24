import math
import random
import pygame


SCREEN_WIDTH = 840
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 38
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27


pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


backround = pygame.image.load('the perfect photo.jpg')


pygame.display.set_caption("Space Invader")
icon = pygame.imahe.load('Best Premium Graphics on Freepik.jpg')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('download.jpg')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0


enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Warhammer 40k Pixel Art Space Marine.jpg'))