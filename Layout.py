import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)

size = (900,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
pygame.mouse.set_visible(0)

screen.fill(black)
pygame.draw.line(screen,white,[449,0],[449,600],8)

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.Surface([12,100])
        self.image.fill(white)
        
        self.rect = self.image.get_rect()

paddle1 = Paddle()
paddle1.rect.x = 20
paddle1.rect.y = 250

paddle2 = Paddle()
paddle2.rect.x = 870
paddle2.rect.y = 250

movingsprites = pygame.sprite.Group()
movingsprites.add(paddle1)
movingsprites.add(paddle2)

movingsprites.draw(screen)

pygame.display.flip()
