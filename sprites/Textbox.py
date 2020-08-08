import pygame

from r import colors

pygame.init()

class Textbox:
    
    def __init__(self, x, y, w, h, fontsize=24, maxlength=100, resizable=True, text='', textcolor=colors.BLACK, bordercolor=(40,120,180), activebordercolor=(200,0,0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = bordercolor
        self.inactivecolor = bordercolor
        self.textcolor = textcolor
        self.activecolor = activebordercolor
        self.maxlength = maxlength
        self.resizable = resizable
        self.text = text
        self.fontsize = fontsize
        Font = pygame.font.Font(None, self.fontsize)
        self.txt_surface = Font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.activecolor
            else:
                self.active = False
                self.color = self.inactivecolor

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key in [pygame.K_TAB, pygame.K_ESCAPE]:
                    pass
                else:
                    if len(self.text) < self.maxlength:
                        self.text += event.unicode

                Font = pygame.font.Font(None, self.fontsize)
                self.txt_surface = Font.render(self.text, True, self.textcolor)

    def update(self):
        if self.resizable:
            width = max(200, self.txt_surface.get_width()+10)
            self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
