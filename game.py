#!/usr/bin/env python

import pygame as pg
from data.main import main
from data.tools import Error

if __name__ == '__main__':
    try:
        main()
    except:
        Error.create_report()
    pg.quit()

