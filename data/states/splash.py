import pygame as pg
from . import state
from .. import prepare

class Splash(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'GAME'
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            self.done = True
        
    def update(self, now, keys):
        pg.mouse.set_visible(False)
        if now-self.timer > 2000:
            self.timer = now
            self.done = True
        
    def render(self):
        prepare.SCREEN.blit(prepare.GFX['splash_page'],(0,0))
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        
