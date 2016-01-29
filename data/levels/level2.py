import pygame as pg
from .. import prepare, tools
from ..components import drop_box
from ..states import game

class Level2(game.Game):
    def __init__(self):
        game.Game.__init__(self)
        #self.level_name = 'Level1'
        self.next = 'MENU'
        self.drop_boxes = [
            drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (-400,-25))),
            #drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (-400,225))),
        ]
        self.setup_text_flow()
        self.setup_start_text() #update text to class name
        self.setup_end_text(pos=(300,650))
        self.fill_tile_queue_order()
        self.tile_queue_layout()
        self.controlled_drag = None
        self.fill_drop_box_layout()
        self.control_flow_order()
        self.control_flow_index = 0
        
        self.control_pause = False
        
    def setup_text_flow(self):
        '''setup arbitrary texts for control flow'''
        self.text_flow = [
            self.make_text('var = NULL;', (245,245,245), (300,350), 50, prepare.FONTS['impact'])
        ]
        
    def control_flow_order(self):
        '''order of control flow to complete level'''
        self.control_flow = [
            self.start_text_rect,
            self.text_flow[0][1],
            self.drop_boxes[0].rect,
            self.end_text_rect,
        ]
        
    def fill_tile_queue_order(self):
        '''fill tile queue to specific level order '''
        self.tile_queue = [
            self.btn_dict['down_arrow'],
        ]
            
    def tile_queue_layout(self):
        '''starting layout of unselected tiles from the tile queue'''
        self.tile_queue_spacer = 10
        for i, obj in enumerate(self.tile_queue):
            obj.rect.x = i*(obj.rect.width+self.tile_queue_spacer)
            obj.rect.y = 0
            obj.true_pos = list(obj.rect.center)
            
    def fill_drop_box_layout(self):
        '''drop boxes that have tiles in them from start'''
        self.drop_box_queue = [
            self.btn_dict['turnaround_arrow']
        ]
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
            
    def all_boxes_full(self):
        for box in self.drop_boxes:
            if box.empty:
                return False
        return True
            
    def update_control_arrow(self, now):
        '''pause/start control flow, change pause/start arrow color, and move arrow'''
        if self.all_boxes_full(): 
            self.control_paused = False
            if now-self.timer > 1000:
                self.timer = now
                self.control_flow_index += 1
                if self.control_flow_index > len(self.control_flow)-1:
                    self.control_flow_index = 0
                    
                #setup box[0] condition
                if self.control_flow_index == 3: #one up from box
                    if not self.drop_boxes[0].occupant.control == 'down_arrow':
                        self.control_flow_index = 0
                
            self.control_arrow_rect.centery = self.control_flow[self.control_flow_index].centery
        else:
            self.control_paused = True
            
        if self.control_flow_index == len(self.drop_boxes)+2:
            self.done = True
        
    def additional_update(self, now, keys, scale):
        self.update_control_arrow(now)
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
            
        if not self.control_paused:
            surface.blit(self.control_arrow, self.control_arrow_rect)
        else:
            surface.blit(self.control_arrow_paused, self.control_arrow_rect)
            
        for obj,rect in self.text_flow:
            surface.blit(obj, rect)
        
    def reset(self):
        self.control_flow_index = 0
        self.tile_queue_layout()
        self.fill_drop_box_layout()
        
    def cleanup(self):
        self.reset()
        
    def entry(self):
        pass
