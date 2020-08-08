import pygame

import r
from r.main import *
from r.game import *

from sprites.UIElement import *

CB_RETURN = 0
CB_PLAY = 4

class PlayerNamesScreen():
    def __init__(self, screen):
        self.screen = screen

    def names(self):
        Player_Names = UIElement(
            center_position = (SCREEN_WIDTH/2, 50),
            font_size = 80,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_playernames_label_txt,
            action = None,
        )
        Player1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 135),
            font_size = 60,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_p1_label_txt,
            action = None,
        )
        Name1 = UIElement(
            center_position = (80, 205),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_name_label_txt,
            action = None,
        )
        Blue1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 270),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.LIGHTBLUE,
            text = r_color_blue_label_txt,
            action = None,
        )
        Green1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 320),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.GREEN,
            text = r_color_green_label_txt,
            action = None,
        )
        Yellow1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 370),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.YELLOW,
            text = r_color_yellow_label_txt,
            action = None,
        )
        Orange1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 420),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.ORANGE,
            text = r_color_orange_label_txt,
            action = None,
        )
        Red1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 470),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.RED,
            text = r_color_red_label_txt,
            action = None,
        )
        Player2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 135),
            font_size = 60,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_p2_label_txt,
            action = None,
        )
        Name2 = UIElement(
            center_position = (SCREEN_WIDTH/2 + 80, 205),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_name_label_txt,
            action = None,
        )
        Blue2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 270),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.LIGHTBLUE,
            text = r_color_blue_label_txt,
            action = None,
        )
        Green2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 320),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.GREEN,
            text = r_color_green_label_txt,
            action = None,
        )
        Yellow2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 370),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.YELLOW,
            text = r_color_yellow_label_txt,
            action = None,
        )
        Orange2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 420),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.ORANGE,
            text = r_color_orange_label_txt,
            action = None,
        )
        Red2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 470),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.RED,
            text = r_color_red_label_txt,
            action = None,
        )
        enter_btn = UIElement(
            center_position = (SCREEN_WIDTH/2, 550),
            font_size = 45,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_enter_button_txt,
            action = CB_PLAY,
        )
        return_to_mainmenu_btn = UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 620),
            font_size = 45,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.main.r_return_to_mainmenu_button_txt,
            action=CB_RETURN,
        )

        Player_Names.setHighlightable(False)
        Player1.setHighlightable(False)
        Name1.setHighlightable(False)
        Player2.setHighlightable(False)
        Name2.setHighlightable(False)

        buttons = [Player_Names, Player1, Name1, Blue1, Green1, Yellow1, Orange1, Red1, Player2, Name2, Blue2, Green2, Yellow2, Orange2, Red2, enter_btn, return_to_mainmenu_btn]

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(r.game.BLACK)

            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action

                pygame.draw.line(self.screen,r.colors.WHITE,[r.game.SCREEN_WIDTH/2,95],[r.game.SCREEN_WIDTH/2,505],5)

                button.draw(self.screen)

            pygame.display.flip()
