import pygame

import r
from r.main import *
from r.game import *

from sprites.UIElement import *

CB_PLAY = 4

class PlayerNamesScreen():
    def __init__(self, screen):
        self.screen = screen

    def names(self):
        Player_Names = UIElement(
            center_position = (SCREEN_WIDTH/2, 50),
            font_size = 70,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_playernames_label_txt,
            action = None,
        )
        Player1 = UIElement(
            center_position = (300, 120),
            font_size = 35,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_p1_name_label_txt,
            action = None,
        )
        Color1 = UIElement(
            center_position = (458, 170),
            font_size = 35,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_color_label_txt,
            action = None,
        )
        Player2 = UIElement(
            center_position = (300, 270),
            font_size = 35,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_p2_name_label_txt,
            action = None,
        )
        Color2 = UIElement(
            center_position = (458, 320),
            font_size = 35,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_color_label_txt,
            action = None,
        )
        Color_List = UIElement(
            center_position = (196, 395),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_color_list_label_txt,
            action = None,
        )
        Color_Blue = UIElement(
            center_position = (500, 395),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.LIGHTBLUE,
            text = r_color_blue_label_txt,
            action = None,
        )
        Color_Green = UIElement(
            center_position = (512, 430),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.GREEN,
            text = r_color_green_label_txt,
            action = None,
        )
        Color_Yellow = UIElement(
            center_position = (523, 465),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.YELLOW,
            text = r_color_yellow_label_txt,
            action = None,
        )
        Color_Orange = UIElement(
            center_position = (523, 500),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.ORANGE,
            text = r_color_orange_label_txt,
            action = None,
        )
        Color_Red = UIElement(
            center_position = (487, 535),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.RED,
            text = r_color_red_label_txt,
            action = None,
        )
        enter_btn = UIElement(
            center_position = (SCREEN_WIDTH/2, 620),
            font_size = 55,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r_enter_button_txt,
            action = CB_PLAY,
        )

        Player_Names.setHighlightable(False)
        Player1.setHighlightable(False)
        Color1.setHighlightable(False)
        Player2.setHighlightable(False)
        Color2.setHighlightable(False)
        Color_List.setHighlightable(False)
        Color_Blue.setHighlightable(False)
        Color_Green.setHighlightable(False)
        Color_Yellow.setHighlightable(False)
        Color_Orange.setHighlightable(False)
        Color_Red.setHighlightable(False)

        buttons = [Player_Names, Player1, Color1, Player2, Color2, Color_List, Color_Blue, Color_Green, Color_Yellow, Color_Orange, Color_Red, enter_btn]

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
                button.draw(self.screen)

            pygame.display.flip()
