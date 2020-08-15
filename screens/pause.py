import pygame

import r

from sprites.Button import *

CB_RETURN = 0
CB_PLAY = 4
CB_QUIT = -1

class PauseScreen():
    def __init__(self, screen):
        self.screen = screen
        self.scores=(0,0)
        self.setButtons()
        
    def pause_game(self):
        buttons = [self.score_label, self.paused, self.resume_btn, self.quit_btn, self.return_to_mainmenu_btn]

        self.paused.setHighlightable(False)
        self.score_label.setHighlightable(False)

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            self.screen.fill(r.game.BLACK)

            for button in buttons:
                button_action = button.update(pygame.mouse.get_pos(), mouse_up)                    
                if button_action is not None:
                    return button_action
                button.draw(self.screen)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    return CB_PLAY

            pygame.display.flip()

    def setButtons(self):
        self.paused = Button(
            center_position = (r.game.SCREEN_WIDTH/2, 125),
            font_size = r.font_size.xxl,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.pause.paused_label_txt,
            action = None,
        )
        self.score_label=Button(
            center_position = (r.game.SCREEN_WIDTH/2, 285),
            font_size = r.font_size.m,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = str(self.scores[0])+" : "+str(self.scores[1]),
            action = None,
        )
        self.resume_btn = Button(
            center_position = (r.game.SCREEN_WIDTH/2, 385),
            font_size = r.font_size.m,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.pause.resume_button_txt,
            action=CB_PLAY,
        )
        self.return_to_mainmenu_btn = Button(
            center_position = (r.game.SCREEN_WIDTH/2, 485),
            font_size = r.font_size.m,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.pause.return_to_mainmenu_button_txt,
            action=CB_RETURN,
        )
        self.quit_btn = Button(
            center_position = (r.game.SCREEN_WIDTH/2, 585),
            font_size = r.font_size.m,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = r.pause.quit_button_txt,
            action = CB_QUIT,
        )

    def setScores(self,a):
        self.scores=a
        self.score_label=Button(
            center_position = (r.game.SCREEN_WIDTH/2, 285),
            font_size = r.font_size.m,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = str(self.scores[0])+" : "+str(self.scores[1]),
            action = None,
        )
