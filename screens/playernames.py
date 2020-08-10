import pygame

import r
from r.playernames import *
from r.game import *

from sprites.UIElement import *
from sprites.Textbox import *

CB_RETURN = 0
CB_PLAY = 4

class PlayerNamesScreen():
    def __init__(self, screen):
        self.screen = screen
        self.p1name="Player1"
        self.p2name="Player2"
        self.p1color=(0,0,0)
        self.p2color=(0,0,0)

    def names(self):
        Player_Names = UIElement(
            center_position = (SCREEN_WIDTH/2, 50),
            font_size = 80,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = playernames_label_txt,
            action = None,
        )
        Player1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 135),
            font_size = 60,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = p1_label_txt,
            action = None,
        )
        Name1 = UIElement(
            center_position = (80, 205),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = name_label_txt,
            action = None,
        )
        Blue1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 270),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.LIGHTBLUE,
            text = color_blue_label_txt,
            action = None,
        )
        Pink1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 320),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.PINK,
            text = color_pink_label_txt,
            action = None,
        )
        Green1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 370),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.GREEN,
            text = color_green_label_txt,
            action = None,
        )
        Yellow1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 420),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.YELLOW,
            text = color_yellow_label_txt,
            action = None,
        )
        Red1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 470),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.RED,
            text = color_red_label_txt,
            action = None,
        )
        Player2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 135),
            font_size = 60,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = p2_label_txt,
            action = None,
        )
        Name2 = UIElement(
            center_position = (SCREEN_WIDTH/2 + 80, 205),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = name_label_txt,
            action = None,
        )
        Blue2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 270),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.LIGHTBLUE,
            text = color_blue_label_txt,
            action = None,
        )
        Pink2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 320),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.PINK,
            text = color_pink_label_txt,
            action = None,
        )
        Green2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 370),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.GREEN,
            text = color_green_label_txt,
            action = None,
        )
        Yellow2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 420),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.YELLOW,
            text = color_yellow_label_txt,
            action = None,
        )
        Red2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 470),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.RED,
            text = color_red_label_txt,
            action = None,
        )
        enter_btn = UIElement(
            center_position = (SCREEN_WIDTH/2, 550),
            font_size = 50,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = enter_button_txt,
            action = CB_PLAY,
        )
        return_to_mainmenu_btn = UIElement(
            center_position = (r.game.SCREEN_WIDTH/2, 620),
            font_size = 50,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.WHITE,
            text = return_to_mainmenu_button_txt,
            action=CB_RETURN,
        )

        Player_Names.setHighlightable(False)
        Player1.setHighlightable(False)
        Name1.setHighlightable(False)
        Player2.setHighlightable(False)
        Name2.setHighlightable(False)

        buttons = [Player_Names, Player1, Name1, Blue1, Green1, Yellow1, Pink1, Red1, Player2, Name2, Blue2, Green2, Yellow2, Pink2, Red2, enter_btn, return_to_mainmenu_btn]

        P1 = Textbox(180, 190, 200, 30, 31, 13, True)
        P2 = Textbox(SCREEN_WIDTH/2+180, 190, 200, 30, 31, 13, False)

        textboxes = [P1, P2]

        while True:
            mouse_up = False
            events=pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
                
                # for textbox in textboxes:
                #     textbox.handle_event(event)
                    
            self.screen.fill(r.game.BLACK)

            for textbox in textboxes:
                textbox.handle_events(events)
                textbox.draw(self.screen)

            for button in buttons:
                ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if ui_action is not None:
                    
                    if ui_action==CB_PLAY:
                        self.p1name=P1.getText()
                        self.p2name=P2.getText()

                        #Add code here to set the colours according to what is selected
                    
                    return ui_action

                pygame.draw.line(self.screen,r.colors.WHITE,[r.game.SCREEN_WIDTH/2,95],[r.game.SCREEN_WIDTH/2,505],5)

                button.draw(self.screen)

            pygame.display.flip()

    def getPlayer1Name(self):
        return self.p1name
    def getColor1(self):
        return self.color1
    
    def getPlayer2Name(self):
        return self.p2name
    def getColor2(self):
        return self.color2
