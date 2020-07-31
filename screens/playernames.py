import pygame

import r
from r.main import *
from r.colors import *

from sprites.UIElement import *

CB_PLAY = 4

class PlayerNamesScreen():
    
    def __init__(self, screen):
        self.screen = screen

    def player_names(self):
        Player_Names = UIElement(
            center_position = (SCREEN_WIDTH/2, 150),
            font_size = 70,
            bg_rgb = r.colors.BLUE,
            text_rgb = r.colors.WHITE,
            text = r_playernames_label_txt,
            action = None,
        )
        Player1 = UIElement(
            center_position = (300, 300),
            font_size = 35,
            bg_rgb = r.colors.BLUE,
            text_rgb = r.colors.WHITE,
            text = r_p1_name_label_txt,
            action = None,
        )
        Player2 = UIElement(
            center_position = (300, 400),
            font_size = 35,
            bg_rgb = r.colors.BLUE,
            text_rgb = r.colors.WHITE,
            text = r_p2_name_label_txt,
            action = None,
        )
        enter_btn = UIElement(
            center_position = (SCREEN_WIDTH/2, 550),
            font_size = 45,
            bg_rgb = r.colors.BLUE,
            text_rgb = r.colors.WHITE,
            text = r_enter_button_txt,
            action = CB_PLAY,
        )

        Player_Names.setHighlightable(False)
        Player1.setHighlightable(False)
        Player2.setHighlightable(False)

        buttons = [Player_Names, Player1, Player2, enter_btn]

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
