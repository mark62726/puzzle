import pygame as pg
from .. import prepare, tools
from ..components import button

class State:
    '''
    Super class for all states 
    '''
    def __init__(self):
        self.quit = False #quit game
        self.done = False #quit state
        self.timer = 0.0
        self.music_volume = .3
        self.music = tools.Music(volume=self.music_volume)
        
        
        self.buttons = tools.strip_from_sheet(prepare.GFX['arrows'], (0,0), (62,62), 5,3)
        self.btn_dict = {
            'turnaround_arrow'      :button.ImageDrag(self.buttons[0]),
            'right_arrow'           :button.ImageDrag(self.buttons[1]),
            'up_arrow'              :button.ImageDrag(pg.transform.rotate(self.buttons[1], 90)),
            'left_arrow'            :button.ImageDrag(pg.transform.rotate(self.buttons[1], 180)),
            'down_arrow'            :button.ImageDrag(pg.transform.rotate(self.buttons[1], 270)),
            'horizontal_arrows'     :button.ImageDrag(self.buttons[2]),
            'vertical_arrows'       :button.ImageDrag(pg.transform.rotate(self.buttons[2], 90)),
            '3_way_arrow_up'        :button.ImageDrag(self.buttons[3]),
            '3_way_arrow_left'      :button.ImageDrag(pg.transform.rotate(self.buttons[3], 90)),
            '3_way_arrow_down'      :button.ImageDrag(pg.transform.rotate(self.buttons[3], 180)),
            '3_way_arrow_right'     :button.ImageDrag(pg.transform.rotate(self.buttons[3], 270)),
            'lighting_arrow'        :button.ImageDrag(self.buttons[4]),
            'triangle_right'        :button.ImageDrag(self.buttons[5]),
            'triangle_up'           :button.ImageDrag(pg.transform.rotate(self.buttons[5], 90)),
            'triangle_left'         :button.ImageDrag(pg.transform.rotate(self.buttons[5], 180)),
            'triangle_down'         :button.ImageDrag(pg.transform.rotate(self.buttons[5], 270)),
            '4_way_arrow'           :button.ImageDrag(self.buttons[6]),
            '4_way_arrow_box'       :button.ImageDrag(self.buttons[7]),
            'arrowhead_right'       :button.ImageDrag(self.buttons[8]),
            'arrowhead_up'          :button.ImageDrag(pg.transform.rotate(self.buttons[8], 90)),
            'arrowhead_left'        :button.ImageDrag(pg.transform.rotate(self.buttons[8], 180)),
            'arrowhead_down'        :button.ImageDrag(pg.transform.rotate(self.buttons[8], 270)),
            'fat_arrow_right'       :button.ImageDrag(self.buttons[9]),
            'square'                :button.ImageDrag(self.buttons[10]),
            'arrow_90'              :button.ImageDrag(self.buttons[11]),
            'flex_u_arrow'          :button.ImageDrag(self.buttons[12]),
            'bent_arrow_up'         :button.ImageDrag(self.buttons[13]),
            's_curve_arrow'         :button.ImageDrag(self.buttons[14]),
        }
