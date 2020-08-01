#A dummy file to represent how the screens are going to be organised

#TODO: Add code for endgame here

import pygame

from sprites.UIElement import *
import r

CB_RETURN = 0
CB_PAUSE = 1
CB_ENDGAME = 2
CB_QUIT = -1

class EndgameScreen():

	def __init__(self, screen):
		self.screen=screen
		self.winnerName = ""

	def setWinnerName(self, winnerName):
		self.winnerName = winnerName

	def showEndScreen(self):
		winner_label = UIElement(
	        center_position=(r.game.SCREEN_WIDTH/2, 200), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
	        font_size=30,
	        bg_rgb=r.colors.BLUE,
	        text_rgb=r.colors.WHITE,
	        text=self.winnerName + r.endgame.win_statement,
		)

		winner_label.setHighlightable(False)

		ui_els = [winner_label]


		while True:
			mouse_up = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return CB_QUIT
				if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					mouse_up = True

			self.screen.fill(r.colors.BLUE)
			for ui_el in ui_els:
				ui_action=ui_el.update(pygame.mouse.get_pos(), False) #Change that appropriately
				if ui_action is not None:
					return ui_action
				ui_el.draw(self.screen)

			keys=pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				return CB_QUIT

			pygame.display.flip()


if __name__=="__main__":
	#Testing
	pygame.init()
	screen=pygame.display.set_mode((r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT))

	egScreen=EndgameScreen(screen)
	egScreen.setWinnerName("Player1")

	new_status = egScreen.showEndScreen()

	if new_status == CB_QUIT:
		pygame.quit()
	pygame.quit()