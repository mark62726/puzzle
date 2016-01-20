import pygame as pg
from .. import prepare, tools

class ImageDrag(object):
    def __init__(self, image, pos=(0,0)):
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.click = False
        self.scale = None

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            tools.scaled_mouse_rel(self.scale, pos)

    def update(self, screen_rect, pos, scale):
        self.scale = scale
        if self.click:
            self.rect.move_ip(tools.scaled_mouse_rel(scale, pos))
            self.rect.clamp_ip(screen_rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class FontDrag(object):
    SIZE = (150, 150)
    
    def __init__(self, pos, msg, color):
        self.rect = pg.Rect((0,0), FontDrag.SIZE)
        self.rect.center = pos
        self.text, self.text_rect = self.setup_font(msg, color)
        self.click = False

    def setup_font(self, msg, color):
        font = pg.font.Font(prepare.FONTS['impact'], 50)
        label = font.render(msg, True, color)
        label_rect = label.get_rect()
        return label, label_rect

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pg.mouse.get_rel()

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pg.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        self.text_rect.center = (self.rect.centerx, self.rect.centery+90)

    def draw(self, surface):
        surface.blit(self.text, self.text_rect)
