
import pygame as pg
from . import state
from .. import prepare, tools

class Game(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'MENU'
        self.setup_bg()
        
    def setup_bg(self):
        self.bg_orig = prepare.GFX['bg']
        self.bg = pg.transform.smoothscale(self.bg_orig, prepare.SCREEN_RECT.size)
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for v in self.btn_dict.values():
                v.check_click(event.pos)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            for v in self.btn_dict.values():
                v.click = False
        self.music.get_event(event)
        
    def update(self, now, keys):
        pg.mouse.set_visible(True)
        if now-self.timer > 1000:
            self.timer = now
            
        for v in self.btn_dict.values():
            v.update(prepare.SCREEN_RECT)
        
    def render(self):
        prepare.SCREEN.blit(self.bg,(0,0))
        
        
        for v in self.btn_dict.values():
            prepare.SCREEN.blit(v.image, v.rect)
        
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        

        
