import pygame as pg

class VarDisplay:
    def __init__(self, color1, color2, center, size, fonttype, value=0, limit=100):
        self.value = value
        self.limit = limit
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.flip = False
        self.center = center
        self.size = size 
        self.fonttype = fonttype
        self.update_msg()
        self.make_text(self.msg, color1, center, size, fonttype)
        self.timer = 0.0
        
    def make_text(self,message,color,center,size, fonttype):
        font = pg.font.Font(fonttype, size)
        self.text = font.render(message,True,color)
        self.rect = self.text.get_rect(center=center)
        
    def update(self, now):
        self.update_msg()
        if self.value >= self.limit:
            self.color = self.color1
        else:
            self.color = self.color2
        self.make_text(self.msg, self.color, self.center, self.size, self.fonttype)
            
    def update_msg(self):
        self.msg = 'var = {}'.format(self.value)
        
    def render(self, surf):
        surf.blit(self.text, self.rect)
