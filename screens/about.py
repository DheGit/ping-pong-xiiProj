import pygame
import pygame.freetype

from sprites.Label import *

CB_RETURN=0
CB_QUIT=-1

class AboutScreen():
	def __init__(self,screen,abouttext,screen_dimen,bg_color,fg_color,fps,fontsize=30):
		self.screen=screen
		self.screen_dimen=screen_dimen
		self.bg_color=bg_color
		self.fg_color=fg_color
		self.fps=fps

		self.font=pygame.font.Font(None,fontsize)
		self.clock=pygame.time.Clock()

		self.setAboutText(abouttext)

	def showAbout(self):
		exitw=False

		while not exitw:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exitw=True
					return CB_QUIT

			keys=pygame.key.get_pressed()

			if(keys[pygame.K_ESCAPE]):
				return CB_RETURN

			self.screen.fill(self.bg_color)
			self.aboutLabel.draw()

			pygame.display.flip()

			self.clock.tick(30)

	def setAboutText(self,abouttext):
		self.abouttext=abouttext
		self.aboutLabel=Label(self.screen,pygame.Rect(40,40,self.screen_dimen[0]-80,self.screen_dimen[1]-80),self.fg_color,self.bg_color,self.font,text=self.abouttext,lineSpacing=-2)

if __name__=="__main__":
	pygame.init()
	screen=pygame.display.set_mode((800,600))

	abts=AboutScreen(screen,"Test is currently quite successful",(800,600),(0,0,0),(255,255,255),30)
	abts.showAbout()

	pygame.quit()
