import pygame

import r

from sprites.UIElement import *

CB_RETURN = 0
CB_PLAY = 4
CB_QUIT = -1

class PauseScreen():
    def __init__(self, screen):
        self.screen = screen
        self.scores=(0,0)
        
    def pause_game(self):
        score_label=UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 250), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size = 45,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = str(self.scores[0])+" : "+str(self.scores[1]),
            action = None,
        )
        paused = UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 150), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size = 90,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.main.r_paused_button_txt,
            action = None,
        )
        resume_btn = UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 350), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size = 45,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.main.r_resume_button_txt,
            action=CB_PLAY,
        )
        return_to_mainmenu_btn = UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 450), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size = 45,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.main.r_return_to_mainmenu_button_txt,
            action=CB_RETURN,
        )
        quit_btn = UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 550),
            font_size = 45,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.main.r_quit_button_txt,
            action = CB_QUIT,
        )

        buttons = [score_label, paused, resume_btn, quit_btn, return_to_mainmenu_btn]

        paused.setHighlightable(False)
        score_label.setHighlightable(False)

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

    def setScores(self,a):
        self.scores=a