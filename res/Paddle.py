import pygame
from res.rgame import *

paddle_colour_default = (255,255,255)

class Paddle(pygame.sprite.Sprite):
    """
    The constructor. All the dimen parameters are in the order (width,height)
    """
    def __init__(self, screen_dimen, paddle_dimen, score_margin):
        
        super().__init__()
        
        self.image = pygame.Surface([paddle_dimen[0],paddle_dimen[1]])
        self.image.fill(paddle_colour_default)
        self.screen_dimen=screen_dimen
        self.paddle_dimen=paddle_dimen
        self.score_margin=score_margin

        self.rect = self.image.get_rect()

    def moveUp(self,pixels):
        self.rect.y -= pixels

        if self.rect.y < self.score_margin:
            self.rect.y = self.score_margin

    def moveDown(self,pixels):
        self.rect.y += pixels

        if self.rect.y > self.screen_dimen[1] - self.paddle_dimen[1]:
            self.rect.y = self.screen_dimen[1] - self.paddle_dimen[1]
