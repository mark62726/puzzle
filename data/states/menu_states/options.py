
import pygame as pg
from . import menus

class Options(menus.Menus):
    def __init__(self):
        menus.Menus.__init__(self)
        self.options = ['Audio', 'Video','Back']
        self.next_list = ['AUDIO','DISABLED','MENU']
        self.title_text = 'Options'
        self.pre_render_options()
        self.setup_title()
    

        
