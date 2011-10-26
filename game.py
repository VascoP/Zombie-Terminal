### IMPORTS
import os, sys
import libtcodpy as libtcod



### CLASSES

class Thing(object):
    def __init__(self, x, y, char, color, player=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

        self.player = player
        if self.player:
            self.player.owner = self

    def move(self, dx, dy):
        if not world.region[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

        if self.x >= SCREEN_WIDTH or self.x < 0:
            self.x -= dx
        if self.y >= SCREEN_HEIGHT or self.y < 0:
            self.y -=dy

    def draw(self):
        libtcod.console_put_char_ex(con, self.x, self.y, self.char, libtcod.white, libtcod.BKGND_NONE)

    def clear(self):
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_SET)


class World(object):    
    def __init__(self):
        self.region = [[ Tile(blocked=False) for y in range(MAP_HEIGHT) ] for x in range(MAP_WIDTH) ]
        
        mapfile = open("map.data", "r")
        for j, line in enumerate(mapfile):
            for i, char in enumerate(line):
                if char == '.':
                    self.region[i][j].blocked = True
                    self.region[i][j].block_sight = True

    def draw(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                wall = world.region[x][y].block_sight
                if wall:
                    libtcod.console_set_back(con, x, y, WALL, libtcod.BKGND_SET )
                else:
                    libtcod.console_set_back(con, x, y, GROUND, libtcod.BKGND_SET )
        

class Tile(object):
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight


class Game(object):    
    def __init__(self):
        self.play()

    def handle_input(self):
        key = libtcod.console_wait_for_keypress(True)

        if key.vk == libtcod.KEY_UP:
            player.move(0, -1)
        elif key.vk == libtcod.KEY_DOWN:
            player.move(0, 1)
        elif key.vk == libtcod.KEY_LEFT:
            player.move(-1, 0)
        elif key.vk == libtcod.KEY_RIGHT:
            player.move(1, 0)
        elif key.vk == libtcod.KEY_ESCAPE:
            return True

    def logic(self):
        pass

    def render(self):
        world.draw()
        
        for thing in objects:
            thing.draw()
            
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()

    def cleanup(self):
        pass
    
    def play(self):
        # GAME LOOP
        while not libtcod.console_is_window_closed():
            #display objects on the screen
            self.render()
            #clear objects before next update (avoid trails)
            for thing in objects:
                thing.clear()
            #get player input
            quit = self.handle_input()
            if  quit == True:
                break

            #aditional loop logic before new screen update
            self.logic()

        #player has quit the game
        self.cleanup()



### FUNCTIONS



            
### GLOBAL VARIABLES

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

WALL = libtcod.white
GROUND = libtcod.black

PLAYER_CHAR = "@"
PLAYER_COLOR = libtcod.white

### INITIALIZATIONS

#screen
libtcod.console_set_custom_font("consolas12x12_gs_tc.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, "Zombie Terminal", False)

#panels
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#objects
world = World()
player = Thing(1, 1, PLAYER_CHAR, PLAYER_COLOR)

objects = [player]



### GAME
game = Game();

#print "You turn on the TV and you watch the news. There were 12 more deaths since yesterday. And they say the vaccine had some side effects."
#print "Nobody should leave their homes so they don't get infected. Almost everyone that was infected died within 5 hours."
#print "They are doing everything in their power to stop this from spreading."
#print "You are tired from work anyway, and you could use these extra hours to get some sleep."
#print "You go to bed..."
#print "You wake up with siren noises coming from the street. You can also hear people screaming"
#menu = OptionsMenu("What do you want to do?", ["Kill yourself", "Go back to sleep", "Watch the street from the window", "Go outside"])
#menu.show()

