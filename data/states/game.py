
import pygame as pg
from . import state
from .. import prepare, tools

class Game(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'MENU'
        self.screen_rect = pg.Rect((0, 0), prepare.RENDER_SIZE)
        self.setup_bg(self.screen_rect)
        
    def setup_bg(self, screen_rect):
        self.bg_orig = prepare.GFX['bg']
        self.bg = pg.transform.smoothscale(self.bg_orig, self.screen_rect.size)
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for v in self.btn_dict.values():
                v.check_click(self.mouse_pos)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            for v in self.btn_dict.values():
                v.click = False
        self.music.get_event(event)
        
    def update(self, now, keys, scale):
        pg.mouse.set_visible(True)
        if now-self.timer > 1000:
            self.timer = now
            
        for v in self.btn_dict.values():
            v.update(self.screen_rect)
        
    def render(self, surface):
        surface.blit(self.bg,(0,0))
        
        for v in self.btn_dict.values():
            surface.blit(v.image, v.rect)
        
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        


        
