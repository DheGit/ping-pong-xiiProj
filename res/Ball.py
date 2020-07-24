import pygame
import random
import math

ball_color_default = (255,255,255)

class Ball(pygame.sprite.Sprite):
    """
    The constructor. All the dimen parameters are in the order (width,height)
    """
    def __init__(self, ball_dimen, screen_dimen, paddle_dimen, score_margin):

        super().__init__()

        self.image = pygame.Surface([ball_dimen[0] , ball_dimen[1]])
        self.image.fill(ball_color_default)

        self.rect = self.image.get_rect()

        self.speed = 0
        self.x = 0
        self.y = 0
        self.direction = 0
        self.bounce_bias=0
        self.reset_margin=0
        self.ball_dimen = ball_dimen
        self.screen_dimen = screen_dimen
        self.paddle_dimen = paddle_dimen
        self.score_margin=score_margin

        self.reset()

    def bounce(self,b_param):
        self.direction = (180-self.direction)%360
        self.direction += (b_param/self.paddle_dimen[1])*self.bounce_bias

    def reset(self):
        self.speed = 5.0
        self.y = random.randrange(self.reset_margin + self.score_margin , self.screen_dimen[1] - self.reset_margin)
        self.x = self.screen_dimen[0]/2 - self.ball_dimen[0]/2 

        self.direction = random.randrange(-45,45)

        if random.randrange(2) == 0:
            self.direction += 180

    def update(self):        
        rads = math.radians(self.direction)

        self.x += math.cos(rads) * self.speed
        self.y -= math.sin(rads) * self.speed

        if self.x < -self.ball_dimen[0]*5 or self.x > self.screen_dimen[0] + self.ball_dimen[0]*5:
            self.reset()        

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.y <= self.score_margin:
            self.direction = (360-self.direction)%360
            self.y = 1 + self.score_margin
        if self.y >= self.screen_dimen[1] - self.ball_dimen[1]:
            self.direction = (360-self.direction)%360
            self.y = self.screen_dimen[1] - self.ball_dimen[1] - 1

    def setBounceBias(self, bias):
        self.bounce_bias = bias

    def setResetMargin(self, margin):
        self.reset_margin = margin

    def setBallSpeed(self, speed):
        self.speed = speed
