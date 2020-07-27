import pygame

from enum import Enum

from res.UIElement import *
from res.rgame import *
from res.rmain import *
from game import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.MENU

    while True:
        if game_state == GameState.MENU:
            game_state = show_menu(screen)

        if game_state == GameState.PLAYGAME:
            game_state = play_game(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

def show_menu(screen):
    start_btn = UIElement(
        center_position=(SCREEN_WIDTH/2, 450), #TODO: Change these hardcoded values into variables, including margin, etc, to make the positioning more comfortable and dynamic 
        font_size=45,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=r_start_button_txt,
        action=GameState.PLAYGAME,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_WIDTH/2, 550),
        font_size=45,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=r_quit_button_txt,
        action=GameState.QUIT,
    )
    game_name = UIElement(
        center_position=(SCREEN_WIDTH/2, 220),
        font_size=135,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text=r_title_label_txt,
        action=None,
    )

    game_name.setHighlightable(False)

    buttons = [start_btn, quit_btn, game_name]

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
