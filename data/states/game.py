import pygame as pg
from . import state
from .. import prepare, tools

class Game(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'SPLASH'
        self.setup_bg()
        self.setup_buttons()
        
    def setup_bg(self):
        self.bg_orig = prepare.GFX['bg']
        self.bg = pg.transform.smoothscale(self.bg_orig, prepare.SCREEN_RECT.size)
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            self.done = True
        
    def update(self, now, keys):
        pg.mouse.set_visible(True)
        if now-self.timer > 1000:
            self.timer = now
        
    def render(self):
        prepare.SCREEN.blit(self.bg,(0,0))
        prepare.SCREEN.blit(self.btn_dict['arrowhead_down'], pg.mouse.get_pos())
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        
