
import pygame as pg
from . import menus

class Credits(menus.Menus):
    def __init__(self):
        menus.Menus.__init__(self)
        self.options = ['']
        self.next_list = ['MENU']
        self.title_text = 'Credits'
        self.pre_render_options()
        self.setup_title()
        self.from_bottom = 500
    
    def additional_event_handler(self, event):
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            #select hidden back button
            self.select_option(0)
        
        
