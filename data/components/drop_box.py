import pygame as pg
from .. import prepare, tools

class DropBox:
    def __init__(self, size, pos):
        self.color_full = (255,255,255)
        self.color_empty = (255,0,0)
        self.color = self.color_full
        self.border = 10
        size = list(size)
        size[0], size[1] = size[0]+self.border, size[1]+self.border
        self.size = size
        self.image = pg.Surface(self.size).convert()
        self.image.fill((255,0,255))
        self.image.set_colorkey((255,0,255))
        self.draw_rect()
        self.rect_orig = self.image.get_rect(center=pos)
        self.rect = self.rect_orig.inflate((self.border,self.border))
        self.empty = True
        self.occupant = None
        self.place_tile_sound = prepare.SFX['button2']
        self.place_tile_sound.set_volume(.2)
        
    def draw_rect(self):
        pg.draw.rect(self.image, self.color, pg.Rect((0,0),self.size), self.border)
        
    def get_event(self, event, obj):
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            if obj:
                if self.rect.colliderect(obj.rect):
                    if self.empty:
                        self.place_tile_sound.play()
                    self.set_occupant(obj)
        elif event.type == pg.MOUSEMOTION:
            if self.occupant and self.rect:
                if not self.rect.colliderect(self.occupant.rect):
                    self.empty = True
                    
    def set_occupant(self, obj):
        obj.rect.topleft = self.rect_orig.topleft
        obj.update_true_pos()
        self.empty = False
        self.occupant = obj
        
    def update(self):
        self.draw_rect()
        if not self.empty:
            self.color = self.color_full
        else:
            self.color = self.color_empty
        
    def render(self, surf):
        surf.blit(self.image, self.rect)
