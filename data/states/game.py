
import pygame as pg
from . import state
from .. import prepare, tools

class Game(state.State):
    '''
    super class to all level states
    '''
    def __init__(self):
        state.State.__init__(self)
        self.next = 'MENU'
        self.setup_bg(self.screen_rect)
        self.tile_rect = self.btn_dict['square'].rect #arbitrary single object for sizing
        self.setup_control_arrows()
        self.control_paused = None
        self.level_complete_sound = prepare.SFX['positive']
        self.level_complete_sound.set_volume(.5)
        
    def get_level_num(self):
        return self.__class__.__name__[5:]
        
    def setup_start_text(self):
        self.start_text, self.start_text_rect = self.make_text(
            'Start({})'.format(self.get_level_num()), (245,245,245), (300,200), 50, prepare.FONTS['hackers'])

    def setup_end_text(self, pos):
        self.end_text, self.end_text_rect = self.make_text(
            'return 0;', (245,245,245), pos, 50, prepare.FONTS['hackers'])
        
    def setup_control_arrows(self):
        sheet = prepare.GFX['colored_arrows']
        arrows = tools.strip_from_sheet(sheet, (0,0), (126,164), 2, 1)
        self.control_arrow_paused = pg.transform.smoothscale(arrows[1], (75,100))
        self.control_arrow_paused = pg.transform.rotate(self.control_arrow_paused, 90)
        self.control_arrow = pg.transform.smoothscale(arrows[0], (75,100))
        self.control_arrow = pg.transform.rotate(self.control_arrow, 270)
        self.control_arrow_rect = self.control_arrow.get_rect()
        self.control_arrow_col = self.control_arrow_rect.copy()
        self.control_arrow_col.width = 5000

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
        #if now-self.timer > 100:
        #    self.timer = now
            #print('sec')
        self.additional_update(now, keys, scale)
                
    def additional_render(self):
        '''subclass level render'''
        pass
        
    def render(self, surface):
        surface.blit(self.bg,(0,0))
        self.additional_render(surface)
        surface.blit(self.start_text, self.start_text_rect)
        surface.blit(self.end_text, self.end_text_rect)
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        


        
