#A dummy file to represent how the screens are going to be organised

#TODO: Add code for endgame here

import pygame

from sprites.UIElement import *
import r

class EndgameScreen():

	def __init__(self, screen):
		self.screen=screen
		self.winnerName = ""

	def setWinnerName(self, winnerName):
		self.winnerName = winnerName

	def showEndScreen(self):
		winner_label = UIElement(
	        center_position=(r.game.SCREEN_WIDTH/2, 450), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
	        font_size=30,
	        bg_rgb=r.colors.BLACK,
	        text_rgb=r.colors.WHITE,
	        text=self.winnerName + r.endgame.win_statement,
		)

		winner_label.setHighlightable(False)

		ui_els = [winner_label]

		while True:
			for ui_el in ui_els:
				ui_action=ui_el.update(pygame.mouse.get_pos(), False) #Change that appropriately
				if ui_action is not None:
					return ui_action
				ui_el.draw(self.screen)

if __name__=="__main__":
	pygame.init()
	screen=pygame.display.set_mode((r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT))

	egScreen=EndgameScreen(screen)
	egScreen.setWinnerName("Dheer The Banker")

	egScreen.showEndScreen()