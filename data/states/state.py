import pygame as pg


class State:
    '''
    Super class for all games states 
    '''
    def __init__(self):
        self.quit = False #quit game
        self.done = False #quit state
        self.timer = 0.0
        
