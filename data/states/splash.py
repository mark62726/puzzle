import pygame as pg
from . import state
from .. import prepare

class Splash(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'MENU'
        self.bg_orig = prepare.GFX['splash_page']
        self.bg = pg.transform.smoothscale(self.bg_orig, prepare.SCREEN_RECT.size)
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            self.done = True
        
    def update(self, now, keys):
        pg.mouse.set_visible(False)
        if now-self.timer > 2000:
            self.timer = now
            self.done = True
        
    def render(self):
        prepare.SCREEN.blit(self.bg,(0,0))
        
    def cleanup(self):
        pg.mixer.music.play()
        
    def entry(self):
        pass
        
