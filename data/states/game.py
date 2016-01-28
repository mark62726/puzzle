
import pygame as pg
from . import state
from .. import prepare, tools
from ..components import image_drop

class Game(state.State):
    '''
    super class to all level states
    '''
    def __init__(self):
        state.State.__init__(self)
        self.setup_bg(self.screen_rect)
        self.tile_rect = self.btn_dict['square'].rect #arbitrary single object for sizing

    def setup_bg(self, screen_rect):
        self.bg_orig = prepare.GFX['bg']
        self.bg = pg.transform.smoothscale(self.bg_orig, self.screen_rect.size)
        
    def additional_get_event(self, event):
        '''subclass level get_event runs'''
        pass
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.next = 'MENU'
                self.done = True
        self.music.get_event(event)
        self.additional_get_event(event, keys)
        
    def additional_update(self, now, keys, scale):
        '''subclass level updates'''
        pass
        
    def update(self, now, keys, scale):
        pg.mouse.set_visible(True)
        if now-self.timer > 1000:
            self.timer = now
        self.additional_update(now, keys, scale)
                
    def additional_render(self):
        '''subclass level render'''
        pass
        
    def render(self, surface):
        surface.blit(self.bg,(0,0))
        self.additional_render(surface)
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        


        
