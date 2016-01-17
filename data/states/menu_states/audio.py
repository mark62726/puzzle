
import pygame as pg
from . import menus
from ...toolbox import button
from ... import prepare
   
class Audio(menus.Menus):
    def __init__(self):
        menus.Menus.__init__(self)
        self.options = ['Back']
        self.next_list = ['MENU']
        self.title_text = 'Audio'
        self.pre_render_options()
        self.setup_title()
        self.from_bottom = 300
        self.music_select_label, self.music_select_label_rect = self.make_text(
            'Switch Music Track', (0,0,0), (prepare.SCREEN_RECT.centerx, 162), 15, prepare.FONTS['impact'])
        #self.update_labels()
        
        button_config = {
            "hover_color"        : (150,150,150),
            "clicked_color"      : (255,255,255),
            "clicked_font_color" : (0,0,0),
            "hover_font_color"   : (0,0,0),
            'font'               : pg.font.Font(prepare.FONTS['impact'], 15)
        }
        self.next_button = button.Button((475,150,100,25),(100,100,100), 
            self.music.switch_track, text='Next', **button_config
        )
        self.prev_button = button.Button((225,150,100,25),(100,100,100), 
            lambda x=-1:self.music.switch_track(x), text='Previous', **button_config
        )
        
        self.vol_up_button = button.Button((475,200,100,25),(100,100,100), 
            self.music_modify, text='+', **button_config
        )
        self.vol_down_button = button.Button((225,200,100,25),(100,100,100), 
            lambda x=-1:self.music_modify(-.1), text='-', **button_config
        )
        
    def update_labels(self):
        self.volume_select_label, self.volume_select_label_rect = self.make_text(
            'Music Volume {}'.format(int(self.music_volume*10)), (0,0,0), (prepare.SCREEN_RECT.centerx, 212), 15, prepare.FONTS['impact'])
            
        self.music_song_label, self.music_song_label_rect = self.make_text(
            '{}'.format(
                self.music.track_name(self.music.tracks[self.music.track])), 
            (0,0,0), (prepare.SCREEN_RECT.centerx, 187), 15, prepare.FONTS['impact'])
    
    def music_modify(self, amount=.1):
        self.music_volume += amount
        if self.music_volume > .9:
            self.music_volume = 1.0
        elif self.music_volume < .1:
            self.music_volume = 0.0
        pg.mixer.music.set_volume(self.music_volume)
        
    def additional_update(self):
        self.update_labels()
        
    def additional_event_handler(self, event):
        self.next_button.check_event(event)
        self.prev_button.check_event(event)
        self.vol_up_button.check_event(event)
        self.vol_down_button.check_event(event)
    
    def additional_render(self):
        self.next_button.render(prepare.SCREEN)
        self.prev_button.render(prepare.SCREEN)
        self.vol_up_button.render(prepare.SCREEN)
        self.vol_down_button.render(prepare.SCREEN)
        prepare.SCREEN.blit(self.music_select_label, self.music_select_label_rect)
        prepare.SCREEN.blit(self.volume_select_label, self.volume_select_label_rect)
        if self.next_button.ever_clicked or self.prev_button.ever_clicked:
            prepare.SCREEN.blit(self.music_song_label, self.music_song_label_rect)

        
