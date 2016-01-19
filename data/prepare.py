
from . import tools
import pygame as pg
import os

FPS = 60
CAPTION = 'Puzzle'
#START_SIZE = (800,600)
START_SIZE = (928, 696)
RENDER_SIZE = (1400, 1050)
RESOLUTIONS = [(600,400),(800, 600), (928, 696), (1280, 960), (1400, 1050)]
WIN_POS = (0,0)
ARGS = tools.get_cli_args(CAPTION, WIN_POS, START_SIZE)
DEBUG = bool(ARGS['debug'])

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

MONITOR_SIZE = (pg.display.Info().current_w, pg.display.Info().current_h)

#set position of window
if ARGS['center']:
    os.environ['SDL_VIDEO_CENTERED'] = "True"
else:
    os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(*ARGS['winpos'])
    
pg.display.set_caption(CAPTION)

#change size of window
if ARGS['winsize']:
    START_SIZE = (
        int(ARGS['winsize'][0]), 
        int(ARGS['winsize'][1]) 
    )
if ARGS['fullscreen']:
    SCREEN = pg.display.set_mode(START_SIZE, pg.FULLSCREEN)
else:
    SCREEN = pg.display.set_mode(START_SIZE, pg.RESIZABLE)
    pg.event.clear(pg.VIDEORESIZE)

#Default screen_rect for states constructors
#SCREEN_RECT = SCREEN.get_rect()
    
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
SFX   = tools.load_all_sfx(os.path.join("resources", "sound"))
GFX   = tools.load_all_gfx(os.path.join("resources", "graphics"))

#set starting music volume
if ARGS['music_off']:
    MUSIC_VOLUME = 0.0
else:
    MUSIC_VOLUME = .3
