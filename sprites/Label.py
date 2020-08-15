import pygame
import pygame.freetype

class Label():
	def __init__(self,screen,limitRect,fg_color,bg_color,font,text="",lineSpacing=-2):
		self.limitRect=pygame.Rect(limitRect)
		self.screen=screen
		self.fg_color=fg_color
		self.bg_color=bg_color
		self.font=font
		self.text=text
		self.lineSpacing=lineSpacing

	def draw(self):
		y=self.limitRect.top
		fh=self.font.size("Tg")[1]
		temptxt=self.text
		while temptxt:
			i=1

			if y+fh>self.limitRect.bottom:
				break

			while self.font.size(temptxt[:i])[0] < self.limitRect.width and i < len(temptxt):
				i+=1

			if i<len(temptxt):
				i=temptxt.rfind(" ",0,i)+1

			image=self.font.render(temptxt[:i],1,self.fg_color)

			self.screen.blit(image,(self.limitRect.left,y))
			y+=fh+self.lineSpacing

			temptxt=temptxt[i:]
		return temptxt

	def setText(self,text):
		self.text=text

if __name__=="__main__":
	#Testing
	pygame.init()
	screen=pygame.display.set_mode((800,600))
	label=Label(screen,pygame.Rect(0,0,800,300),(255,255,255),(0,0,0),pygame.font.Font(None,40),lineSpacing=0,text="This is a test line just to check how well the said Label class can really perform, so it is made to be senselessly long, to check even the worst case condition for this class.")
	clock=pygame.time.Clock()
	exit_window=False
	while not exit_window:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_window=True

		keys=pygame.key.get_pressed()
		
		if keys[pygame.K_q]:
			break
		
		label.draw()

		pygame.display.flip()
		clock.tick(30)
	pygame.quit()