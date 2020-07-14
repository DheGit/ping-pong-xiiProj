import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_WIDTH=900
SCREEN_HEIGHT=600
PADDLE_WIDTH=12
PADDLE_HEIGHT=120
PADDLE_MARGIN=20

size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
pygame.mouse.set_visible(0)

screen.fill(BLACK)
pygame.draw.line(screen,WHITE,[SCREEN_WIDTH//2,0],[SCREEN_WIDTH//2,SCREEN_HEIGHT],4)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.Surface([PADDLE_WIDTH,PADDLE_HEIGHT])
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()

paddle1 = Paddle()
paddle1.rect.x = PADDLE_MARGIN
paddle1.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2

paddle2 = Paddle()
paddle2.rect.x = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_MARGIN
paddle2.rect.y = SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2

movingsprites = pygame.sprite.Group()
movingsprites.add(paddle1)
movingsprites.add(paddle2)

movingsprites.draw(screen)

pygame.display.flip()

exit_window=False

while not exit_window:

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			exit_window=True

pygame.quit()