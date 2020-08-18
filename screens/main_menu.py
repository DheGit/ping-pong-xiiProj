import pygame

import r

from sprites.Button import *

CB_NAMES = 3
CB_QUIT = -1
CB_ABOUT = 7

class MainMenuScreen():
    def __init__(self, screen):
        self.screen = screen

    def show_menu(self):
        game_name = Button(
            center_position=(r.game.SCREEN_WIDTH/2, 220),
            font_size=r.font_size.xxxl,
            bg_rgb=r.colors.BLACK,
            text_rgb=r.colors.WHITE,
            text=r.main.r_title_label_txt,
            action=None,
        )
        start_btn = Button(
            center_position=(r.game.SCREEN_WIDTH/2, 430),
            font_size=r.font_size.m,
            bg_rgb=r.colors.BLACK,
            text_rgb=r.colors.WHITE,
            text=r.main.r_start_button_txt,
            action=CB_NAMES,
        )
        about_btn=Button( 
            center_position=(r.game.SCREEN_WIDTH/2, 515),
            font_size=r.font_size.m,
            bg_rgb=r.colors.BLACK,
            text_rgb=r.colors.WHITE,
            text=r.main.r_about_button_txt,
            action=CB_ABOUT,
        )
        quit_btn = Button(
            center_position=(r.game.SCREEN_WIDTH/2, 600),
            font_size=r.font_size.m,
            bg_rgb=r.colors.BLACK,
            text_rgb=r.colors.WHITE,
            text=r.main.r_quit_button_txt,
            action=CB_QUIT,
        )

        game_name.setHighlightable(False)

        buttons = [start_btn, about_btn, quit_btn, game_name]


        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(r.game.BLACK)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                return CB_ABOUT

            for button in buttons:
                button_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if button_action is not None:
                    return button_action
                button.draw(self.screen)

            pygame.display.flip()
