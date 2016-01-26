import pygame as pg
from .. import prepare, tools

class CreditSurf:
    def __init__(self, size, pos):
        self.color = (255,255,255)
        self.border = 1
        size = list(size)
        size[0], size[1] = size[0]+self.border, size[1]+self.border
        self.image = pg.Surface(size).convert()
        self.image.fill((255,0,255))
        self.image.set_colorkey((255,0,255))
        pg.draw.rect(self.image, self.color, pg.Rect((0,0),size), self.border)
        self.rect = self.image.get_rect(bottomleft=pos)
        self.rect.inflate_ip((self.border,self.border))
        
    def update(self):
        pass
        
    def render(self, surf):
        surf.blit(self.image, self.rect)
