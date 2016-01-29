import pygame as pg
from .. import prepare, tools
from ..components import tile

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
        
        self.buttons = tools.strip_from_sheet(prepare.GFX['arrows'], (0,0), (62,62), 5,4)
        self.btn_dict = {
            'turnaround_arrow'      :tile.Tile('turnaround_arrow',  self.buttons[0]),
            'right_arrow'           :tile.Tile('right_arrow',       self.buttons[1]),
            'up_arrow'              :tile.Tile('up_arrow',          pg.transform.rotate(self.buttons[1], 90)),
            'left_arrow'            :tile.Tile('left_arrow',        pg.transform.rotate(self.buttons[1], 180)),
            'down_arrow'            :tile.Tile('down_arrow',        pg.transform.rotate(self.buttons[1], 270)),
            'horizontal_arrows'     :tile.Tile(None, self.buttons[2]),
            'vertical_arrows'       :tile.Tile(None, pg.transform.rotate(self.buttons[2], 90)),
            '3_way_arrow_up'        :tile.Tile(None, self.buttons[3]),
            '3_way_arrow_left'      :tile.Tile(None, pg.transform.rotate(self.buttons[3], 90)),
            '3_way_arrow_down'      :tile.Tile(None, pg.transform.rotate(self.buttons[3], 180)),
            '3_way_arrow_right'     :tile.Tile(None, pg.transform.rotate(self.buttons[3], 270)),
            'lighting_arrow'        :tile.Tile(None, self.buttons[4]),
            'triangle_right'        :tile.Tile(None, self.buttons[5]),
            'triangle_up'           :tile.Tile(None, pg.transform.rotate(self.buttons[5], 90)),
            'triangle_left'         :tile.Tile(None, pg.transform.rotate(self.buttons[5], 180)),
            'triangle_down'         :tile.Tile(None, pg.transform.rotate(self.buttons[5], 270)),
            '4_way_arrow'           :tile.Tile(None, self.buttons[6]),
            '4_way_arrow_box'       :tile.Tile(None, self.buttons[7]),
            'arrowhead_right'       :tile.Tile(None, self.buttons[8]),
            'arrowhead_up'          :tile.Tile(None, pg.transform.rotate(self.buttons[8], 90)),
            'arrowhead_left'        :tile.Tile(None, pg.transform.rotate(self.buttons[8], 180)),
            'arrowhead_down'        :tile.Tile(None, pg.transform.rotate(self.buttons[8], 270)),
            'fat_arrow_right'       :tile.Tile(None, self.buttons[9]),
            'square'                :tile.Tile(None, self.buttons[10]),
            'arrow_90'              :tile.Tile(None, self.buttons[11]),
            'flex_u_arrow'          :tile.Tile(None, self.buttons[12]),
            'bent_arrow_up'         :tile.Tile(None, self.buttons[13]),
            's_curve_arrow'         :tile.Tile(None, self.buttons[14]),
            'jump'                  :tile.Tile('jump', self.buttons[15]),
            'jump2'                  :tile.Tile('jump', self.buttons[15]),
        }
        
    def update(self, now, keys, scale):
        self.mouse_pos = tools.scaled_mouse_pos(scale)
        
    def make_text(self,message,color,center,size, fonttype):
        font = pg.font.Font(fonttype, size)
        text = font.render(message,True,color)
        rect = text.get_rect(center=center)
        return text,rect
