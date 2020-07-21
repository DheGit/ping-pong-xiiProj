import pygame
import random
import math
from res.rgame import *
from res.Paddle import *
from res.Ball import *

pygame.init()

screen_size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ping Pong")
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

score1 = 0
score2 = 0
lastUp1 = FPS
lastUp2 = FPS

paddle1 = Paddle(screen_size, (PADDLE_WIDTH,PADDLE_HEIGHT),SCORE_MARGIN)
paddle1.rect.x = PADDLE_MARGIN
paddle1.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2 + SCORE_MARGIN//2

paddle2 = Paddle(screen_size, (PADDLE_WIDTH,PADDLE_HEIGHT),SCORE_MARGIN)
paddle2.rect.x = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_MARGIN
paddle2.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2 + SCORE_MARGIN//2

ball = Ball((BALL_WIDTH,BALL_HEIGHT),screen_size,(PADDLE_WIDTH,PADDLE_HEIGHT), SCORE_MARGIN)
ball.setResetMargin(BALL_RESET_Y_MARGIN)
ball.setBounceBias(PADDLE_BOUNCE_BIAS)
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

def updateScore(playerNum):
    global lastUp1, lastUp2,score1,score2
    if playerNum == 1 and lastUp1 >= FPS:
        score1 += 1
        lastUp1 = 0
    if playerNum == 2 and lastUp2 >= FPS:
        score2 += 1
        lastUp2 = 0

exit_window=False

while not exit_window:

    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    exit_window = True
        
    if ball.x > PADDLE_MARGIN + PADDLE_WIDTH and ball.x < SCREEN_WIDTH - (PADDLE_MARGIN + PADDLE_WIDTH):
        lastUp1 += 1
        lastUp2 += 1
    ball.update()
    
    if collides() == 1:
        diff = (paddle1.rect.y + PADDLE_HEIGHT/2) - (ball.rect.y+BALL_HEIGHT/2)
        ball.x = PADDLE_MARGIN+PADDLE_WIDTH + 2
        ball.bounce(diff)
        updateScore(1)

    if collides() == 2:
        diff = (paddle2.rect.y + PADDLE_HEIGHT/2) - (ball.rect.y+BALL_HEIGHT/2) 
        ball.x = SCREEN_WIDTH - (PADDLE_MARGIN+BALL_WIDTH+2)
        ball.bounce(-diff)
        updateScore(2)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        paddle1.moveUp(PADDLE_SPEED)
    if keys[pygame.K_s]:
        paddle1.moveDown(PADDLE_SPEED)
    if keys[pygame.K_UP]:
        paddle2.moveUp(PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(PADDLE_SPEED)

    if keys[pygame.K_ESCAPE]:
        exit_window = True

    movingsprites.update()

    pygame.draw.line(screen,WHITE,[SCREEN_WIDTH//2,0],[SCREEN_WIDTH//2,SCREEN_HEIGHT],5)

    pygame.draw.line(screen,WHITE,[0,SCORE_MARGIN],[SCREEN_WIDTH,SCORE_MARGIN],5)

    movingsprites.draw(screen)
    
    font = pygame.font.Font(None,74)
    
    text1 = font.render(str(score1),1,WHITE)
    screen.blit(text1,((SCREEN_WIDTH//2)//2,10))
    
    text2 = font.render(str(score2),1,WHITE)
    screen.blit(text2,(3*((SCREEN_WIDTH//2)//2),10))
    
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
