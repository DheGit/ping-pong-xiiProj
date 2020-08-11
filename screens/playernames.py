import pygame

import r
from r.playernames import *
from r.game import *

from sprites.UIElement import *
from sprites.Textbox import *

CB_RETURN = 0
CB_PLAY = 4

BLUE1=10
PINK1=11
GREEN1=12
YELLOW1=13
RED1=14
BLUE2=15
PINK2=16
GREEN2=17
YELLOW2=18
RED2=19

CLICKABLE_COLOURS=[BLUE1,PINK1,GREEN1,YELLOW1,RED1,BLUE2,PINK2,GREEN2,YELLOW2,RED2]

class PlayerNamesScreen():
    def __init__(self, screen):
        self.screen = screen
        self.p1name="Player1"
        self.p2name="Player2"
        self.color1=(0,0,0)
        self.color2=(0,0,0)

        # self.Blue1=None
        # self.Pink1=None
        # self.Green1=None
        # self.Yellow1=None
        # self.Red1=None

        # self.Blue2=None
        # self.Pink2=None
        # self.Green2=None
        # self.Yellow2=None
        # self.Red2=None

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
        self.Blue1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 270),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.LIGHTBLUE,
            text = color_blue_label_txt,
            action = BLUE1,
        )
        self.Pink1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 320),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.PINK,
            text = color_pink_label_txt,
            action = PINK1,
        )
        self.Green1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 370),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.GREEN,
            text = color_green_label_txt,
            action = GREEN1,
        )
        self.Yellow1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 420),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.YELLOW,
            text = color_yellow_label_txt,
            action = YELLOW1,
        )
        self.Red1 = UIElement(
            center_position = (SCREEN_WIDTH/4, 470),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.RED,
            text = color_red_label_txt,
            action = RED1,
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
        self.Blue2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 270),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.LIGHTBLUE,
            text = color_blue_label_txt,
            action = BLUE2,
        )
        self.Pink2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 320),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.PINK,
            text = color_pink_label_txt,
            action = PINK2,
        )
        self.Green2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 370),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.GREEN,
            text = color_green_label_txt,
            action = GREEN2,
        )
        self.Yellow2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 420),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.YELLOW,
            text = color_yellow_label_txt,
            action = YELLOW2,
        )
        self.Red2 = UIElement(
            center_position = (3*(SCREEN_WIDTH/4), 470),
            font_size = 40,
            bg_rgb = r.colors.BLACK,
            text_rgb = r.colors.RED,
            text = color_red_label_txt,
            action = RED2,
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

        buttons = [Player_Names, Player1, Name1, self.Blue1, self.Green1, self.Yellow1, self.Pink1, self.Red1, Player2, Name2, self.Blue2, self.Green2, self.Yellow2, self.Pink2, self.Red2, enter_btn, return_to_mainmenu_btn]



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

                    if ui_action in CLICKABLE_COLOURS:
                        self.handleColorClick(ui_action)
                        print("color1: "+str(self.color1)+", color2: "+str(self.color2))
                    else:
                        return ui_action

                pygame.draw.line(self.screen,r.colors.WHITE,[r.game.SCREEN_WIDTH/2,95],[r.game.SCREEN_WIDTH/2,505],5)

                button.draw(self.screen)

            pygame.display.flip()

    def handleColorClick(self, clicked):
        if clicked in CLICKABLE_COLOURS[:5]:
            self.Blue1.stayHighlighted(False)
            self.Pink1.stayHighlighted(False)
            self.Green1.stayHighlighted(False)
            self.Yellow1.stayHighlighted(False)
            self.Red1.stayHighlighted(False)

        elif clicked in CLICKABLE_COLOURS[5:]:
            self.Blue2.stayHighlighted(False)
            self.Pink2.stayHighlighted(False)
            self.Green2.stayHighlighted(False)
            self.Yellow2.stayHighlighted(False)
            self.Red2.stayHighlighted(False)

        if clicked==BLUE1:
            self.Blue1.stayHighlighted(True)
            self.color1=r.colors.LIGHTBLUE
        elif clicked==PINK1:
            self.Pink1.stayHighlighted(True)
            self.color1=r.colors.PINK
        elif clicked==GREEN1:
            self.Green1.stayHighlighted(True)
            self.color1=r.colors.GREEN
        elif clicked==YELLOW1:
            self.Yellow1.stayHighlighted(True)
            self.color1=r.colors.YELLOW
        elif clicked==RED1:
            self.Red1.stayHighlighted(True)
            self.color1=r.colors.RED

        if clicked==BLUE2:
            self.Blue2.stayHighlighted(True)
            self.color2=r.colors.LIGHTBLUE
        elif clicked==PINK2:
            self.Pink2.stayHighlighted(True)
            self.color2=r.colors.PINK
        elif clicked==GREEN2:
            self.Green2.stayHighlighted(True)
            self.color2=r.colors.GREEN
        elif clicked==YELLOW2:
            self.Yellow2.stayHighlighted(True)
            self.color2=r.colors.YELLOW
        elif clicked==RED2:
            self.Red2.stayHighlighted(True)
            self.color2=r.colors.RED


    def getPlayer1Name(self):
        return self.p1name
    def getColor1(self):
        return self.color1
    
    def getPlayer2Name(self):
        return self.p2name
    def getColor2(self):
        return self.color2
