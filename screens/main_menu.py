import pygame

import r

from sprites.UIElement import *

CB_NAMES = 3
CB_QUIT = -1

class MainMenuScreen():
	def __init__(self, screen):
		self.screen = screen

	def show_menu(self):
	    start_btn = UIElement(
	        center_position=(r.game.SCREEN_WIDTH/2, 450), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
	        font_size=45,
	        bg_rgb=r.colors.BLUE,
	        text_rgb=r.colors.WHITE,
	        text=r.main.r_start_button_txt,
	        action=CB_NAMES,
	    )
	    quit_btn = UIElement(
	        center_position=(r.game.SCREEN_WIDTH/2, 550),
	        font_size=45,
	        bg_rgb=r.colors.BLUE,
	        text_rgb=r.colors.WHITE,
	        text=r.main.r_quit_button_txt,
	        action=CB_QUIT,
	    )
	    game_name = UIElement(
	        center_position=(r.game.SCREEN_WIDTH/2, 220),
	        font_size=135,
	        bg_rgb=r.colors.BLUE,
	        text_rgb=r.colors.WHITE,
	        text=r.main.r_title_label_txt,
	        action=None,
	    )

	    game_name.setHighlightable(False)

	    buttons = [start_btn, quit_btn, game_name]

	    while True:
	        mouse_up = False
	        for event in pygame.event.get():
	            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
	                mouse_up = True
	        self.screen.fill(r.game.BLUE)

	        for button in buttons:
	            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
	            if ui_action is not None:
	                return ui_action
	            button.draw(self.screen)

	        pygame.display.flip()
