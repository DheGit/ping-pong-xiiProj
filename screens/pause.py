import pygame

import r

from sprites.UIElement import *

CB_PLAY = 4
CB_QUIT = -1

class PauseScreen():
    def __init__(self, screen):
        self.screen = screen

    def pause_game(self):
        self.screen.fill(r.colors.BLACK)
        
        resume_btn = UIElement(
            center_position=(r.game.SCREEN_WIDTH/2, 450), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size=45,
            bg_rgb=r.colors.BLUE,
            text_rgb=r.colors.WHITE,
            text=r.main.r_resume_button_txt,
            action=CB_PLAY,
        )
        quit_btn = UIElement(
            center_position=(r.game.SCREEN_WIDTH/2, 550),
            font_size=45,
            bg_rgb=r.colors.BLUE,
            text_rgb=r.colors.WHITE,
            text=r.main.r_quit_button_txt,
            action=CB_QUIT,
        )

        buttons = [resume_btn, quit_btn]

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

