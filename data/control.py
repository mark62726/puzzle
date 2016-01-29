
import os
import pygame as pg
from . import prepare
import setup_dict



class Control():
    def __init__(self):
        
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.render_size = prepare.RENDER_SIZE
        self.render_surf = pg.Surface(self.render_size).convert()
        self.resolutions = prepare.RESOLUTIONS
        self.set_scale()
            
        self.clock = pg.time.Clock()
        self.keys = None
        self.done = False
        self.state_dict = setup_dict.DICT
        self.state_name = prepare.STARTING_STATE
        self.state = self.state_dict[self.state_name]
        
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type in (pg.KEYDOWN,pg.KEYUP):
                self.keys = pg.key.get_pressed()
                if event.key == pg.K_PRINT:
                    #Print screen for full render-sized screencaps.
                    pg.image.save(self.render_surf, "screenshot.png")
            elif event.type == pg.VIDEORESIZE:
                self.on_resize(event.size)
                pg.event.clear(pg.VIDEORESIZE)
            self.state.get_event(event, self.keys)

    def change_state(self, now):
        if self.state.done:
            if not self.state.next in ['DISABLED', 'TOGGLE']:
                self.state.cleanup()
                self.state_name = self.state.next
                self.state.done = False
                self.state = self.state_dict[self.state_name]
                self.state.timer = now
                self.state.entry()

    def run(self):
        while not self.done:
            if self.state.quit:
                self.done = True
            now = pg.time.get_ticks()
            self.event_loop()
            self.render()
            self.change_state(now)
            delta_time = self.clock.tick(prepare.FPS)
            self.state.update(now, self.keys, self.scale)
            self.state.render(self.render_surf)
            pg.display.update()
            
    def render(self):
        """
        Scale the render surface if not the same size as the display surface.
        The render surface is then drawn to the screen.
        """
        if self.render_size != self.screen_rect.size:
            scale_args = (self.render_surf, self.screen_rect.size, self.screen)
            pg.transform.smoothscale(*scale_args)
        else:
            self.screen.blit(self.render_surf, (0, 0))

    def on_resize(self, size):
        """
        If the user resized the window, change to the next available
        resolution depending on if scaled up or scaled down.
        """
        if size == self.screen_rect.size:
            return
        res_index = self.resolutions.index(self.screen_rect.size)
        adjust = 1 if size > self.screen_rect.size else -1
        if 0 <= res_index+adjust < len(self.resolutions):
            new_size = self.resolutions[res_index+adjust]
        else:
            new_size = self.screen_rect.size
        self.screen = pg.display.set_mode(new_size, pg.RESIZABLE)
        self.screen_rect.size = new_size
        self.set_scale()

    def set_scale(self):
        """
        Reset the ratio of render size to window size.
        Used to make sure that mouse clicks are accurate on all resolutions.
        """
        w_ratio = self.render_size[0]/float(self.screen_rect.w)
        h_ratio = self.render_size[1]/float(self.screen_rect.h)
        self.scale = (w_ratio, h_ratio)
