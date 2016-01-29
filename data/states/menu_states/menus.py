import pygame as pg
from ... import prepare, tools
from .. import state

class Menus(state.State):
    '''
    Super class for all menu states 
    '''
    def __init__(self):
        state.State.__init__(self)
        self.screen_rect = pg.Rect((0, 0), prepare.RENDER_SIZE)
        self.bg_orig = prepare.GFX['old_paper']
        self.setup_bg(self.screen_rect)
        self.selected_color = (235,0,0)
        self.deselected_color = (15,15,15)
        self.title_text = None
        self.from_bottom = 200
        self.spacer = 75
        self.selected_index = 0
        self.mouse_pos = (0,0)
        
    def setup_bg(self, screen_rect):
        self.bg = pg.transform.smoothscale(self.bg_orig, screen_rect.size)
        
    def setup_title(self):
        self.title, self.title_rect = self.make_text(
            self.title_text, (75,75,75), (self.screen_rect.centerx, 75), 150, prepare.FONTS['3rdman'])
        
    def pre_render_options(self):
        font_deselect = pg.font.Font(prepare.FONTS['magazine'], 75)
        font_selected = pg.font.Font(prepare.FONTS['magazine'], 100)

        rendered_msg = {"des":[],"sel":[]}
        for option in self.options:
            d_rend = font_deselect.render(option, 1, self.deselected_color)
            d_rect = d_rend.get_rect()
            s_rend = font_selected.render(option, 1, self.selected_color)
            s_rect = s_rend.get_rect()
            rendered_msg["des"].append((d_rend,d_rect))
            rendered_msg["sel"].append((s_rend,s_rect))
        self.rendered = rendered_msg
        
    def mouse_menu_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for i,opt in enumerate(self.rendered["des"]):
                if opt[1].collidepoint(self.mouse_pos):
                    self.selected_index = i
                    self.select_option(i)
                    break
                    
    def additional_event_handler(self, event):
        pass

    def get_event(self, event, keys):
        self.additional_event_handler(event)
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYDOWN:
            if event.key in [pg.K_UP, pg.K_w]:
                self.change_selected_option(-1)
            elif event.key in [pg.K_DOWN, pg.K_s]:
                self.change_selected_option(1)
                
            elif event.key == pg.K_RETURN:
                self.select_option(self.selected_index)
        self.mouse_menu_click(event)
        self.music.get_event(event)

    def additional_update(self):
        pass
        
    def update(self, now, keys, scale):
        self.mouse_pos = tools.scaled_mouse_pos(scale)
        self.additional_update()
        pg.mouse.set_visible(True)
        #self.mouse_hover_sound()
        self.change_selected_option()
        
    def additional_render(self, surface):
        pass

    def render(self, surface):
        surface.blit(self.bg,(0,0))
        surface.blit(self.title,self.title_rect)
        for i,opt in enumerate(self.rendered["des"]):
            opt[1].center = (surface.get_rect().centerx, self.from_bottom+i*self.spacer)
            if i == self.selected_index:
                rend_img,rend_rect = self.rendered["sel"][i]
                rend_rect.center = opt[1].center
                surface.blit(rend_img,rend_rect)
            else:
                surface.blit(opt[0],opt[1])
        self.additional_render(surface)
                
    def select_option(self, i):
        '''select menu option via keys or mouse'''
        if i == len(self.next_list):
            self.quit = True
        else:
            #self.button_sound.sound.play()
            self.next = self.next_list[i]
            self.done = True
            self.selected_index = 0

    def change_selected_option(self, op=0):
        '''change highlighted menu option'''
        for i,opt in enumerate(self.rendered["des"]):
            if opt[1].collidepoint(self.mouse_pos):
                self.selected_index = i

        if op:
            self.selected_index += op
            max_ind = len(self.rendered['des'])-1
            if self.selected_index < 0:
                self.selected_index = max_ind
            elif self.selected_index > max_ind:
                self.selected_index = 0
            #self.button_hover.sound.play()

    def cleanup(self):
        pass
        
    def entry(self):
        pass
        
