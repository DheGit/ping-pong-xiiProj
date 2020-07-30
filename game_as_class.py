import pygame
import pygame.freetype

from sprites.Paddle import *
from sprites.Ball import *

from r import colors

CB_RETURN = 0
CB_PAUSE = 1
CB_ENDGAME = 2
CB_QUIT = 3

"""
A class enclosing the game logic. All dimens are tuples (width,height)
"""
class Game():

	def __init__(self, screen, screen_dimen, score_margin, bg_color, fps):
		self.screen=screen
		self.score_margin=score_margin
		self.screen_dimen=screen_dimen
		self.bg_color=bg_color

		self.reset()

		self.fps=fps

	def reset(self):
		self.lastUp1=0
		self.lastUp2=0
		self.score1=0
		self.score2=0


	def setMovables(self, ball_radius, paddle_dimen, color):
		self.paddle_dimen=paddle_dimen
		self.ball_dimen=(ball_radius,ball_radius)

		self.ball=Ball(self.ball_dimen, self.screen_dimen, self.paddle_dimen, self.score_margin)
		self.ball_group=pygame.sprite.Group()
		self.ball_group.add(self.ball)

		self.paddle1=Paddle(self.screen_dimen, self.paddle_dimen, self.score_margin)
		self.paddle2=Paddle(self.screen_dimen, self.paddle_dimen, self.score_margin)

	def setPaddleMargin(self, paddle_margin):
		self.paddle_margin=paddle_margin

	def setPaddleSpeed(self, paddle_speed):
		self.paddle_speed=paddle_speed

	def setBallResetMargin(self, ball_reset_margin):
		self.ball_reset_margin=ball_reset_margin

	def setBounceBias(self, bounce_bias):
		self.bounce_bias=bounce_bias

	def collides(self):
	    if (self.ball.x <= self.paddle1.rect.x + self.paddle_dimen[0] and self.ball.x >= self.paddle1.rect.x + self.paddle_dimen[0] - self.ball.speed*3) and (self.ball.y >= self.paddle1.rect.y and self.ball.y <=self.paddle1.rect.y + self.paddle_dimen[1]):
	        return 1
	    if (self.ball.x >= self.paddle2.rect.x - self.ball.ball_dimen[0] and self.ball.x <= self.paddle2.rect.x - self.ball.ball_dimen[0] + self.ball.speed*3)and (self.ball.y >= self.paddle2.rect.y and self.ball.y <=self.paddle2.rect.y + self.paddle_dimen[1]):
	        return 2
	    return 0

	def play(self):
	    clock = pygame.time.Clock()

	    self.paddle1.rect.x = self.paddle_margin
	    self.paddle1.rect.y = self.screen_dimen[1]//2 - self.paddle_dimen[1]//2 + self.score_margin//2

	    self.paddle2.rect.x = self.screen_dimen[0] - self.paddle_dimen[0] - self.paddle_margin
	    self.paddle2.rect.y = self.screen_dimen[1]//2 - self.paddle_dimen[1]//2 + self.score_margin//2

	    self.ball.setResetMargin(self.ball_reset_margin)
	    self.ball.setBounceBias(self.bounce_bias)
	    self.ball.reset()
	    self.ball.update()

	    movingsprites = pygame.sprite.Group()
	    movingsprites.add(self.paddle1)
	    movingsprites.add(self.paddle2)
	    movingsprites.add(self.ball)
	    
	    exit_window = False
	    
	    while not exit_window:

	        self.screen.fill(self.bg_color)
	        
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	            	exit_window = True
	            	return CB_QUIT
	            
	        if self.ball.x > self.paddle_margin + self.paddle_dimen[0] and self.ball.x < self.screen_dimen[0] - (self.paddle_margin + self.paddle_dimen[0]):
	            self.lastUp1 += 1
	            self.lastUp2 += 1
	        self.ball.update()
	        
	        if self.collides() == 1:
	            diff = (self.paddle1.rect.y + self.paddle_dimen[1]/2) - (self.ball.rect.y+self.ball_dimen[1]/2)
	            self.ball.x = self.paddle_margin+self.paddle_dimen[0] + 2
	            self.ball.bounce(diff)
	            # updateScore(1)
	            self.score1+=1

	        if self.collides() == 2:
	            diff = (self.paddle2.rect.y + self.paddle_dimen[1]/2) - (self.ball.rect.y+self.ball_dimen[1]/2) 
	            self.ball.x = self.screen_dimen[0] - (self.paddle_margin+self.ball_dimen[0]+self.paddle_dimen[0]+2)
	            self.ball.bounce(-diff)
	            # updateScore(2)
	            self.score2+=1

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

	        movingsprites.update()

	        pygame.draw.line(self.screen,colors.WHITE,[self.screen_dimen[0]//2,self.score_margin],[self.screen_dimen[0]//2,self.screen_dimen[1]],5)

	        pygame.draw.line(self.screen,colors.WHITE,[0,self.score_margin],[self.screen_dimen[0],self.score_margin],5)

	        movingsprites.draw(self.screen)
	        
	        font = pygame.font.Font(None,74)
	        
	        text1 = font.render(str(self.score1),1,colors.WHITE)
	        self.screen.blit(text1,(int(self.screen_dimen[0]/4),10))
	        
	        text2 = font.render(str(self.score2),1,colors.WHITE)
	        self.screen.blit(text2,(3*int(self.screen_dimen[0]/4),10))

	        # if self.score1 == 10 or self.score2 == 10:
	        #     self.screen.fill(colors.BLACK)
	        #     text3 = font.render("WINS",1,colors.WHITE)
	        #     text4 = font.render("PLAYER 1",1,colors.WHITE)
	        #     text5 = font.render("PLAYER 2",1,colors.WHITE)

	        #     if self.score1 == 10:
	        #         self.screen.blit(text4,(self.screen_dimen[0]//2 - 120,self.screen_dimen[1]//2 - 74))
	        #         self.screen.blit(text3,(self.screen_dimen[0]//2 - 75,self.screen_dimen[1]//2 - 4))

	        #     else:
	        #         self.screen.blit(text5,(self.screen_dimen[0]//2 - 120,self.screen_dimen[1]//2 - 74))
	        #         self.screen.blit(text3,(self.screen_dimen[0]//2 - 75,self.screen_dimen[1]//2 - 4))

	        if self.score1 == 10 or self.score2 == 10:
	        	self.reset()
	        	return CB_ENDGAME

	       	if keys[pygame.K_p]:
	       		return CB_PAUSE

	        pygame.display.flip()

	        clock.tick(self.fps)