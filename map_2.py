import pygame as pg
from settings import *
from os import path
from tilemap import Map
from player import *
from obstacles import *
class load_map2:
    def __init__(self):
        # self.all_sprites = pg.sprite.Group()
        # self.walls = pg.sprite.Group()
        # self.teleports = pg.sprite.Group()
        for row, tiles in enumerate(self.map2.data):
            for col, tile in enumerate(tiles):
                if tile == '*':
                        Wall(self, col, row)
                if tile == 'U':
                        self.player = Player(self, col, row) 
  
                        