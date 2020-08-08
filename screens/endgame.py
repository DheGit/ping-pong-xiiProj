import pygame

from sprites.UIElement import *
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
        self.bg_rgb = bg_rgb

    def setWinnerName(self, winnerName):
        self.winnerName = winnerName

    def showEndScreen(self):
        winner_label = UIElement(
            center_position=(r.game.SCREEN_WIDTH/2, 150), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size=90,
            bg_rgb=self.bg_rgb,
            text_rgb=r.colors.WHITE,
            text=self.winnerName + r.endgame.win_statement,
        )

        play_btn =  UIElement(
            center_position=(r.game.SCREEN_WIDTH/2, 300), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size=45,
            bg_rgb=self.bg_rgb,
            text_rgb=r.colors.WHITE,
            text=r.endgame.play_again_btn_txt,
            action=CB_PLAY
        )

        back_btn = UIElement(
            center_position=(r.game.SCREEN_WIDTH/2, 400), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
            font_size=45,
            bg_rgb=self.bg_rgb,
            text_rgb=r.colors.WHITE,
            text=r.endgame.return_btn_txt,
            action=CB_RETURN
        )
        quit_btn = UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 500),
            font_size = 45,
            bg_rgb = self.bg_rgb,
            text_rgb = r.colors.WHITE,
            text = r.main.r_quit_button_txt,
            action = CB_QUIT,
        )


        winner_label.setHighlightable(False)

        ui_els = [winner_label, play_btn, back_btn, quit_btn]


        while True:
            mouse_up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return CB_QUIT
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True

            self.screen.fill(self.bg_rgb)
            for ui_el in ui_els:
                ui_action=ui_el.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    return ui_action
                ui_el.draw(self.screen)

            keys=pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                return CB_QUIT

            pygame.display.flip()


if __name__=="__main__":
    #Testing
    pygame.init()
    screen=pygame.display.set_mode((r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT))

    egScreen=EndgameScreen(screen, r.colors.BLUE)
    egScreen.setWinnerName("Player 1")

    new_status = egScreen.showEndScreen()

    if new_status == CB_RETURN:
        print("Returning to main menu now")
    if new_status == CB_PLAY:
        print("Restarting game now")
    pygame.quit()
