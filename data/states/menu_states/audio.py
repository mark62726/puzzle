
import pygame as pg
from . import menus

class Audio(menus.Menus):
    def __init__(self):
        menus.Menus.__init__(self)
        self.options = ['Volume','Sound','Back']
        self.next_list = ['DISABLED','DISABLED','MENU']
        self.title_text = 'Audio'
        self.pre_render_options()
        self.setup_title()
    

        
