### IMPORTS
import os, sys
import libtcodpy as libtcod


### GLOBAL VARIABLES
MAP_WIDTH = 80
MAP_HEIGHT = 45

WALL = libtcod.white
GROUND = libtcod.black


### CLASSES
class Thing(object):
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
        if self.x >= MAP_WIDTH or self.x < 0:
            self.x -= dx
        if self.y >= MAP_HEIGHT or self.y < 0:
            self.y -=dy

    def draw(self):
        libtcod.console_put_char_ex(con, self.x, self.y, self.char, self.color, libtcod.BKGND_NONE)

    def clear(self):
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)


class Tile(object):
    def __init__(self, drawn):
        self.drawn = drawn


class World(object):
    def __init__(self):
        self.region = [[ Tile(drawn=False) for y in range(MAP_HEIGHT) ] for x in range(MAP_WIDTH) ]
        self.load()

    def action(self):
        if self.region[cursor.x][cursor.y].drawn:
            self.region[cursor.x][cursor.y].drawn = False
        else:
            self.region[cursor.x][cursor.y].drawn = True

    def draw(self):
        if self.region[cursor.x][cursor.y].drawn:
            libtcod.console_set_back(con, cursor.x, cursor.y, WALL, libtcod.BKGND_SET)
        else:
            libtcod.console_set_back(con, cursor.x, cursor.y, GROUND, libtcod.BKGND_SET)

    def load(self):
        for j, line in enumerate(mapfile):
            for i, char in enumerate(line):
                if char == '#':
                    self.region[i][j].drawn = True
                    libtcod.console_set_back(con, i, j, WALL, libtcod.BKGND_SET)
        mapfile.close()

    def save(self):
        mapfile = open(sys.argv[1], "w")
        for i in range(0, MAP_HEIGHT):
            for j, line in enumerate(self.region):
                if line[i].drawn == True:
                    mapfile.write('#')
                else:
                    mapfile.write(' ')
            mapfile.write('\n')
        

### INITIALIZATIONS
if len(sys.argv) > 1:
    try:
        mapfile = open(sys.argv[1], "r")
    except:
        mapfile = open(sys.argv[1], "w+")
else:
    print "No input file specified"
    exit(0)

libtcod.console_set_custom_font("consolas12x12_gs_tc.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(MAP_WIDTH, MAP_HEIGHT, "Map Generator", False)
con = libtcod.console_new(MAP_WIDTH, MAP_HEIGHT)

world = World()
cursor = Thing(MAP_WIDTH/2, MAP_HEIGHT/2, libtcod.CHAR_CROSS, libtcod.green)

while not libtcod.console_is_window_closed():
    cursor.draw()
    world.draw()

    libtcod.console_blit(con, 0, 0, MAP_WIDTH, MAP_HEIGHT, 0, 0, 0)
    libtcod.console_flush()

    cursor.clear()
    
    key = libtcod.console_wait_for_keypress(True)

    if key.vk == libtcod.KEY_UP:
        cursor.move(0, -1)
    elif key.vk == libtcod.KEY_DOWN:
        cursor.move(0, 1)
    elif key.vk == libtcod.KEY_LEFT:
        cursor.move(-1, 0)
    elif key.vk == libtcod.KEY_RIGHT:
        cursor.move(1, 0)
    elif key.vk == libtcod.KEY_ENTER or key.vk == libtcod.KEY_SPACE:
        world.action()
    elif key.vk == libtcod.KEY_ESCAPE or key.c == ord('q'):
        world.save()
        mapfile.close()
        break





