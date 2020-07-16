import pygame
import random
import math

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 120
PADDLE_MARGIN = 20
BALL_WIDTH = 17
BALL_HEIGHT = 17
BALL_RESET_Y_MARGIN=50

size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
pygame.mouse.set_visible(0)

screen.fill(BLACK)
pygame.draw.line(screen,WHITE,[SCREEN_WIDTH//2,0],[SCREEN_WIDTH//2,SCREEN_HEIGHT],4)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.Surface([PADDLE_WIDTH,PADDLE_HEIGHT])
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface([BALL_WIDTH,BALL_HEIGHT])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

        self.speed = 0
        self.x=0
        self.y=0
        self.direction=0

        self.reset()

    def reset(self):
    	self.speed=8.0
    	self.y=random.randrange(BALL_RESET_Y_MARGIN, SCREEN_HEIGHT - BALL_RESET_Y_MARGIN)
    	self.x=PADDLE_MARGIN

    	self.direction=random.randrange(-45,45)

    	if random.randrange(2)==0:
    		self.direction += 180
    		self.x=SCREEN_WIDTH - BALL_WIDTH - PADDLE_MARGIN

    def update(self):
    	rads=math.radians(self.direction)

    	self.x += math.cos(rads) * self.speed
    	self.y -= math.sin(rads) * self.speed

    	if self.x < 0 or self.x > SCREEN_WIDTH:
    		self.reset()

    	self.rect.x=int(self.x)
    	self.rect.y=int(self.y)

clock=pygame.time.Clock()

paddle1 = Paddle()
paddle1.rect.x = PADDLE_MARGIN
paddle1.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2

paddle2 = Paddle()
paddle2.rect.x = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_MARGIN
paddle2.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2

ball = Ball()
ball.reset()
ball.update()

movingsprites = pygame.sprite.Group()
movingsprites.add(paddle1)
movingsprites.add(paddle2)
movingsprites.add(ball)

exit_window=False

while not exit_window:

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit_window=True

	ball.update()
	print("Ball Speed: ", ball.speed)
	
	screen.fill(BLACK)
	movingsprites.draw(screen)
	pygame.display.flip()

	clock.tick(30)

pygame.quit()
