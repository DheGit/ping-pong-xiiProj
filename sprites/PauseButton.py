import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect

class PauseButton(Sprite):
    def __init__(self, action = None, position = (0,0), dimensions=(0,0)):

        pygame.init()

        pb = pygame.image.load('image\image.png')
        
        self.mouse_over = False

        # self.rect = pb.get_rect(center = (SCREEN_WIDTH/2, 20))
        self.rect=pygame.Rect(position[0],position[1],dimensions[0],dimensions[1])
    
        self.action = action
        self.clickSound=pygame.mixer.Sound('sound/click3.wav')
    
        super().__init__()

    @property
    def rects(self):
        return self.rect

    def update(self, mouse_pos, mouse_up):
        if self.rects.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                self.clickSound.play()
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(pausebutton, (SCREEN_WIDTH/2, 20))
        surface.blit(self.rects)

