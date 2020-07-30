import pygame

from enum import Enum

from sprites.UIElement import *
import r
from game import *

import game_as_class

def main():
    pygame.init()

    screen = pygame.display.set_mode((r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT))
    game_state = GameState.MENU

    game=game_as_class.Game(screen, (r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT), r.game.SCORE_MARGIN, r.colors.BLACK, r.game.FPS)
    game.setMovables(r.game.BALL_HEIGHT,(r.game.PADDLE_WIDTH, r.game.PADDLE_HEIGHT), r.colors.WHITE)
    game.setPaddleMargin(r.game.PADDLE_MARGIN)
    game.setPaddleSpeed(r.game.PADDLE_SPEED)
    game.setBallResetMargin(r.game.BALL_RESET_Y_MARGIN)
    game.setBounceBias(r.game.PADDLE_BOUNCE_BIAS)

    while True:
        if game_state == GameState.MENU:
            game_state = show_menu(screen)

        if game_state == GameState.PLAYGAME:
            # game_state = play_game(screen)
            start_game_aliter(screen, game)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

def show_menu(screen):
    start_btn = UIElement(
        center_position=(r.game.SCREEN_WIDTH/2, 450), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
        font_size=45,
        bg_rgb=r.game.BLUE,
        text_rgb=r.game.WHITE,
        text=r.main.r_start_button_txt,
        action=GameState.PLAYGAME,
    )
    quit_btn = UIElement(
        center_position=(r.game.SCREEN_WIDTH/2, 550),
        font_size=45,
        bg_rgb=r.game.BLUE,
        text_rgb=r.game.WHITE,
        text=r.main.r_quit_button_txt,
        action=GameState.QUIT,
    )
    game_name = UIElement(
        center_position=(r.game.SCREEN_WIDTH/2, 220),
        font_size=135,
        bg_rgb=r.game.BLUE,
        text_rgb=r.game.WHITE,
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
        screen.fill(r.game.BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()

def start_game_aliter(screen,game):
    game.play()
    game_state=GameState.MENU

class GameState(Enum):
    QUIT=-1
    MENU=0
    PLAYGAME=1
    PAUSE=2
    ENDGAME=3

if __name__=="__main__":
    main()
