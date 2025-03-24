from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)
                
        s_horiz_tiles = len(self.data[0])
        s_vert_tiles = len(self.data)
        
        self.tilewidth = s_horiz_tiles * TILESIZE
        self.tileheight = s_vert_tiles * TILESIZE
        
        # read tilemap[x][y] trough txt