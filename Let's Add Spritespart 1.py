import pygame
import random

pygame.init()



SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKROUND_COLOR_CHANGE = pygame.USEREVENT + 2



BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')


YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')



class Sprite(pygame.sprite.Sprite):


    def __init__(self,color,height,width):

        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

    
        self.rect = self.image.get.rect()

        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)

        boundray_hit = False

        if self.rect.left <= 0 or self.rect.bottom >= 500:
            self.velocity[0] = -self.velocity[0]
            boundray_hit = True
        
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundray_hit = True

        if boundray_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKROUND_COLOR_CHANGE))
    def change_color(self):
        self.image.fill(random.choice[YELLOW, MAGENTA, ORANGE, WHITE])