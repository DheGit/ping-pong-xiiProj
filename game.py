import pygame

from r.game import *
from sprites.Paddle import *
from sprites.Ball import *

screen_size = (SCREEN_WIDTH,SCREEN_HEIGHT)

paddle1 = Paddle(screen_size, (PADDLE_WIDTH,PADDLE_HEIGHT), SCORE_MARGIN)
paddle2 = Paddle(screen_size, (PADDLE_WIDTH,PADDLE_HEIGHT), SCORE_MARGIN)
ball = Ball((BALL_WIDTH,BALL_HEIGHT), screen_size, (PADDLE_WIDTH,PADDLE_HEIGHT), SCORE_MARGIN)

score1 = 0
score2 = 0
lastUp1 = FPS
lastUp2 = FPS

def collides():
    if (ball.x <= PADDLE_MARGIN + PADDLE_WIDTH and ball.x >= PADDLE_MARGIN + PADDLE_WIDTH - ball.speed*3) and (ball.y >= paddle1.rect.y and ball.y <=paddle1.rect.y + PADDLE_HEIGHT):
        return 1
    if (ball.x >= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH + PADDLE_WIDTH) and ball.x <= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH + PADDLE_WIDTH) + ball.speed*3)and (ball.y >= paddle2.rect.y and ball.y <=paddle2.rect.y + PADDLE_HEIGHT):
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

def play_game(screen):
    global score1,score2, lastUp1,lastUp2, paddle1,paddle2, ball, screen_size
    pygame.display.set_caption("Ping Pong")

    clock = pygame.time.Clock()

    paddle1.rect.x = PADDLE_MARGIN
    paddle1.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2 + SCORE_MARGIN//2

    paddle2.rect.x = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_MARGIN
    paddle2.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2 + SCORE_MARGIN//2

    ball.setResetMargin(BALL_RESET_Y_MARGIN)
    ball.setBounceBias(PADDLE_BOUNCE_BIAS)
    ball.reset()
    ball.update()

    movingsprites = pygame.sprite.Group()
    movingsprites.add(paddle1)
    movingsprites.add(paddle2)
    movingsprites.add(ball)
    
    exit_window = False
    
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
            ball.x = SCREEN_WIDTH - (PADDLE_MARGIN+BALL_WIDTH+PADDLE_WIDTH+2)
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
            
        if keys[pygame.K_F11]:
            screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        movingsprites.update()

        pygame.draw.line(screen,WHITE,[SCREEN_WIDTH//2,SCORE_MARGIN],[SCREEN_WIDTH//2,SCREEN_HEIGHT],5)

        pygame.draw.line(screen,WHITE,[0,SCORE_MARGIN],[SCREEN_WIDTH,SCORE_MARGIN],5)

        movingsprites.draw(screen)
        
        font = pygame.font.Font(None,74)
        
        text1 = font.render(str(score1),1,WHITE)
        screen.blit(text1,((SCREEN_WIDTH//2)//2,10))
        
        text2 = font.render(str(score2),1,WHITE)
        screen.blit(text2,(3*((SCREEN_WIDTH//2)//2),10))

        if score1 == 10 or score2 == 10:
            screen.fill(BLACK)
            text3 = font.render("WINS",1,WHITE)
            text4 = font.render("PLAYER 1",1,WHITE)
            text5 = font.render("PLAYER 2",1,WHITE)

            if score1 == 10:
                screen.blit(text4,(SCREEN_WIDTH//2 - 120,SCREEN_HEIGHT//2 - 74))
                screen.blit(text3,(SCREEN_WIDTH//2 - 75,SCREEN_HEIGHT//2 - 4))

            else:
                screen.blit(text5,(SCREEN_WIDTH//2 - 120,SCREEN_HEIGHT//2 - 74))
                screen.blit(text3,(SCREEN_WIDTH//2 - 75,SCREEN_HEIGHT//2 - 4))
        
        pygame.display.flip()

        clock.tick(FPS)
        
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
