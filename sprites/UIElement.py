import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    pygame.init()
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    font.pad=True
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    
    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        
        self.mouse_over = False

        self.text_rgb=text_rgb

        default_image = create_surface_with_text(text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=None)
        selected_image = create_surface_with_text(text=text, font_size=font_size * 1.2, text_rgb=bg_rgb, bg_rgb=text_rgb)
        highlighted_image = create_surface_with_text(text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=None)

        self.images = [default_image, selected_image, highlighted_image]

        self.rects = [default_image.get_rect(center=center_position),
            selected_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position)]


        self.action = action
        self.highlightable = True
        self.stay_highlighted=False

        super().__init__()

    @property
    def image(self):
        if self.stay_highlighted:
            return self.images[1]
        if self.mouse_over:
            return self.images[2]

        return self.images[0]

    @property
    def rect(self):
        if self.stay_highlighted:
            return self.rects[1]
        if self.mouse_over:
            return self.rects[2]

        return self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if not self.highlightable:
            return
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                click = pygame.mixer.Sound('sound/click3.wav')
                click.play()
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

    def setHighlightable(self, highlightable):
        self.highlightable = highlightable

    def stayHighlighted(self,stay):
    	self.stay_highlighted=stay

    def staysHighlighted(self):
    	return self.stay_highlighted

    def getTextRgb(self):
    	return self.text_rgb
