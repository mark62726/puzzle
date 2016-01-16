
import os
import pygame as pg
from .states.menu_states import menu, options, audio, credits
from .states import splash, game
from . import prepare


class Control():
    def __init__(self):
        self.clock = pg.time.Clock()
        self.keys = None
        self.done = False
        self.state_dict = {
            "MENU"      : menu.Menu(),
            "SPLASH"    : splash.Splash(),
            'GAME'      : game.Game(),
            'OPTIONS'   : options.Options(),
            'AUDIO'     : audio.Audio(),
            'AUDIO'     : audio.Audio(),
            'CREDITS'   : credits.Credits(),
            'DISABLED'  :None
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
            if not self.state.next == 'DISABLED':
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


