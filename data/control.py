
import os
import pygame as pg
from .states import splash, game
from . import prepare


class Control():
    def __init__(self):
        self.clock = pg.time.Clock()
        self.keys = None
        self.done = False
        self.state_dict = {
        #    "MENU"     : menu.Menu(self.screen_rect),
            "SPLASH"   : splash.Splash(),
        #    'TITLE'    : title.Title(self.screen_rect),
            'GAME'     : game.Game(),
        #    'OPTIONS'  : options.Options(self.screen_rect, self.default_screensize, self.fullscreen),
        }

        self.state_name = "SPLASH"
        self.state = self.state_dict[self.state_name]
            
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type in (pg.KEYDOWN,pg.KEYUP):
                self.keys = pg.key.get_pressed()
            self.state.get_event(event, self.keys)

    def change_state(self, now):
        if self.state.done:
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
            self.change_state(now)
            delta_time = self.clock.tick(prepare.FPS)
            self.state.update(now, self.keys)
            self.state.render()
            pg.display.update()


