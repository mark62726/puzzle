import pygame as pg

class ImageDrag(object):
    def __init__(self, image, pos=(0,0)):
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.click = False

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pg.mouse.get_rel()

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pg.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
