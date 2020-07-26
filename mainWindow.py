import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from res.rgame import *
from res.Paddle import *
from res.Ball import *

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

screen_size = (SCREEN_WIDTH,SCREEN_HEIGHT)

paddle1 = Paddle(screen_size, (PADDLE_WIDTH,PADDLE_HEIGHT),SCORE_MARGIN)
paddle2 = Paddle(screen_size, (PADDLE_WIDTH,PADDLE_HEIGHT),SCORE_MARGIN)
ball = Ball((BALL_WIDTH,BALL_HEIGHT),screen_size,(PADDLE_WIDTH,PADDLE_HEIGHT), SCORE_MARGIN)

score1 = 0
score2 = 0
lastUp1 = FPS
lastUp2 = FPS


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb)

        highlighted_image = create_surface_with_text(text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb)

        self.images = [default_image, highlighted_image]

        self.rects = [default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

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
        center_position=(450, 450),
        font_size=45,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.PLAYGAME,
    )
    quit_btn = UIElement(
        center_position=(450, 550),
        font_size=45,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    game_name = UIElement(
        center_position=(450, 220),
        font_size=135,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="PING PONG",
        action=None,
    )

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

def collides():
    if (ball.x <= PADDLE_MARGIN + PADDLE_WIDTH and ball.x >= PADDLE_MARGIN + PADDLE_WIDTH - ball.speed*3) and (ball.y >= paddle1.rect.y and ball.y <=paddle1.rect.y + PADDLE_HEIGHT):
        return 1
    if (ball.x >= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH) and ball.x <= SCREEN_WIDTH - (PADDLE_MARGIN + BALL_WIDTH) + ball.speed*3)and (ball.y >= paddle2.rect.y and ball.y <=paddle2.rect.y + PADDLE_HEIGHT):
        return 2
    return 0

def updateScore(playerNum):
    global lastUp1, lastUp2,score1,score2
    if playerNum == 1 and lastUp1 >= FPS:
        score1 += 1
        lastUp1 = 0
    if playerNum == 2 and lastUp2 >= FPS:
        score2 += 1
        lastUp2 = 0

def play_game(screen):
    global score1,score2, lastUp1,lastUp2, paddle1,paddle2, ball, screen_size
    pygame.display.set_caption("Ping Pong")

    clock = pygame.time.Clock()

    paddle1.rect.x = PADDLE_MARGIN
    paddle1.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2 + SCORE_MARGIN//2

    paddle2.rect.x = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_MARGIN
    paddle2.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2 + SCORE_MARGIN//2

    ball.setResetMargin(BALL_RESET_Y_MARGIN)
    ball.setBounceBias(PADDLE_BOUNCE_BIAS)
    ball.reset()
    ball.update()

    movingsprites = pygame.sprite.Group()
    movingsprites.add(paddle1)
    movingsprites.add(paddle2)
    movingsprites.add(ball)
    
    exit_window=False
    
    while not exit_window:

        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        exit_window = True
            
        if ball.x > PADDLE_MARGIN + PADDLE_WIDTH and ball.x < SCREEN_WIDTH - (PADDLE_MARGIN + PADDLE_WIDTH):
            lastUp1 += 1
            lastUp2 += 1
        ball.update()
        
        if collides() == 1:
            diff = (paddle1.rect.y + PADDLE_HEIGHT/2) - (ball.rect.y+BALL_HEIGHT/2)
            ball.x = PADDLE_MARGIN+PADDLE_WIDTH + 2
            ball.bounce(diff)
            updateScore(1)

        if collides() == 2:
            diff = (paddle2.rect.y + PADDLE_HEIGHT/2) - (ball.rect.y+BALL_HEIGHT/2) 
            ball.x = SCREEN_WIDTH - (PADDLE_MARGIN+BALL_WIDTH+2)
            ball.bounce(-diff)
            updateScore(2)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            paddle1.moveUp(PADDLE_SPEED)
        if keys[pygame.K_s]:
            paddle1.moveDown(PADDLE_SPEED)
        if keys[pygame.K_UP]:
            paddle2.moveUp(PADDLE_SPEED)
        if keys[pygame.K_DOWN]:
            paddle2.moveDown(PADDLE_SPEED)

        if keys[pygame.K_ESCAPE]:
            exit_window = True
            
        if keys[pygame.K_F11]:
            screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        movingsprites.update()

        pygame.draw.line(screen,WHITE,[SCREEN_WIDTH//2,SCORE_MARGIN],[SCREEN_WIDTH//2,SCREEN_HEIGHT],5)

        pygame.draw.line(screen,WHITE,[0,SCORE_MARGIN],[SCREEN_WIDTH,SCORE_MARGIN],5)

        movingsprites.draw(screen)
        
        font = pygame.font.Font(None,74)
        
        text1 = font.render(str(score1),1,WHITE)
        screen.blit(text1,((SCREEN_WIDTH//2)//2,10))
        
        text2 = font.render(str(score2),1,WHITE)
        screen.blit(text2,(3*((SCREEN_WIDTH//2)//2),10))

        if score1 == 10 or score2 == 10:
            screen.fill(BLACK)
            text3 = font.render("WINS",1,WHITE)
            text4 = font.render("PLAYER 1",1,WHITE)
            text5 = font.render("PLAYER 2",1,WHITE)

            if score1 == 10:
                screen.blit(text4,(SCREEN_WIDTH//2 - 120,SCREEN_HEIGHT//2 - 74))
                screen.blit(text3,(SCREEN_WIDTH//2 - 75,SCREEN_HEIGHT//2 - 4))

            else:
                screen.blit(text5,(SCREEN_WIDTH//2 - 120,SCREEN_HEIGHT//2 - 74))
                screen.blit(text3,(SCREEN_WIDTH//2 - 75,SCREEN_HEIGHT//2 - 4))
        
        pygame.display.flip()

        clock.tick(FPS)
        
        # if event.type == pygame.KEYDOWN and keys[pygame.K_p]:
        #     while True:
        #         event = pygame.event.wait()
        #         if event.type == pygame.KEYDOWN and keys[pygame.K_p]:
        #             break
        #         if event.type == pygame.QUIT:
        #             exit_window = True
        #             break 
        #         if keys[pygame.K_ESCAPE]:
        #             exit_window = True
        #             break

    pygame.quit()

class GameState(Enum):
    QUIT=-1
    MENU=0
    PLAYGAME=1
    PAUSE=2
    ENDGAME=3

if __name__=="__main__":
    main()
