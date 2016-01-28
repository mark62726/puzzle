
import pygame as pg
from . import menus
from ... import prepare, tools

class Menu(menus.Menus):
    def __init__(self):
        menus.Menus.__init__(self)
        self.options = ['Play', 'Options', 'Credits', 'Quit']
        self.next_list = ['LEVEL1','OPTIONS', 'CREDITS']
        self.title_text = 'Puzzle'
        self.pre_render_options()
        self.setup_title()
