import pygame as pg
from .. import prepare, tools
from ..components import drop_box
from ..states import game

class Level1(game.Game):
    def __init__(self):
        game.Game.__init__(self)
        self.drop_boxes = [
            drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (-500,0))),
            drop_box.DropBox(self.tile_rect.size, self.screen_rect.center)
        ]

        self.fill_tile_queue_order()
        self.tile_queue_layout()
        self.controlled_drag = None
        self.fill_drop_box_layout()
        self.control_flow_order
        
    def control_flow_order(self):
        '''order of control flow to complete level'''
        self.control_flow = []
        #self.control_flow.append()
        
    def fill_tile_queue_order(self):
        '''file tile queue to specific level order '''
        self.tile_queue = []
        self.tile_queue.append(self.btn_dict['down_arrow'])
        self.tile_queue.append(self.btn_dict['right_arrow'])
            
    def tile_queue_layout(self):
        '''starting layout of unselected tiles from the tile queue'''
        self.tile_queue_spacer = 10
        for i, obj in enumerate(self.tile_queue):
            obj.rect.x = i*(obj.rect.width+self.tile_queue_spacer)
            obj.true_pos = list(obj.rect.center)
            
    def fill_drop_box_layout(self):
        '''drop boxes that have tiles in them from start'''
        self.drop_box_queue = []
        self.drop_box_queue.append(self.btn_dict['turnaround_arrow'])
        self.drop_boxes[0].set_occupant(self.drop_box_queue[0])
        
    def additional_get_event(self, event, keys):
        if event.type == pg.KEYDOWN:
            if prepare.DEBUG:
                if event.key == pg.K_n:
                    self.next = 'LEVEL2'
                elif event.key == pg.K_p:
                    self.next = 'LEVEL1'
                self.done = True
        for v in self.tile_queue:
            v.get_event(event)
        for tile in self.drop_box_queue:
            tile.get_event(event)
        for box in self.drop_boxes:
            box.get_event(event, self.controlled_drag)
        
    def additional_update(self, now, keys, scale):
        if now-self.timer > 1000:
            self.timer = now
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
        
    def additional_render(self, surface):
        for box in self.drop_boxes:
            box.render(surface)
        for v in reversed(self.tile_queue):
            v.render(surface)
        for tile in self.drop_box_queue:
            tile.render(surface)
        
    def cleanup(self):
        pass
        
    def entry(self):
        pass
