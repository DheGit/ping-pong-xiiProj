import pygame
from res.rgame import *

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.Surface([PADDLE_WIDTH,PADDLE_HEIGHT])
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()

    def moveUp(self,pixels):
        self.rect.y -= pixels

        if self.rect.y < SCORE_MARGIN:
            self.rect.y = SCORE_MARGIN

    def moveDown(self,pixels):
        self.rect.y += pixels

        if self.rect.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT
