from .states.menu_states import menu, options, audio, credits
from .states import splash, game
import importlib
import os

d = {}

listed = os.listdir('data/levels')
package = 'data.levels.'
for f in listed:
    f = os.path.splitext(f)[0]
    if f.endswith('.py') or not f.startswith('__'):
        module_name = os.path.splitext(f)[0]
        module = importlib.import_module(package + f)
        klass = getattr(module, module_name.title())
        d.update(
            {'{}'.format(module_name.upper()) : klass()},
        )

DICT = {
    "MENU"      : menu.Menu(),
    "SPLASH"    : splash.Splash(),
    'GAME'      : game.Game(),
    'OPTIONS'   : options.Options(),
    'AUDIO'     : audio.Audio(),
    'CREDITS'   : credits.Credits(),
    'DISABLED'  :None
}
DICT.update(d)
