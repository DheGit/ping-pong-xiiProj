import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)

size = (900,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

screen.fill(black)
pygame.draw.line(screen,white,[449,0],[449,600],8)
pygame.display.flip()

class Paddle(pygame.sprite.Sprite):
    
    def __init__(self,color,width,height):
        
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(white)
        
        pygame.draw.rect(self.image,color,[0,0,width,height])
        
        self.rect = self.image.get_rect()

paddle1 = Paddle(white,12,120)
paddle1.rect.x = 20
paddle1.rect.y = 300

paddle2 = Paddle(white,12,120)
paddle2.rect.x = 870
paddle2.rect.y = 300
