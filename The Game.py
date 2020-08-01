import pygame

from enum import Enum

from sprites.UIElement import *
import r

import screens

def main():
    global game, main_menu, pauseScreen
    pygame.init()

    screen = pygame.display.set_mode((r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT))
    game_state = GameState.MENU

    game=screens.game.GameScreen(screen, (r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT), r.game.SCORE_MARGIN, r.colors.BLACK, r.game.FPS)
    game.setMovables(r.game.BALL_HEIGHT,(r.game.PADDLE_WIDTH, r.game.PADDLE_HEIGHT), r.colors.WHITE)
    game.setPaddleMargin(r.game.PADDLE_MARGIN)
    game.setPaddleSpeed(r.game.PADDLE_SPEED)
    game.setBallResetMargin(r.game.BALL_RESET_Y_MARGIN)
    game.setBounceBias(r.game.PADDLE_BOUNCE_BIAS)


    main_menu=screens.main_menu.MainMenuScreen(screen)

    pauseScreen=screens.pause.PauseScreen(screen)

    while True:
        if game_state == GameState.MENU:
            game_state = start_menu(screen)

        if game_state == GameState.PLAYGAME:
            game_state = start_game(screen, game)

        if game_state == GameState.PAUSE:
            game_state = pause_game(screen) #TODO: Invoke the respective function call here

        if game_state == GameState.ENDGAME:
            print("Endgame GameState")
            game_state = GameState.MENU  #TODO: Invoke the respective function call here

        if game_state == GameState.QUIT:
            pygame.quit()
            return

def start_menu(screen):
    new_state=main_menu.show_menu()

    if new_state == screens.main_menu.CB_QUIT:
        return GameState.QUIT
    if new_state == screens.main_menu.CB_PLAY:
        return GameState.PLAYGAME

    return GameState.QUIT

def start_game(screen,game):
    global game_state
    new_state = game.play()

    if new_state == screens.game.CB_PAUSE:
        return GameState.PAUSE
    elif new_state == screens.game.CB_ENDGAME:
        return GameState.ENDGAME
    elif new_state == screens.game.CB_RETURN:
        return GameState.MENU
    elif new_state == screens.game.CB_QUIT:
        return GameState.QUIT
    return GameState.MENU

def pause_game(screen):
    new_state = pauseScreen.pause_game()

    if new_state == screens.pause.CB_QUIT:
        return GameState.QUIT
    if new_state == screens.pause.CB_PLAY:
        return GameState.PLAYGAME

    return GameState.QUIT

class GameState(Enum):
    QUIT=-1
    MENU=0
    PLAYGAME=1
    PAUSE=2
    ENDGAME=3

if __name__=="__main__":
    main()
