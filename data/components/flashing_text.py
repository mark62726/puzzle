import pygame as pg

class FlashingText:
    def __init__(self, msg, color1, color2, center, size, fonttype, delay):
        self.msg = msg
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.flip = False
        self.center = center
        self.size = size 
        self.fonttype = fonttype
        self.delay = delay
        self.make_text(msg, color1, center, size, fonttype)
        self.timer = 0.0
        
    def make_text(self,message,color,center,size, fonttype):
        font = pg.font.Font(fonttype, size)
        self.text = font.render(message,True,color)
        self.rect = self.text.get_rect(center=center)
        
    def update(self, now):
        if now-self.timer > self.delay:
            self.timer = now
            self.flip = not self.flip
            if self.flip:
                self.color = self.color1
            else:
                self.color = self.color2
            self.make_text(self.msg, self.color, self.center, self.size, self.fonttype)
    def render(self, surf):
        surf.blit(self.text, self.rect)
