import pygame as pg
from .. import prepare, tools

class State:
    '''
    Super class for all games states 
    '''
    def __init__(self):
        self.quit = False #quit game
        self.done = False #quit state
        self.timer = 0.0
        
    def setup_buttons(self):
        self.buttons = tools.strip_from_sheet(prepare.GFX['arrows'], (0,0), (62,62), 5,3)
        self.btn_dict = {
            'turnaround_arrow'      :self.buttons[0],
            'right_arrow'           :self.buttons[1],
            'up_arrow'              :pg.transform.rotate(self.buttons[1], 90),
            'left_arrow'            :pg.transform.rotate(self.buttons[1], 180),
            'down_arrow'            :pg.transform.rotate(self.buttons[1], 270),
            'horizontal_arrows'     :self.buttons[2],
            'vertical_arrows'       :pg.transform.rotate(self.buttons[2], 90),
            '3_way_arrow_up'        :self.buttons[3],
            '3_way_arrow_left'      :pg.transform.rotate(self.buttons[3], 90),
            '3_way_arrow_down'      :pg.transform.rotate(self.buttons[3], 180),
            '3_way_arrow_right'     :pg.transform.rotate(self.buttons[3], 270),
            'lighting_arrow'        :self.buttons[4],
            'triangle_right'        :self.buttons[5],
            'triangle_up'           :pg.transform.rotate(self.buttons[5], 90),
            'triangle_left'         :pg.transform.rotate(self.buttons[5], 180),
            'triangle_down'         :pg.transform.rotate(self.buttons[5], 270),
            '4_way_arrow'           :self.buttons[6],
            '4_way_arrow_box'       :self.buttons[7],
            'arrowhead_right'       :self.buttons[8],
            'arrowhead_up'          :pg.transform.rotate(self.buttons[8], 90),
            'arrowhead_left'        :pg.transform.rotate(self.buttons[8], 180),
            'arrowhead_down'        :pg.transform.rotate(self.buttons[8], 270),
            'fat_arrow_right'       :self.buttons[9],
            'square'                :self.buttons[10],
            'arrow_90'              :self.buttons[11],
            'flex_u_arrow'          :self.buttons[12],
            'bent_arrow_up'         :self.buttons[13],
            's_curve_arrow'         :self.buttons[14],
        }
