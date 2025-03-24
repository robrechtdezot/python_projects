import pygame as pg
from settings import *
from os import path
from spritesheet import SpriteSheet
from tilemap import Map
from obstacles import *
from map_2 import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.load()
        
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def collision_with_walls(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if (self.x + dx) == wall.x and (self.y + dy) == wall.y:
                return True
        return False
    
    def collision_with_teleport(self, dx = 0, dy = 0):
        for teleport in self.game.teleport:
            if (self.x + dx) == teleport.x and (self.y + dy) == teleport.y:
                return True
        return False
    
    def load(self):
        # spritesheet = SpriteSheet(path.join(self.screen.game.img_dir, 'player_spritesheet.png'))
        # standing_frames = (7, 47, 19, 45)
        # self.image = spritesheet.get_image(standing_frames)
        pass
    def move(self, dx = 0, dy = 0):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group() 
        self.teleports = pg.sprite.Group()
        if not self.collision_with_walls(dx, dy): 
                self.x += dx
                self.y += dy
        
                          
    def update(self):
            self.rect.x = self.x*TILESIZE
            self.rect.y = self.y*TILESIZE
               