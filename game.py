import pygame

from enum import Enum

import r
from sprites.UIElement import *
from sprites.Paddle import *
from sprites.Ball import *

screen_size = (r.game.SCREEN_WIDTH,r.game.SCREEN_HEIGHT)

paddle1 = Paddle(screen_size, (r.game.PADDLE_WIDTH,r.game.PADDLE_HEIGHT), r.game.SCORE_MARGIN)
paddle2 = Paddle(screen_size, (r.game.PADDLE_WIDTH,r.game.PADDLE_HEIGHT), r.game.SCORE_MARGIN)
ball = Ball((r.game.BALL_WIDTH,r.game.BALL_HEIGHT), screen_size, (r.game.PADDLE_WIDTH,r.game.PADDLE_HEIGHT), r.game.SCORE_MARGIN)

score1 = 0
score2 = 0
lastUp1 = r.game.FPS
lastUp2 = r.game.FPS

def collides():
    if (ball.x <= r.game.PADDLE_MARGIN + r.game.PADDLE_WIDTH and ball.x >= r.game.PADDLE_MARGIN + r.game.PADDLE_WIDTH - ball.speed*3) and (ball.y + r.game.BALL_HEIGHT >= paddle1.rect.y and ball.y <=paddle1.rect.y + r.game.PADDLE_HEIGHT):
        return 1
    if (ball.x >= r.game.SCREEN_WIDTH - (r.game.PADDLE_MARGIN + r.game.BALL_WIDTH + r.game.PADDLE_WIDTH) and ball.x <= r.game.SCREEN_WIDTH - (r.game.PADDLE_MARGIN + r.game.BALL_WIDTH + r.game.PADDLE_WIDTH) + ball.speed*3)and (ball.y + r.game.BALL_HEIGHT>= paddle2.rect.y and ball.y <=paddle2.rect.y + r.game.PADDLE_HEIGHT):
        return 2
    return 0

def updateScore(playerNum):
    global lastUp1, lastUp2,score1,score2
    if playerNum == 1 and lastUp1 >= r.game.FPS:
        score1 += 1
        lastUp1 = 0
    if playerNum == 2 and lastUp2 >= r.game.FPS:
        score2 += 1
        lastUp2 = 0

def play_game(screen):
    global score1,score2, lastUp1,lastUp2, paddle1,paddle2, ball, screen_size
    pygame.display.set_caption("Ping Pong")

    clock = pygame.time.Clock()

    paddle1.rect.x = r.game.PADDLE_MARGIN
    paddle1.rect.y = r.game.SCREEN_HEIGHT//2 - r.game.PADDLE_HEIGHT//2 + r.game.SCORE_MARGIN//2

    paddle2.rect.x = r.game.SCREEN_WIDTH - r.game.PADDLE_WIDTH - r.game.PADDLE_MARGIN
    paddle2.rect.y = r.game.SCREEN_HEIGHT//2 - r.game.PADDLE_HEIGHT//2 + r.game.SCORE_MARGIN//2

    ball.setResetMargin(r.game.BALL_RESET_Y_MARGIN)
    ball.setBounceBias(r.game.PADDLE_BOUNCE_BIAS)
    ball.reset()
    ball.update()

    movingsprites = pygame.sprite.Group()
    movingsprites.add(paddle1)
    movingsprites.add(paddle2)
    movingsprites.add(ball)
    
    exit_window = False
    
    while not exit_window:

        screen.fill(r.game.BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        exit_window = True
            
        if ball.x > r.game.PADDLE_MARGIN + r.game.PADDLE_WIDTH and ball.x < r.game.SCREEN_WIDTH - (r.game.PADDLE_MARGIN + r.game.PADDLE_WIDTH):
            lastUp1 += 1
            lastUp2 += 1
        ball.update()
        
        if collides() == 1:
            diff = (paddle1.rect.y + r.game.PADDLE_HEIGHT/2) - (ball.rect.y+r.game.BALL_HEIGHT/2)
            ball.x = r.game.PADDLE_MARGIN+r.game.PADDLE_WIDTH + 2
            ball.bounce(diff)
            updateScore(1)

        if collides() == 2:
            diff = (paddle2.rect.y + r.game.PADDLE_HEIGHT/2) - (ball.rect.y+r.game.BALL_HEIGHT/2) 
            ball.x = r.game.SCREEN_WIDTH - (r.game.PADDLE_MARGIN+r.game.BALL_WIDTH+r.game.PADDLE_WIDTH+2)
            ball.bounce(-diff)
            updateScore(2)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            paddle1.moveUp(r.game.PADDLE_SPEED)
        if keys[pygame.K_s]:
            paddle1.moveDown(r.game.PADDLE_SPEED)
        if keys[pygame.K_UP]:
            paddle2.moveUp(r.game.PADDLE_SPEED)
        if keys[pygame.K_DOWN]:
            paddle2.moveDown(r.game.PADDLE_SPEED)

        if keys[pygame.K_ESCAPE]:
            exit_window = True
            
        if keys[pygame.K_F11]:
            screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        movingsprites.update()

        pygame.draw.line(screen,r.game.WHITE,[r.game.SCREEN_WIDTH//2,r.game.SCORE_MARGIN],[r.game.SCREEN_WIDTH//2,r.game.SCREEN_HEIGHT],5)

        pygame.draw.line(screen,r.game.WHITE,[0,r.game.SCORE_MARGIN],[r.game.SCREEN_WIDTH,r.game.SCORE_MARGIN],5)

        movingsprites.draw(screen)
        
        font = pygame.font.Font(None,74)
        
        text1 = font.render(str(score1),1,r.game.WHITE)
        screen.blit(text1,((r.game.SCREEN_WIDTH//2)//2,10))
        
        text2 = font.render(str(score2),1,r.game.WHITE)
        screen.blit(text2,(3*((r.game.SCREEN_WIDTH//2)//2),10))

        if score1 == 10 or score2 == 10:
            screen.fill(r.game.BLACK)
            text3 = font.render("WINS",1,r.game.WHITE)
            text4 = font.render("PLAYER 1",1,r.game.WHITE)
            text5 = font.render("PLAYER 2",1,r.game.WHITE)

            if score1 == 10:
                screen.blit(text4,(r.game.SCREEN_WIDTH//2 - 120,r.game.SCREEN_HEIGHT//2 - 74))
                screen.blit(text3,(r.game.SCREEN_WIDTH//2 - 75,r.game.SCREEN_HEIGHT//2 - 4))

            else:
                screen.blit(text5,(r.game.SCREEN_WIDTH//2 - 120,r.game.SCREEN_HEIGHT//2 - 74))
                screen.blit(text3,(r.game.SCREEN_WIDTH//2 - 75,r.game.SCREEN_HEIGHT//2 - 4))
        
        pygame.display.flip()

        clock.tick(r.game.FPS)
        
        # if event.type == pygame.KEYDOWN and keys[pygame.K_p]:
        #     while True:
        #         event = pygame.event.wait()
        #         if event.type == pygame.KEYDOWN and keys[pygame.K_p]:
        #             break
        #         if event.type == pygame.QUIT:
        #             exit_window = True
        #             break 
        #         if keys[pygame.K_ESCAPE]:
        #             exit_window = True
        #             break

    pygame.quit()
