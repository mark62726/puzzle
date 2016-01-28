
import pygame as pg
from . import state
from .. import prepare, tools
from ..components import image_drop

class Game(state.State):
    def __init__(self):
        state.State.__init__(self)
        self.next = 'MENU'
        #self.screen_rect = pg.Rect((0, 0), prepare.RENDER_SIZE)
        self.setup_bg(self.screen_rect)
        
        self.drag_rect = self.btn_dict['square'].rect #arbitrary single object for sizing
        self.droppers = [
            image_drop.ImageDrop(self.drag_rect.size, self.screen_rect.center),
            image_drop.ImageDrop(self.drag_rect.size, tools.from_center(self.screen_rect, (400,0))),
            image_drop.ImageDrop(self.drag_rect.size, tools.from_center(self.screen_rect, (-400,0)))
        ]
    
        self.fill_queue()
        #self.queue_layout()
        self.controlled_drag = None
        
    def fill_queue(self):
        self.queue = []
        #for v in self.btn_dict.values():
        #    self.queue.append(v)
        
        #temp to limit queue for testing
        for i, v in enumerate(self.btn_dict.values()):
            self.queue.append(v)
            if i == 2:
                break
            
    def queue_layout(self):
        self.queue_spacer = 10
        for i, obj in enumerate(self.queue):
            obj.rect.x = (i*obj.rect.width)+self.queue_spacer
        
    def setup_bg(self, screen_rect):
        self.bg_orig = prepare.GFX['bg']
        self.bg = pg.transform.smoothscale(self.bg_orig, self.screen_rect.size)
        
    def get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
        for v in self.queue:
            v.get_event(event)
        self.music.get_event(event)
        
        #for obj in self.queue:
        #    for drop in self.droppers:
        #        drop.get_event(event, obj)
                
        #if self.controlled_drag:
        for drop in self.droppers:
            drop.get_event(event, self.controlled_drag)
        
    def update(self, now, keys, scale):
        pg.mouse.set_visible(True)
        if now-self.timer > 1000:
            self.timer = now
        for drop in self.droppers:
            drop.update()
        for drag in self.queue:
            drag.update(self.screen_rect, self.mouse_pos, scale)
            if drag.click:
                self.controlled_drag = drag
        
    def render(self, surface):
        surface.blit(self.bg,(0,0))
        
        for drop in self.droppers:
            drop.render(surface)
        for v in reversed(self.queue):
            surface.blit(v.image, v.rect)
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
        


        
