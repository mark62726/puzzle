
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
        self.update_buttons()
        self.setup_music_select_label(self.screen_rect)
        self.update_labels(self.screen_rect)
        
        
    def update_buttons(self):
        button_config = {
            "hover_color"        : (150,150,150),
            "clicked_color"      : (255,255,255),
            "clicked_font_color" : (0,0,0),
            "hover_font_color"   : (0,0,0),
            'font'               : pg.font.Font(prepare.FONTS['impact'], 15)
        }
        self.next_button = button.Button((825,150,100,25),(100,100,100), 
            self.music.switch_track, text='Next', **button_config
        )
        self.prev_button = button.Button((475,150,100,25),(100,100,100), 
            lambda x=-1:self.music.switch_track(x), text='Previous', **button_config
        )
        
        self.vol_up_button = button.Button((825,225,100,25),(100,100,100), 
            self.music_modify, text='+', **button_config
        )
        self.vol_down_button = button.Button((475,225,100,25),(100,100,100), 
            lambda x=-1:self.music_modify(-.1), text='-', **button_config
        )
        
    def setup_music_select_label(self, screen_rect):
        self.music_select_label, self.music_select_label_rect = self.make_text(
            'Switch Music Track', (0,0,0), (screen_rect.centerx, 162), 25, prepare.FONTS['impact'])
        
    def update_labels(self, screen_rect):
        if self.vol_up_button.ever_clicked or self.vol_down_button.ever_clicked:
            volume_num = int(self.music_volume*10)
        else:
            volume_num = ''
        self.volume_select_label, self.volume_select_label_rect = self.make_text(
            'Music Volume {}'.format(
                volume_num), 
            (0,0,0), (screen_rect.centerx, 237), 25, prepare.FONTS['impact'])
        
        if self.next_button.ever_clicked or self.prev_button.ever_clicked:
            song_name = self.music.tracks[self.music.track]
        else:
            song_name = ''
        self.music_song_label, self.music_song_label_rect = self.make_text(
            '{}'.format(
                self.music.track_name(song_name)), 
            (0,0,0), (screen_rect.centerx, 199), 25, prepare.FONTS['impact'])
    
    def music_modify(self, amount=.1):
        self.music_volume += amount
        if self.music_volume > .9:
            self.music_volume = 1.0
        elif self.music_volume < .1:
            self.music_volume = 0.0
        pg.mixer.music.set_volume(self.music_volume)
        
    def additional_update(self):
        self.update_labels(self.screen_rect)
        self.next_button.update(self.mouse_pos)
        self.prev_button.update(self.mouse_pos)
        self.vol_up_button.update(self.mouse_pos)
        self.vol_down_button.update(self.mouse_pos)
    
    def additional_event_handler(self, event):
        self.next_button.check_event(event)
        self.prev_button.check_event(event)
        self.vol_up_button.check_event(event)
        self.vol_down_button.check_event(event)
    
    def additional_render(self, surface):
        self.next_button.render(surface)
        self.prev_button.render(surface)
        self.vol_up_button.render(surface)
        self.vol_down_button.render(surface)
        surface.blit(self.music_select_label, self.music_select_label_rect)
        surface.blit(self.volume_select_label, self.volume_select_label_rect)
        surface.blit(self.music_song_label, self.music_song_label_rect)

        
