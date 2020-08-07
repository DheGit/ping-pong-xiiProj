import pygame

from enum import Enum

from sprites.UIElement import *
import r

import screens

def main():
    global game, main_menu, pause_screen, endgame_screen
    pygame.init()
    pygame.display.set_caption(r.main.r_title_label_txt)

    screen = pygame.display.set_mode((r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT))
    game_state = GameState.MENU

    game=screens.game.GameScreen(screen, (r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT), r.game.SCORE_MARGIN, r.colors.BLACK, r.game.FPS)
    game.setPaddleMargin(r.game.PADDLE_MARGIN)
    game.setPaddleSpeed(r.game.PADDLE_SPEED)
    game.setBallResetMargin(r.game.BALL_RESET_Y_MARGIN)
    game.setBounceBias(r.game.PADDLE_BOUNCE_BIAS)
    game.setBounceAcceleration(r.game.BALL_BOUNCE_ACC)
    game.setGameObjective(r.game.game_obj_txt)
    game.setMovables(r.game.BALL_HEIGHT,(r.game.PADDLE_WIDTH, r.game.PADDLE_HEIGHT), r.colors.WHITE)

    main_menu=screens.main_menu.MainMenuScreen(screen)

    pause_screen=screens.pause.PauseScreen(screen)

    endgame_screen=screens.endgame.EndgameScreen(screen, r.colors.BLACK)

    while True:
        if game_state == GameState.MENU:
            game_state = start_menu(screen)

        if game_state == GameState.PLAYGAME:
            game_state = start_game(screen, game)

        if game_state == GameState.PAUSE:
            game_state = pause_game(screen)
            
        if game_state == GameState.ENDGAME:
            game_state = launch_endgame(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

def start_menu(screen):
    new_state=main_menu.show_menu()

    game.reset()

    if new_state == screens.main_menu.CB_QUIT:
        return GameState.QUIT
    if new_state == screens.main_menu.CB_PLAY:
        return GameState.PLAYGAME

    return GameState.QUIT

def start_game(screen,game):
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
    new_state = pause_screen.pause_game()

    global game

    if new_state == screens.pause.CB_QUIT:
        return GameState.QUIT
    if new_state == screens.pause.CB_PLAY:
        return GameState.PLAYGAME
    if new_state == screens.game.CB_RETURN:
        return GameState.MENU

    return GameState.MENU

def launch_endgame(screen):
    endgame_screen.setWinnerName(game.getWinnerName())

    new_state=endgame_screen.showEndScreen()

    if new_state==screens.endgame.CB_PLAY:
        return GameState.PLAYGAME
    if new_state==screens.endgame.CB_RETURN:
        return GameState.MENU
    if new_state == screens.pause.CB_QUIT:
        return GameState.QUIT

    return GameState.MENU

class GameState(Enum):
    QUIT=-1
    MENU=0
    PLAYGAME=1
    PAUSE=2
    ENDGAME=3

if __name__=="__main__":
    main()
