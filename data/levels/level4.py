import pygame as pg
from .. import prepare, tools
from ..components import drop_box, flashing_text
from ..states import game

class Level4(game.Game):
    def __init__(self):
        game.Game.__init__(self)
        self.next = 'MENU'
        self.drop_boxes = {
            'move_down':drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (100,-120))),
            'move_right':drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (-400,-120))),
            'move_left':drop_box.DropBox(self.tile_rect.size, tools.from_center(self.screen_rect, (100,75))),

        }
        self.flash_text = flashing_text.FlashingText('CORRUPTED', (255,255,255),(255,0,0),(300,500), 75, prepare.FONTS['arcade'], 200)
        self.setup_end_text(pos=(300,700))
        self.setup_text_flow()
        self.fill_tile_queue_order()
        self.tile_queue_layout()
        self.fill_drop_box_layout()
        self.control_flow_order()
        self.control_arrow_rect.centery = self.control_flow[0].centery
        
    def setup_text_flow(self):
        '''setup arbitrary texts for control flow'''
        self.text_flow = {
            #'corrupt':self.make_text('CORRUPTED', (255,255,255),(300,500), 75, prepare.FONTS['arcade']),
            'break':self.make_text('break;', (255,255,255), (300,600), 75, prepare.FONTS['leet']),
            'var':self.make_text('var = 1;', (255,255,255), (300,300), 75, prepare.FONTS['arcade']),
            'while':self.make_text('while(true)', (255,255,255), (800,500), 75, prepare.FONTS['impact']),
            'continue':self.make_text('continue;', (255,255,255), (800,700), 75, prepare.FONTS['impact']),
        }
        
    def control_flow_order(self):
        '''order of control flow to complete level'''
        self.control_flow = [
            self.start_text_rect,
            self.text_flow['var'][1],
            self.drop_boxes['move_right'].rect,
            self.flash_text.rect,
            #self.text_flow['corrupt'][1],
            self.text_flow['break'][1],
            self.end_text_rect,
            self.drop_boxes['move_down'].rect,
            self.text_flow['while'][1],
            self.drop_boxes['move_left'].rect,
            self.text_flow['continue'][1],
        ]
        
    def fill_tile_queue_order(self):
        '''fill tile queue to specific level order '''
        self.tile_queue = [
        ]
            
    def fill_drop_box_layout(self):
        '''drop boxes that have tiles in them from start'''
        self.drop_box_queue = [
            self.btn_dict['down_arrow'],
            self.btn_dict['left_arrow'],
            self.btn_dict['right_arrow'],
        ]
        self.drop_boxes['move_right'].set_occupant(self.drop_box_queue[0])
        self.drop_boxes['move_down'].set_occupant(self.drop_box_queue[1])
        self.drop_boxes['move_left'].set_occupant(self.drop_box_queue[2])
            
    def update_control_arrow(self, now):
        '''pause/start control flow, change pause/start arrow color, and move arrow'''
        if self.all_boxes_full(): 
            self.control_paused = False
            if now-self.timer > 1000:
                self.timer = now
                self.control_flow_index += 1
                if self.control_flow_index > len(self.control_flow)-1:
                    self.control_flow_index = 0
                    self.set_control('left')
                
                #1+ to index to hold arrow at position
                if self.control_flow_index == 4:
                    self.control_flow_index = 0
                    self.fail_sound.play()
                elif self.control_flow_index == 3:
                    if self.drop_boxes['move_right'].occupant.value == 'right_arrow':
                        self.set_control('middle')
                        self.control_flow_index = 6
                elif self.control_flow_index == 9:
                    if self.drop_boxes['move_left'].occupant.value == 'left_arrow':
                        self.control_flow_index = 4
                        self.set_control('left')
                elif self.control_flow_index == 7:
                    if self.drop_boxes['move_down'].occupant.value == 'left_arrow':
                        self.set_control('left')
                        self.control_flow_index = 2
                elif self.control_flow_index == 9:
                    self.set_control('left')
                    self.control_flow_index = 0
                
            self.control_arrow_rect.centery = self.control_flow[self.control_flow_index].centery
        else:
            self.control_paused = True
        #print(self.control_flow_index)
            
        if self.control_flow_index == 5:
            self.level_complete_sound.play()
            self.done = True
        
    def additional_update(self, now, keys, scale):
        self.update_control_arrow(now)
        self.flash_text.update(now)
                
    def additional_render(self, surface):
        self.flash_text.render(surface)
            
    def reset(self):
        self.control_flow_index = 0
        self.tile_queue_layout()
        self.fill_drop_box_layout()
        
    def cleanup(self):
        self.reset()
        
    def entry(self):
        pass
