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
PADDLE_BOUNCE_BIAS=80

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

    def bounce(self, b_param):
    	self.direction = (180-self.direction)%360
    	self.direction += (b_param/PADDLE_HEIGHT)*PADDLE_BOUNCE_BIAS

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

    	if self.x < -BALL_WIDTH*20 or self.x > SCREEN_WIDTH + BALL_WIDTH*20:
    		self.reset()

    	self.rect.x=int(self.x)
    	self.rect.y=int(self.y)

    	if self.y<=0 or self.y>=SCREEN_HEIGHT - BALL_HEIGHT:
    		self.direction = (360-self.direction)%360

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

ball_group = pygame.sprite.Group()
ball_group.add(ball)

def collides():
	if (ball.x <= PADDLE_MARGIN + PADDLE_WIDTH and ball.x >= PADDLE_MARGIN + PADDLE_WIDTH - ball.speed*2) and (ball.y >= paddle1.rect.y and ball.y <=paddle1.rect.y + PADDLE_HEIGHT):
		return 1
	if (ball.x >= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH) and ball.x <= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH) + ball.speed*2)and (ball.y >= paddle2.rect.y and ball.y <=paddle2.rect.y + PADDLE_HEIGHT):
		return 2
	return 0

movingsprites = pygame.sprite.Group()
movingsprites.add(paddle1)
movingsprites.add(paddle2)
movingsprites.add(ball)

exit_window=False

while not exit_window:
	screen.fill(BLACK)
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit_window=True

	ball.update()
	
	if collides() == 1:
		diff = (paddle1.rect.y + PADDLE_HEIGHT/2) - (ball.rect.y+BALL_HEIGHT/2)
		ball.x = PADDLE_MARGIN+PADDLE_WIDTH +1
		ball.bounce(diff)

	if collides() == 2:
		diff = (paddle2.rect.y + PADDLE_HEIGHT/2) - (ball.rect.y+BALL_HEIGHT/2) 
		ball.x = SCREEN_WIDTH - (PADDLE_MARGIN+BALL_WIDTH+1)
		ball.bounce(-diff)

	movingsprites.draw(screen)
	pygame.display.flip()

	clock.tick(100) #Kept it that high only for testing purposes, change it to a comfortable 30-40 later.

pygame.quit()
