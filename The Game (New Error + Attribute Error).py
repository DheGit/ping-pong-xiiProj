import pygame

from enum import Enum

import r
from sprites.UIElement import *
from game_NewError_and_AttributeError import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.MENU

    while True:
        if game_state == GameState.MENU:
            game_state = show_menu(screen)

        if game_state == GameState.PLAYER_NAMES:
            game_state = player_names(screen)

        if game_state == GameState.PLAYGAME:
            game_state = play_game(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

def show_menu(screen):
    start_btn = UIElement(
        center_position = (SCREEN_WIDTH/2, 450), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
        font_size = 45,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = r_start_button_txt,
        action = GameState.PLAYER_NAMES,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_WIDTH/2, 550),
        font_size=45,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=r_quit_button_txt,
        action = GameState.QUIT,
    )
    Game_Name = UIElement(
        center_position = (SCREEN_WIDTH/2, 220),
        font_size = 135,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = r_title_label_txt,
        action = None,
    )

    Game_Name.setHighlightable(False)

    buttons = [start_btn, quit_btn, Game_Name]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()

def player_names(screen):
    Player_Names = UIElement(
        center_position = (SCREEN_WIDTH/2, 300),
        font_size = 70,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = r_playernames_label_txt,
        action = None,
    )
    Player1 = UIElement(
        center_position = (30, 400),
        font_size = 40,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = r_p1_name_label_txt,
        action = None,
    )
    Player2 = UIElement(
        center_position = (30, 500),
        font_size = 40,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = r_p2_name_label_txt,
        action = None,
    )
    enter_btn = UIElement(
        center_position = (SCREEN_WIDTH/2, 600),
        font_size = 45,
        bg_rgb = BLUE,
        text_rgb = WHITE,
        text = r_start_button_txt,
        action = GameState.PLAYGAME,
    )

    Player_Names.setHighlightable(False)
    Player1.setHighlightable(False)
    Player2.setHighlightable(False)

    buttons = [Player_Names, Player1, Player2, enter_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


class GameState(Enum):
    QUIT=-1
    MENU=0
    PLAYGAME=1
    PAUSE=2
    ENDGAME=3

if __name__=="__main__":
    main()
