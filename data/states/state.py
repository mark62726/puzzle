import pygame as pg
from .. import prepare, tools
from ..components import image_drag

class State:
    '''
    Super class for all states 
    '''
    def __init__(self):
        self.screen_rect = pg.Rect((0, 0), prepare.RENDER_SIZE)
        self.quit = False #quit game
        self.done = False #quit state
        self.timer = 0.0
        self.music_volume = prepare.MUSIC_VOLUME
        self.music = prepare.MUSIC
        self.mouse_pos = (0,0)
        
        self.buttons = tools.strip_from_sheet(prepare.GFX['arrows'], (0,0), (62,62), 5,3)
        self.btn_dict = {
            'turnaround_arrow'      :image_drag.ImageDrag(self.buttons[0]),
            'right_arrow'           :image_drag.ImageDrag(self.buttons[1]),
            'up_arrow'              :image_drag.ImageDrag(pg.transform.rotate(self.buttons[1], 90)),
            'left_arrow'            :image_drag.ImageDrag(pg.transform.rotate(self.buttons[1], 180)),
            'down_arrow'            :image_drag.ImageDrag(pg.transform.rotate(self.buttons[1], 270)),
            'horizontal_arrows'     :image_drag.ImageDrag(self.buttons[2]),
            'vertical_arrows'       :image_drag.ImageDrag(pg.transform.rotate(self.buttons[2], 90)),
            '3_way_arrow_up'        :image_drag.ImageDrag(self.buttons[3]),
            '3_way_arrow_left'      :image_drag.ImageDrag(pg.transform.rotate(self.buttons[3], 90)),
            '3_way_arrow_down'      :image_drag.ImageDrag(pg.transform.rotate(self.buttons[3], 180)),
            '3_way_arrow_right'     :image_drag.ImageDrag(pg.transform.rotate(self.buttons[3], 270)),
            'lighting_arrow'        :image_drag.ImageDrag(self.buttons[4]),
            'triangle_right'        :image_drag.ImageDrag(self.buttons[5]),
            'triangle_up'           :image_drag.ImageDrag(pg.transform.rotate(self.buttons[5], 90)),
            'triangle_left'         :image_drag.ImageDrag(pg.transform.rotate(self.buttons[5], 180)),
            'triangle_down'         :image_drag.ImageDrag(pg.transform.rotate(self.buttons[5], 270)),
            '4_way_arrow'           :image_drag.ImageDrag(self.buttons[6]),
            '4_way_arrow_box'       :image_drag.ImageDrag(self.buttons[7]),
            'arrowhead_right'       :image_drag.ImageDrag(self.buttons[8]),
            'arrowhead_up'          :image_drag.ImageDrag(pg.transform.rotate(self.buttons[8], 90)),
            'arrowhead_left'        :image_drag.ImageDrag(pg.transform.rotate(self.buttons[8], 180)),
            'arrowhead_down'        :image_drag.ImageDrag(pg.transform.rotate(self.buttons[8], 270)),
            'fat_arrow_right'       :image_drag.ImageDrag(self.buttons[9]),
            'square'                :image_drag.ImageDrag(self.buttons[10]),
            'arrow_90'              :image_drag.ImageDrag(self.buttons[11]),
            'flex_u_arrow'          :image_drag.ImageDrag(self.buttons[12]),
            'bent_arrow_up'         :image_drag.ImageDrag(self.buttons[13]),
            's_curve_arrow'         :image_drag.ImageDrag(self.buttons[14]),
        }
        
    def update(self, now, keys, scale):
        self.mouse_pos = tools.scaled_mouse_pos(scale)
