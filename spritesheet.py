import pygame as pg

class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert_alpha()

    def get_image(self, frame):
        image = self.spritesheet.subsurface(pg.Rect(frame)) 
        return image