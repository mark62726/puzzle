

import pygame as pg
import os
import shutil
import random
import sys
import json
import argparse
import traceback
from time import gmtime, strftime
import platform
        
class DB:
    dirname = 'save'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    path = os.path.join(dirname, 'database{}'.format(sys.version.split()[0]))
    @staticmethod
    def exists():
        return os.path.exists(DB.path)
    @staticmethod
    def load():
        data = open(DB.path)
        obj = json.load(data)
        data.close()
        return obj
    @staticmethod
    def save(obj):
        f = open(DB.path, 'w')
        f.write(json.dumps(obj))
        f.close()
        
class Error:
    @staticmethod
    def create_report():
        open('error.log','w').close()
        
        date = 'DATE: {}'.format(strftime("%m-%d-%Y %H:%M:%S", gmtime()))
        os = 'OS: {}'.format(platform.platform())
        s = traceback.format_exc()
        f = open('error.log', 'r+')
        content = f.read()
        f.seek(0, 0)
        f.write('{}\n'.format(date))
        f.write('{}\n'.format(os))
        f.write('{}\n'.format(s))
        f.write(content)
        f.close()
        print(s)

def clean_files():
    '''remove all pyc files and __pycache__ direcetories in subdirectory'''
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if dir == '__pycache__':
                path = os.path.join(root, dir)
                print('removing {}'.format(os.path.abspath(path)))
                shutil.rmtree(path)
        for name in files:
            if name.endswith('.pyc'):
                path = os.path.join(root, name)
                print('removing {}'.format(os.path.abspath(path)))
                os.remove(path)
    
def strip_from_sheet(sheet, start, size, columns, rows=1):
    """
    Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows.
    """
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames


def strip_coords_from_sheet(sheet, coords, size):
    """Strip specific coordinates from a sprite sheet."""
    frames = []
    for coord in coords:
        location = (coord[0]*size[0], coord[1]*size[1])
        frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames


def get_cell_coordinates(rect, point, size):
    """Find the cell of size, within rect, that point occupies."""
    cell = [None, None]
    point = (point[0]-rect.x, point[1]-rect.y)
    cell[0] = (point[0]//size[0])*size[0]
    cell[1] = (point[1]//size[1])*size[1]
    return tuple(cell)


def get_cli_args(caption, win_pos, start_size):
    """
    Modify prepare module globals based on command line arguments,
    quickly force settings for debugging.
    """
    parser = argparse.ArgumentParser(description='{} Arguments'.format(caption))
    parser.add_argument('-c','--center', action='store_false',
        help='position starting window at (0,0), sets SDL_VIDEO_CENTERED to false')
    parser.add_argument('-w','--winpos', nargs=2, default=win_pos, metavar=('X', 'Y'),
        help='position starting window at (X,Y), default is (0,0)')
    parser.add_argument('-W' , '--winsize', nargs=2, default=start_size, metavar=('WIDTH', 'HEIGHT'),
        help='set window size to WIDTH HEIGHT, defualt is {}'.format(start_size))
    parser.add_argument('-f' , '--fullscreen', action='store_true',
        help='start in fullscreen')
    parser.add_argument('-m' , '--music_off', action='store_true',
        help='start with no music')
    parser.add_argument('-d', '--debug', action='store_true',
        help='run game in debug mode')

    args = vars(parser.parse_args())
    #check each condition
    if not args['center'] or (args['winpos'] != win_pos): #if -c or -w options
        args['center'] = False
    if args['winsize'] != start_size: # if screen size is different
        args['resizable'] = False
    if args['fullscreen']:
        args['center'] = False
        args['resizable'] = False
    return args
    
class Music:
    '''separate music handler from prepare module'''
    def __init__(self, volume):
        self.path = os.path.join('resources', 'music')
        self.setup(volume)
        
    def setup(self, volume):
        self.track_end = pg.USEREVENT+1
        self.tracks = []
        self.track = 0
        for track in os.listdir(self.path):
            self.tracks.append(os.path.join(self.path, track))
        random.shuffle(self.tracks)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.set_endevent(self.track_end)
        pg.mixer.music.load(self.tracks[self.track])
        
    def get_event(self, event):
        if event.type == self.track_end:
            self.switch_track()
            
    def switch_track(self, direction=1):
            self.track = (self.track+direction) % len(self.tracks)
            pg.mixer.music.load(self.tracks[self.track]) 
            pg.mixer.music.play()
            
    def track_name(self, track_path):
        return os.path.splitext(os.path.split(track_path)[1])[0].replace('_', ' ').title()

    
### Resource loading functions.
def load_all_gfx(directory,colorkey=(0,0,0),accept=(".png",".jpg",".bmp")):
    """
    Load all graphics with extensions in the accept argument.  If alpha
    transparency is found in the image the image will be converted using
    convert_alpha().  If no alpha transparency is detected image will be
    converted using convert() and colorkey will be set to colorkey.
    """
    graphics = {}
    for pic in os.listdir(directory):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics

def load_all_music(directory, accept=(".wav", ".mp3", ".ogg", ".mdi")):
    """
    Create a dictionary of paths to music files in given directory
    if their extensions are in accept.
    """
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs

def load_all_fonts(directory, accept=(".ttf",)):
    """
    Create a dictionary of paths to font files in given directory
    if their extensions are in accept.
    """
    return load_all_music(directory, accept)

def load_all_movies(directory, accept=(".mpg",)):
    """
    Create a dictionary of paths to movie files in given directory
    if their extensions are in accept.
    """
    return load_all_music(directory, accept)

def load_all_sfx(directory, accept=(".wav", ".mp3", ".ogg", ".mdi")):
    """
    Load all sfx of extensions found in accept.  Unfortunately it is
    common to need to set sfx volume on a one-by-one basis.  This must be done
    manually if necessary in the setup module.
    """
    effects = {}
    for fx in os.listdir(directory):
        name,ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects
    
class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """
    
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.

    surface = pg.Surface(rect.size).convert()
    #surface.fill(0)
    #surface.set_alpha(0)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException("Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]

    return surface
