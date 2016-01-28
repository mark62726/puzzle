import pygame as pg
from .. import prepare, tools
from ..components import image_drop
from ..states import game

class Level1(game.Game):
    def __init__(self):
        game.Game.__init__(self)
        self.droppers = [
            image_drop.ImageDrop(self.tile_rect.size, self.screen_rect.center),
            image_drop.ImageDrop(self.tile_rect.size, tools.from_center(self.screen_rect, (400,0))),
            image_drop.ImageDrop(self.tile_rect.size, tools.from_center(self.screen_rect, (-400,0)))
        ]

        self.fill_queue()
        self.queue_layout()
        self.controlled_drag = None
        
    def fill_queue(self):
        self.queue = []
        self.queue.append(self.btn_dict['right_arrow'])
        self.queue.append(self.btn_dict['left_arrow'])
        self.queue.append(self.btn_dict['up_arrow'])
        self.queue.append(self.btn_dict['down_arrow'])
            
    def queue_layout(self):
        self.queue_spacer = 10
        for i, obj in enumerate(self.queue):
            obj.rect.x = i*(obj.rect.width+self.queue_spacer)
            obj.true_pos = list(obj.rect.center)
        
    def additional_get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            if prepare.DEBUG:
                if event.key == pg.K_n:
                    self.next = 'LEVEL2'
                elif event.key == pg.K_p:
                    self.next = 'LEVEL1'
                self.done = True
        for v in self.queue:
            v.get_event(event)
        for drop in self.droppers:
            drop.get_event(event, self.controlled_drag)
        
    def additional_update(self, now, keys, scale):
        if now-self.timer > 1000:
            self.timer = now
        for drop in self.droppers:
            drop.update()
        for drag in self.queue:
            drag.update(self.screen_rect, self.mouse_pos, scale)
            if drag.click:
                self.controlled_drag = drag
        
    def additional_render(self, surface):
        
        for drop in self.droppers:
            drop.render(surface)
        for v in reversed(self.queue):
            surface.blit(v.image, v.rect)
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
