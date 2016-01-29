
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
        self.tile_queue = []
        self.control_flow_index = 0
        self.controlled_drag = None
        self.control_pause = False
        self.setup_start_text()
        
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

    def setup_bg(self, screen_rect):
        self.bg_orig = prepare.GFX['bg']
        self.bg = pg.transform.smoothscale(self.bg_orig, self.screen_rect.size)
        
    def additional_get_event(self, event, keys):
        '''subclass level get_event runs'''
        pass
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.next = 'MENU'
                self.done = True
        self.music.get_event(event)
        self.additional_get_event(event, keys)
        for v in self.tile_queue:
            v.get_event(event)
        for tile in self.drop_box_queue:
            tile.get_event(event)
        for box in self.drop_boxes:
            box.get_event(event, self.controlled_drag)
        
    def additional_update(self, now, keys, scale):
        '''subclass level updates'''
        pass
        
    def update(self, now, keys, scale):
        pg.mouse.set_visible(True)
        self.additional_update(now, keys, scale)
        for box in self.drop_boxes:
            box.update()
        for drag in self.tile_queue:
            drag.update(self.screen_rect, self.mouse_pos, scale)
            if drag.click:
                self.controlled_drag = drag
        for tile in self.drop_box_queue:
            tile.update(self.screen_rect, self.mouse_pos, scale)
            if tile.click:
                self.controlled_drag = tile
                
    def additional_render(self):
        '''subclass level render'''
        pass
        
    def render(self, surface):
        surface.blit(self.bg,(0,0))
        self.additional_render(surface)
        surface.blit(self.start_text, self.start_text_rect)
        surface.blit(self.end_text, self.end_text_rect)
        for box in self.drop_boxes:
            box.render(surface)
        for v in reversed(self.tile_queue):
            v.render(surface)
        for tile in self.drop_box_queue:
            tile.render(surface)
            
        if not self.control_paused:
            surface.blit(self.control_arrow, self.control_arrow_rect)
        else:
            surface.blit(self.control_arrow_paused, self.control_arrow_rect)
            
        for obj,rect in self.text_flow:
            surface.blit(obj, rect)

    def tile_queue_layout(self):
        '''starting layout of unselected tiles from the tile queue'''
        self.tile_queue_spacer = 10
        for i, obj in enumerate(self.tile_queue):
            obj.rect.x = i*(obj.rect.width+self.tile_queue_spacer)
            obj.rect.y = 0
            obj.true_pos = list(obj.rect.center)
            
    def all_boxes_full(self):
        for box in self.drop_boxes:
            if box.empty:
                return False
        return True
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        


        
