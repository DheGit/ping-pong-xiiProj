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
PADDLE_SPEED=15

BALL_WIDTH = 17
BALL_HEIGHT = 17
BALL_RESET_Y_MARGIN=50

size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
pygame.mouse.set_visible(0)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.Surface([PADDLE_WIDTH,PADDLE_HEIGHT])
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()

    def moveUp(self,pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self,pixels):
        self.rect.y += pixels

        if self.rect.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT

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
        self.x=SCREEN_WIDTH/2 - BALL_WIDTH/2

        self.direction=random.randrange(-45,45)

        if random.randrange(2)==0:
            self.direction += 180

    def update(self):        
    	rads=math.radians(self.direction)

    	self.x += math.cos(rads) * self.speed
    	self.y -= math.sin(rads) * self.speed

    	if self.x < -BALL_WIDTH*20 or self.x > SCREEN_WIDTH + BALL_WIDTH*20:
            self.reset()	

    	self.rect.x = int(self.x)
    	self.rect.y = int(self.y)

    	if self.y<=0:
    		self.direction=(360-self.direction)%360
    		self.y = 1
    	if self.y>=SCREEN_HEIGHT-BALL_HEIGHT:
    		self.direction=(360-self.direction)%360
    		self.y = SCREEN_HEIGHT - BALL_HEIGHT - 1

clock=pygame.time.Clock()

score1=0
score2=0

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

def collides():
    if (ball.x <= PADDLE_MARGIN + PADDLE_WIDTH and ball.x >= PADDLE_MARGIN + PADDLE_WIDTH - ball.speed*2) and (ball.y >= paddle1.rect.y and ball.y <=paddle1.rect.y + PADDLE_HEIGHT):
        return 1
    if (ball.x >= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH) and ball.x <= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH) + ball.speed*2)and (ball.y >= paddle2.rect.y and ball.y <=paddle2.rect.y + PADDLE_HEIGHT):
        return 2
    return 0

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
        score1 += 1

    if collides() == 2:
        diff = (paddle2.rect.y + PADDLE_HEIGHT/2) - (ball.rect.y+BALL_HEIGHT/2) 
        ball.x = SCREEN_WIDTH - (PADDLE_MARGIN+BALL_WIDTH+1)
        ball.bounce(-diff)
        score2+=1

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        paddle1.moveUp(PADDLE_SPEED)
    if keys[pygame.K_s]:
        paddle1.moveDown(PADDLE_SPEED)
    if keys[pygame.K_UP]:
        paddle2.moveUp(PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(PADDLE_SPEED)

    movingsprites.update()

    screen.fill(BLACK)
    pygame.draw.line(screen,WHITE,[SCREEN_WIDTH//2,0],[SCREEN_WIDTH//2,SCREEN_HEIGHT],5)

    movingsprites.draw(screen)
    
    #Erroneous code block. It updates the score decades of times when the ball crosses the line in concern
    #So it is wise to count every collision as a score of the respective player.
    #We can change scoring system later
#    if ball.rect.x >= SCREEN_WIDTH - BALL_WIDTH:
#        score1 += 1
#    if ball.rect.x <= 0:
#        score2 += 1
    
    font = pygame.font.Font(None,74)
    
    text1 = font.render(str(score1),1,WHITE)
    screen.blit(text1,((SCREEN_WIDTH//2)//2,10))
    
    text2 = font.render(str(score2),1,WHITE)
    screen.blit(text2,(3*((SCREEN_WIDTH//2)//2),10))
    
    pygame.display.flip()

    clock.tick(45) #Kept it that high only for testing purposes, change it to a comfortable 30-40 later.

pygame.quit()
