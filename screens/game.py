import pygame
import pygame.freetype

from sprites.Paddle import *
from sprites.Ball import *
from sprites.UIElement import *

from r.main import *
from r.game import *

from r import colors

CB_RETURN = 0
CB_PAUSE = 1
CB_ENDGAME = 2
CB_QUIT = -1

fg_color_default=(255,255,255)

"""
A class enclosing the game logic. All dimens are tuples (width,height)
"""
class GameScreen():
    def __init__(self, screen, screen_dimen, score_margin, bg_color, fps):
        self.screen=screen
        self.score_margin=score_margin
        self.screen_dimen=screen_dimen
        self.bg_color=bg_color

        self.fps=fps

        self.p1Name="Player1"
        self.p2Name="Player2"

        self.winnerName="TheHulk" # :P

        self.game_obj = ""

        self.bounce_acceleration = 1

    def reset(self):
        self.score1=0
        self.score2=0

        self.paddle1.rect.x = self.paddle_margin
        self.paddle1.rect.y = self.screen_dimen[1]//2 - self.paddle_dimen[1]//2 + self.score_margin//2

        self.paddle2.rect.x = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_MARGIN
        self.paddle2.rect.y = self.screen_dimen[1]//2 - self.paddle_dimen[1]//2 + self.score_margin//2

        self.ball.reset()

    def collides(self):
        if (self.ball.x <= self.paddle1.rect.x + self.paddle_dimen[0] and self.ball.x >= self.paddle1.rect.x + self.paddle_dimen[0] - self.ball.speed*3) and (self.ball.y + self.ball_dimen[1] >= self.paddle1.rect.y and self.ball.y <=self.paddle1.rect.y + self.paddle_dimen[1]):
            return 1
        if (self.ball.x >= self.paddle2.rect.x - self.ball.ball_dimen[0] and self.ball.x <= self.paddle2.rect.x - self.ball.ball_dimen[0] + self.ball.speed*3) and (self.ball.y + self.ball_dimen[1] >= self.paddle2.rect.y and self.ball.y <=self.paddle2.rect.y + self.paddle_dimen[1]):
            return 2
        return 0

    def play(self):
        clock = pygame.time.Clock()

        self.ball.setResetMargin(self.ball_reset_margin)
        self.ball.setBounceBias(self.bounce_bias)
        self.ball.update()

        movingsprites = pygame.sprite.Group()
        movingsprites.add(self.paddle1)
        movingsprites.add(self.paddle2)
        movingsprites.add(self.ball)

        self.countdown()
        
        exit_window = False
        
        while not exit_window:

            self.screen.fill(self.bg_color)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_window = True
                    return CB_QUIT

            self.ball.update()
            
            if self.collides() == 1:
                diff = (self.paddle1.rect.y + self.paddle_dimen[1]/2) - (self.ball.rect.y+self.ball_dimen[1]/2)
                self.ball.x = self.paddle_margin+self.paddle_dimen[0] + 2
                self.ball.bounce(diff)
                self.ball.speed = self.ball.speed*self.bounce_acceleration
                
            if self.collides() == 2:
                diff = (self.paddle2.rect.y + self.paddle_dimen[1]/2) - (self.ball.rect.y+self.ball_dimen[1]/2) 
                self.ball.x = self.screen_dimen[0] - (self.paddle_margin+self.ball_dimen[0]+self.paddle_dimen[0]+2)
                self.ball.bounce(-diff)
                self.ball.speed = self.ball.speed*self.bounce_acceleration

            if self.ball.crossed(self.paddle_margin):
                self.score2+=1
            if self.ball.crossed(self.screen_dimen[0]-self.paddle_margin):
                self.score1+=1

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_w]:
                self.paddle1.moveUp(self.paddle_speed)
            if keys[pygame.K_s]:
                self.paddle1.moveDown(self.paddle_speed)
            if keys[pygame.K_UP]:
                self.paddle2.moveUp(self.paddle_speed)
            if keys[pygame.K_DOWN]:
                self.paddle2.moveDown(self.paddle_speed)

            if keys[pygame.K_ESCAPE]:
                exit_window = True
                self.reset()
                return CB_RETURN
                
            if keys[pygame.K_F11]:
                self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

            if keys[pygame.K_p]:
                return CB_PAUSE

            movingsprites.update()

            pygame.draw.line(self.screen,colors.WHITE,[self.screen_dimen[0]//2,self.score_margin],[self.screen_dimen[0]//2,self.screen_dimen[1]],5)

            pygame.draw.line(self.screen,colors.WHITE,[0,self.score_margin],[self.screen_dimen[0],self.score_margin],5)

            movingsprites.draw(self.screen)

            if self.score1 == 10 or self.score2 == 10:
                if self.score1==10:
                    self.winnerName=self.p1Name
                if self.score2==10:
                    self.winnerName=self.p2Name
                    
                self.reset()
                                
                return CB_ENDGAME

            pygame.display.flip()

            clock.tick(self.fps)

            self.display()

    def countdown(self):
        clock=pygame.time.Clock()
        three=UIElement(
            center_position=(self.screen_dimen[0]//2,self.screen_dimen[1]//2),
            text="3",
            font_size=200,
            bg_rgb=self.bg_color,
            text_rgb=fg_color_default)

        two=UIElement(
            center_position=(self.screen_dimen[0]//2,self.screen_dimen[1]//2),
            text="2",
            font_size=200,
            bg_rgb=self.bg_color,
            text_rgb=fg_color_default)

        one=UIElement(
            center_position=(self.screen_dimen[0]//2,self.screen_dimen[1]//2),
            text="1",
            font_size=200,
            bg_rgb=self.bg_color,
            text_rgb=fg_color_default)

        go=UIElement(
            center_position=(self.screen_dimen[0]//2,self.screen_dimen[1]//2),
            text="GO!",
            font_size=200,
            bg_rgb=self.bg_color,
            text_rgb=fg_color_default)

        game_objective=UIElement(
            center_position=(self.screen_dimen[0]//2,self.screen_dimen[1]//2+200),
            text=self.game_obj,
            font_size=100,
            bg_rgb=self.bg_color,
            text_rgb=fg_color_default)

        for i in range(1,self.fps*4+1):
            self.screen.fill(self.bg_color)

            game_objective.draw(self.screen)
            num=4-i//self.fps
            if num==1:
                go.draw(self.screen)
            elif num==2:
                one.draw(self.screen)
            elif num==3:
                two.draw(self.screen)
            elif num==4:
                three.draw(self.screen)

            pygame.display.flip()
            
            clock.tick(self.fps)

    def display(self):
        Score1=UIElement(
            center_position=(self.screen_dimen[0]/4,self.score_margin/2),
            font_size=70,
            bg_rgb=colors.BLACK,
            text_rgb=colors.WHITE,
            text=str(self.score1),
            action=None
        )

        Score2=UIElement(
            center_position=(3*(self.screen_dimen[0]/4),self.score_margin/2),
            font_size=70,
            bg_rgb=colors.BLACK,
            text_rgb=colors.WHITE,
            text=str(self.score2),
            action=None
        )

        Pause_btn=UIElement(
            center_position=(self.screen_dimen[0]/2,self.score_margin/2),
            font_size=32,
            bg_rgb=colors.BLACK,
            text_rgb=colors.WHITE,
            text=r_pause_button,
            action=CB_PAUSE
        )

        Score1.setHighlightable(False)
        Score2.setHighlightable(False)

        buttons = [Score1, Score2, Pause_btn]

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(colors.BLACK)

            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action

                pygame.draw.circle(self.screen,colors.WHITE,[self.screen_dimen[0]//2,self.score_margin//2],30)
                pygame.draw.circle(self.screen,colors.BLACK,[self.screen_dimen[0]//2,self.score_margin//2],28)
                
                button.draw(self.screen)

            pygame.display.flip()
        

    def setGameObjective(self, game_obj):
        self.game_obj=game_obj

    def setMovables(self, ball_radius, paddle_dimen, color):
        self.paddle_dimen=paddle_dimen
        self.ball_dimen=(ball_radius,ball_radius)

        self.ball=Ball(self.ball_dimen, self.screen_dimen, self.paddle_dimen, self.score_margin)
        self.ball_group=pygame.sprite.Group()
        self.ball_group.add(self.ball)

        self.paddle1=Paddle(self.screen_dimen, self.paddle_dimen, self.score_margin)
        self.paddle2=Paddle(self.screen_dimen, self.paddle_dimen, self.score_margin)

        self.reset()

    def setPaddleMargin(self, paddle_margin):
        self.paddle_margin=paddle_margin

    def setPaddleSpeed(self, paddle_speed):
        self.paddle_speed=paddle_speed

    def setBallResetMargin(self, ball_reset_margin):
        self.ball_reset_margin=ball_reset_margin

    def setBounceBias(self, bounce_bias):
        self.bounce_bias=bounce_bias

    def setPlayer1Name(self, p1Name):
        self.p1Name=p1Name

    def setPlayer1Name(self, p1Name):
        self.p2Name=p2Name

    def setBounceAcceleration(self, bounce_acceleration):
        self.bounce_acceleration = bounce_acceleration

    def getWinnerName(self):
        return self.winnerName

    def getScores(self):
        return (self.score1,self.score2)
