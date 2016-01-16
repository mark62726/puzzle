
import pygame as pg
from . import menus
from ...toolbox import button
from ... import prepare
   
class Audio(menus.Menus):
    def __init__(self):
        menus.Menus.__init__(self)
        self.options = ['Volume','Sound','Back']
        self.next_list = ['DISABLED','DISABLED','MENU']
        self.title_text = 'Audio'
        self.pre_render_options()
        self.setup_title()
        self.from_bottom = 300
        self.music_select_label, self.music_select_label_rect = self.make_text(
            'Switch Music Track', (0,0,0), (prepare.SCREEN_RECT.centerx, 162), 15, prepare.FONTS['impact'])
        
        button_config = {
            "hover_color"        : (150,150,150),
            "clicked_color"      : (255,255,255),
            "clicked_font_color" : (0,0,0),
            "hover_font_color"   : (0,0,0),
            'font'               : pg.font.Font(prepare.FONTS['impact'], 12)
        }
        self.next_button = button.Button((475,150,100,25),(100,100,100), 
            self.music.switch_track, text='Next', **button_config
        )
        self.prev_button = button.Button((225,150,100,25),(100,100,100), 
            lambda x=-1:self.music.switch_track(x), text='Previous', **button_config
        )
        
    def additional_event_handler(self, event):
        self.next_button.check_event(event)
        self.prev_button.check_event(event)
    
    def additional_render(self):
        self.next_button.render(prepare.SCREEN)
        self.prev_button.render(prepare.SCREEN)
        prepare.SCREEN.blit(self.music_select_label, self.music_select_label_rect)

        
