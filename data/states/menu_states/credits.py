
import pygame as pg
from . import menus
from ... import prepare
from ...components import credit_surf

class Credits(menus.Menus):
    def __init__(self):
        menus.Menus.__init__(self)
        self.options = ['']
        self.next_list = ['MENU']
        self.title_text = 'Credits'
        self.pre_render_options()
        self.setup_title()
        self.from_bottom = 500
        
        self.credit = {
            'Developers'    :['metulburr'],
            'Artists'       :[],
            'Assets'        :['bensound.com'],
            'Software'      :['Python', 'Pygame'],
        }
        self.make_credit_surf()
    
    def make_credit_surf(self):
        
        self.credit_surf = credit_surf.CreditSurf((2000,2000), self.screen_rect.bottomleft)
        title_spacer = 100
        self.credit_screen = pg.Surface((2000,2000)).convert()
        for i,(k,v) in enumerate(self.credit.items(),1):
            image, rect = self.make_text(
                k, (75,75,75), self.screen_rect.midbottom, 75, prepare.FONTS['3rdman'])
            #self.credit_surf.image.blit(image,(0,1900))
            
    
    def additional_event_handler(self, event):
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            #select hidden back button
            self.select_option(0)
            
    def additional_render(self, surface):
        pass#self.credit_surf.render(surface)
        
    def additional_update(self):
        pass
        
        
