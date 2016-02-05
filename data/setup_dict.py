from .states.menu_states import menu, options, audio, credits
from .states import splash, game
from .levels import level1, level2, level3

DICT = {
    "MENU"      : menu.Menu(),
    "SPLASH"    : splash.Splash(),
    'GAME'      : game.Game(),
    'OPTIONS'   : options.Options(),
    'AUDIO'     : audio.Audio(),
    'CREDITS'   : credits.Credits(),
    'LEVEL1'    : level1.Level1(),
    'LEVEL2'    : level2.Level2(),
    'LEVEL3'    : level3.Level3(),
    'DISABLED'  :None
}
