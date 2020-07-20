import pygame
import random
import math
from res.rgame import *

class Ball(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface([BALL_WIDTH,BALL_HEIGHT])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.speed = 0
        self.x = 0
        self.y = 0
        self.direction = 0

        self.reset()

    def bounce(self,b_param):
        self.direction = (180-self.direction)%360
        self.direction += (b_param/PADDLE_HEIGHT)*PADDLE_BOUNCE_BIAS

    def reset(self):
        self.speed = 5.0
        self.y = random.randrange(BALL_RESET_Y_MARGIN + (SCORE_MARGIN//2), SCREEN_HEIGHT - BALL_RESET_Y_MARGIN + (SCORE_MARGIN//2))
        self.x = SCREEN_WIDTH/2 - BALL_WIDTH/2

        self.direction = random.randrange(-45,45)

        if random.randrange(2) == 0:
            self.direction += 180

    def update(self):        
        rads = math.radians(self.direction)

        self.x += math.cos(rads) * self.speed
        self.y -= math.sin(rads) * self.speed

        if self.x < -BALL_WIDTH*5 or self.x > SCREEN_WIDTH + BALL_WIDTH*5:
            self.reset()        

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.y <= SCORE_MARGIN:
                self.direction = (360-self.direction)%360
                self.y = 1 + SCORE_MARGIN
        if self.y >= SCREEN_HEIGHT-BALL_HEIGHT:
                self.direction = (360-self.direction)%360
                self.y = SCREEN_HEIGHT - BALL_HEIGHT - 1
