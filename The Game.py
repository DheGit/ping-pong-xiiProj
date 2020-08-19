import pygame

from enum import Enum

import r

import screens

def main():
    global game, main_menu, player_names, pause_screen, endgame_screen, about_screen
    pygame.mixer.pre_init(22050, -16, 1, 512)
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050, -16, 1, 512)
    pygame.display.set_caption(r.main.r_title_label_txt)

    screen = pygame.display.set_mode((r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT))
    game_state = GameScreen.MENU

    game=screens.game.GameScreen(screen, (r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT), r.game.SCORE_MARGIN, r.colors.BLACK, r.game.FPS)
    game.setPaddleMargin(r.game.PADDLE_MARGIN)
    game.setPaddleSpeed(r.game.PADDLE_SPEED)
    game.setBallResetMargin(r.game.BALL_RESET_Y_MARGIN)
    game.setBounceBias(r.game.PADDLE_BOUNCE_BIAS)
    game.setBounceAcceleration(r.game.BALL_BOUNCE_ACC)
    game.setGameObjective(r.game.game_obj_txt)
    game.setMovables(r.game.BALL_HEIGHT, (r.game.PADDLE_WIDTH, r.game.PADDLE_HEIGHT), r.colors.WHITE, r.colors.WHITE)

    main_menu=screens.main_menu.MainMenuScreen(screen)

    player_names=screens.playernames.PlayerNamesScreen(screen)

    pause_screen=screens.pause.PauseScreen(screen)

    endgame_screen=screens.endgame.EndgameScreen(screen, r.colors.BLACK)

    about_screen=screens.about.AboutScreen(screen,r.about.text_about,(r.game.SCREEN_WIDTH, r.game.SCREEN_HEIGHT),r.colors.BLACK,r.colors.WHITE,r.game.FPS,fontsize=r.font_size.s)

    while True:
        if game_state == GameScreen.MENU:
            game_state = start_menu(screen)

        if game_state == GameScreen.PLAYERNAMES:
            game_state = names(screen)

        if game_state == GameScreen.PLAYGAME:
            game_state = start_game(screen, game)

        if game_state == GameScreen.PAUSE:
            game_state = pause_game(screen)
            
        if game_state == GameScreen.ENDGAME:
            game_state = launch_endgame(screen)

        if game_state == GameScreen.ABOUT:
            game_state = launchAbout(screen)

        if game_state == GameScreen.QUIT:
            pygame.quit()
            return

def start_menu(screen):
    new_screen=main_menu.show_menu()

    game.reset()

    if new_screen == screens.main_menu.CB_QUIT:
        return GameScreen.QUIT
    if new_screen == screens.main_menu.CB_NAMES:
        return GameScreen.PLAYERNAMES
    if new_screen == screens.main_menu.CB_ABOUT:
        return GameScreen.ABOUT

    return GameScreen.QUIT

def names(screen):
    new_screen=player_names.names()

    if new_screen == screens.playernames.CB_PLAY:
        game.setPlayer1Name(player_names.getPlayer1Name())
        game.setPlayer2Name(player_names.getPlayer2Name())
        game.setMovables(r.game.BALL_HEIGHT, (r.game.PADDLE_WIDTH, r.game.PADDLE_HEIGHT), player_names.getColor1(), player_names.getColor2())
        return GameScreen.PLAYGAME
    if new_screen == screens.playernames.CB_RETURN:
        return GameScreen.MENU

    return GameScreen.QUIT

def start_game(screen,game):
    new_screen = game.play()

    if new_screen == screens.game.CB_PAUSE:
        return GameScreen.PAUSE
    elif new_screen == screens.game.CB_ENDGAME:
        return GameScreen.ENDGAME
    elif new_screen == screens.game.CB_RETURN:
        return GameScreen.MENU
    elif new_screen == screens.game.CB_QUIT:
        return GameScreen.QUIT
    
    return GameScreen.MENU

def pause_game(screen):
    global game,pause_screen

    pause_screen.setScores(game.getScores())
    new_screen = pause_screen.pause_game()


    if new_screen == screens.pause.CB_QUIT:
        return GameScreen.QUIT
    if new_screen == screens.pause.CB_PLAY:
        return GameScreen.PLAYGAME
    if new_screen == screens.game.CB_RETURN:
        return GameScreen.MENU

    return GameScreen.MENU

def launch_endgame(screen):
    global endgame_screen,game

    endgame_screen.setWinnerName(game.getWinnerName())
    endgame_screen.setWinnerColor(game.getWinnerColor())

    new_screen=endgame_screen.showEndScreen()

    if new_screen==screens.endgame.CB_PLAY:
        return GameScreen.PLAYGAME
    if new_screen==screens.endgame.CB_RETURN:
        return GameScreen.MENU
    if new_screen == screens.pause.CB_QUIT:
        return GameScreen.QUIT

    return GameScreen.MENU

def launchAbout(screen):
    global about_screen

    new_screen=about_screen.showAbout()

    if new_screen==screens.about.CB_RETURN:
        return GameScreen.MENU
    if new_screen==screens.about.CB_QUIT:
        return GameScreen.QUIT

    return GameScreen.MENU


class GameScreen(Enum):
    QUIT=-1
    MENU=0
    PLAYGAME=1
    PAUSE=2
    ENDGAME=3
    PLAYERNAMES=4
    ABOUT=5

if __name__=="__main__":
    main()
