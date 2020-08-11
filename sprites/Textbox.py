import pygame

from r import colors

pygame.init()

class Textbox:
    
    def __init__(self, x, y, w, h, fontsize=24, maxlength=100, resizable=True, text='', textcolor=colors.WHITE, bordercolor=(40,120,180), activebordercolor=(200,0,0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = bordercolor
        self.inactivecolor = bordercolor
        self.textcolor = textcolor
        self.activecolor = activebordercolor
        self.maxlength = maxlength
        self.resizable = resizable
        self.text = text
        
        self.fontsize = fontsize
        self.font=pygame.font.Font(None, self.fontsize)

        self.txt_surface = self.font.render(text, True, self.color)
        self.txt_surface.set_alpha(0)

        self.active = False

        self.repeater_count={}
        self.nr_init=400
        self.nr_inter=35

        self.clock=pygame.time.Clock()


    def handle_events(self,events):
        for event in events:
            self.handle_event(event)

        for k in self.repeater_count:
            self.repeater_count[k][0]+=self.clock.get_time()
            if self.repeater_count[k][0] >= self.nr_init:
                self.repeater_count[k][0]=(self.nr_init - self.nr_inter)

                e_key, e_uni=k,self.repeater_count[k][1]
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=e_key,unicode=e_uni))
        
        self.txt_surface = self.font.render(self.text, True, self.textcolor)
        
        self.clock.tick()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.activecolor
            else:
                self.active = False
                self.color = self.inactivecolor

        if self.active:
            if event.type == pygame.KEYDOWN:
                if event.key not in self.repeater_count:
                    self.repeater_count[event.key]=[0,event.unicode]

                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key in [pygame.K_TAB, pygame.K_ESCAPE]:
                    pass
                else:
                    if len(self.text) < self.maxlength:
                        self.text += event.unicode

            elif event.type==pygame.KEYUP:
                del self.repeater_count[event.key]

    def update(self):
        if self.resizable:
            width = max(200, self.txt_surface.get_width()+10)
            self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def getText(self):
        return self.text