import pygame

from sprites.Button import *

import r

CB_RETURN = 0
CB_PAUSE = 1
CB_ENDGAME = 2
CB_QUIT = -1
CB_PLAY = 4

class EndgameScreen():

    def __init__(self, screen, bg_rgb):
        self.screen=screen
        self.winnerName = ""
        self.winnerColor = r.colors.WHITE
        self.bg_rgb = bg_rgb
        self.setButtons()

    def setWinnerColor(self, winnerColor):
        self.winnerColor = winnerColor

        self.winner_label = Button(
            center_position=(r.game.SCREEN_WIDTH/2, 100),
            font_size=r.font_size.xxl,
            bg_rgb=self.bg_rgb,
            text_rgb=self.winnerColor,
            text=self.winnerName,
        )
        self.win_label = Button(
            center_position=(r.game.SCREEN_WIDTH/2, 220),
            font_size=r.font_size.xxl,
            bg_rgb=self.bg_rgb,
            text_rgb=self.winnerColor,
            text=r.endgame.win_statement,
        )

    def setWinnerName(self, winnerName):
        self.winnerName = winnerName

        self.winner_label = Button(
            center_position=(r.game.SCREEN_WIDTH/2, 100),
            font_size=r.font_size.xxl,
            bg_rgb=self.bg_rgb,
            text_rgb=self.winnerColor,
            text=self.winnerName,
        )
        self.win_label = Button(
            center_position=(r.game.SCREEN_WIDTH/2, 220),
            font_size=r.font_size.xxl,
            bg_rgb=self.bg_rgb,
            text_rgb=self.winnerColor,
            text=r.endgame.win_statement,
        )

    def showEndScreen(self):
        self.winner_label.setHighlightable(False)
        self.win_label.setHighlightable(False)

        buttons = [self.winner_label, self.win_label, self.play_btn, self.return_to_mainmenu_btn, self.quit_btn]

        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return CB_QUIT
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True

            self.screen.fill(self.bg_rgb)
            for button in buttons:
                button_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if button_action is not None:
                    return button_action
                button.draw(self.screen)

            keys=pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                return CB_QUIT

            pygame.display.flip()

    def setButtons(self):
        self.play_btn =  Button(
            center_position = (r.game.SCREEN_WIDTH/2, 370),
            font_size = r.font_size.m,
            bg_rgb = self.bg_rgb,
            text_rgb = r.colors.WHITE,
            text = r.endgame.play_again_btn_txt,
            action = CB_PLAY
        )
        self.return_to_mainmenu_btn = Button(
            center_position = (r.game.SCREEN_WIDTH/2, 470), 
            font_size = r.font_size.m,
            bg_rgb = self.bg_rgb,
            text_rgb = r.colors.WHITE,
            text = r.endgame.return_to_mainmenu_button_txt,
            action = CB_RETURN
        )
        self.quit_btn = Button(
            center_position = (r.game.SCREEN_WIDTH/2, 570),
            font_size = r.font_size.m,
            bg_rgb = self.bg_rgb,
            text_rgb = r.colors.WHITE,
            text = r.endgame.quit_button_txt,
            action = CB_QUIT,
        )
