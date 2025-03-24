import pygame as pg
from settings import *
import sys

from tilemap import Map
from os import path
from player import Player
from obstacles import *

class Game:
    def __init__(self):
        '''setup pygame'''
        # pg.init()
        # pg.mixer.init()
        # self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        # pg.display.set_caption(settings.TITLE)
        # self.clock = pg.time.Clock()
        # self.running = True
        
        # # declare variables that are used in the game
        # self.all_sprites = None
        # self.player = None
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        
        self.load()
        pg.key.set_repeat(500, 10)
        self.new()
    def new(self): 
        '''start a new game'''
        self.all_sprites = pg.sprite.Group()
        #create sprites
        self.player = Player(self, 0, 0)   
    def load(self):
        '''load game assets'''
        game_dir = path.dirname(__file__)
        self.map = Map(path.join(game_dir, 'map.txt'))
        self.map2 = Map(path.join(game_dir, 'map2.txt'))
        
        # self.player = Player()
        # self.all_sprites.add(self.player)
       
    def new_instance(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.teleports = pg.sprite.Group()
        
        
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '*':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'T':
                    Teleport(self, col, row)
        if Player.collision_with_teleport(self):        
            self.load_map2()
                    
        
    def load_map2(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group() 
        for row, tiles in enumerate(self.map2.data):
            for col, tile in enumerate(tiles):
                if tile == '*':
                        Wall(self, col, row)
                if tile == 'U':
                        self.player = Player(self, col, row)                                
        
                
                    
                    
        
        # self.player = Player(self, 1, 1)
        # for x in range(0, 17):
        #     Wall(self, x, 0)
        #     Wall(self, x, 11)
        #     Wall(self, x, 10)
       
        # for y in range(0, 12):
        #     Wall(self, 0, y)
        #     Wall(self, 19, y)
        
            
        
        
    def run(self):
        '''game loop'''
        self.playing = True 
        while self.playing:
            # control FPS
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()
    
    def quit(self):
        pg.quit()
        sys.exit()
        
    def update(self):
        '''game update'''
        self.all_sprites.update()
    
    def events(self):
        '''game events'''
        for e in pg.event.get():
            # if window closes 
            if e.type == pg.QUIT:
                self.quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    self.player.move(dx = -1)
                if e.key == pg.K_RIGHT:
                    self.player.move(dx = 1)
                if e.key == pg.K_UP:
                    self.player.move(dy=-1)
                if e.key == pg.K_DOWN:
                    self.player.move(dy=1)
                if e.key == pg.K_ESCAPE:
                    self.playing = False
                # if self.playing:
                #     self.playing = False 
                # self.running = False
    
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, BLACK, (0, y), (WIDTH, y))
        
    
        
    
    def draw(self):
        '''game draw'''
        self.screen.fill(TAN)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        
        pg.display.flip()
    
    # def show_start_screen(self):
    #     '''start screen'''
        
    # def show_go_screen(self):    
    #     '''game over screen'''  
         
        
# def game():
#     '''method for creating game instance'''
#     g = Main()
#     g.show_start_screen()
#     while g.running:
#         g.new()
#         g.show_go_screen()
#     pg.quit()

if __name__ == '__main__':
     g = Game()
     while True:         
         g.new_instance()
         
         g.run()
         
         
         