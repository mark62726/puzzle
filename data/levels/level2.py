import pygame as pg
from .. import prepare, tools
from ..components import drop_box
from ..states import game

class Level2(game.Game):
    def __init__(self):
        game.Game.__init__(self)
        self.next = 'MENU'
        
        self.drop_boxes = [
            drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (-400,75))),
            drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (-400,-120))),
        ]
        self.setup_end_text(pos=(300,700))
        self.setup_text_flow()
        self.fill_tile_queue_order()
        self.tile_queue_layout()
        self.fill_drop_box_layout()
        self.control_flow_order()
        
    def setup_text_flow(self):
        '''setup arbitrary texts for control flow'''
        self.text_flow = [
            self.make_text('var = 0;', (245,245,245), (300,300), 50, prepare.FONTS['impact']),
            self.make_text('max(list);', (245,245,245), (300,500), 50, prepare.FONTS['leet']),
        ]
        
    def control_flow_order(self):
        '''order of control flow to complete level'''
        self.control_flow = [
            self.start_text_rect,
            self.text_flow[0][1],
            self.drop_boxes[1].rect,
            self.text_flow[1][1],
            self.drop_boxes[0].rect,
            self.end_text_rect,
        ]
        
    def fill_tile_queue_order(self):
        '''fill tile queue to specific level order '''
        self.tile_queue = [
            #self.btn_dict['jump'],
            #self.btn_dict['jump2'],
        ]
            
    def fill_drop_box_layout(self):
        '''drop boxes that have tiles in them from start'''
        self.drop_box_queue = [
            self.btn_dict['turnaround_arrow'],
            self.btn_dict['down_arrow'],
        ]
        self.drop_boxes[0].set_occupant(self.drop_box_queue[0])
        self.drop_boxes[1].set_occupant(self.drop_box_queue[1])
            
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
                if self.control_flow_index == 5: #one up from box
                    if not self.drop_boxes[0].occupant.control == 'down_arrow':
                        self.control_flow_index = 0
                if self.control_flow_index == 3:
                    if not self.drop_boxes[0].occupant.control == 'turnaround_arrow':
                        self.control_flow_index = 0
                
            self.control_arrow_rect.centery = self.control_flow[self.control_flow_index].centery
        else:
            self.control_paused = True
            
        if self.control_flow_index == len(self.control_flow)-1:
            self.level_complete_sound.play()
            self.done = True
        
    def additional_update(self, now, keys, scale):
        self.update_control_arrow(now)
                
    def additional_render(self, surface):
        pass
            
    def reset(self):
        self.control_flow_index = 0
        self.tile_queue_layout()
        self.fill_drop_box_layout()
        
    def cleanup(self):
        self.reset()
        
    def entry(self):
        pass
