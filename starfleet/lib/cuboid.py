

import re
from copy import deepcopy
import ipdb
from cStringIO import StringIO
from operator import itemgetter, attrgetter, methodcaller

class Cuboid:

    # trust me. this is sweet..
    z_map = {c:(i+1)*-1 for i,c in enumerate([chr(c) for c in range(ord('a'), ord('z')+1)] + [chr(c) for c in range(ord('A'), ord('Z')+1)])}
        
    eol = "\n"
    empty_space = "."
    missed_mine = "*"
    
    def __init__(self, string_input, decent_level=0):

        self.decent_level = decent_level
        
        if self.validate(string_input):
            self.string_input = string_input
            #build out cuboid
            self.compute_characteristics()              
            self.generate_cube_space()
            self.place_mines()
        
    # stub validation
    def validate(self, string_input):
        # must be an odd number on x and y
        # all x lines must be same width
        # all y lines must be same width
        return True

    
    # compute the state of the cuboid
    def compute_characteristics(self):        

        # get the set of mine characters
        self.mine_chars = list(set(re.findall(r'[a-zA-Z]', self.string_input)))
     
        # lookup chars
        self.mine_chars = map(lambda char:
                              self.char_resolver(char),
                              self.mine_chars)

        print "mine_chars: " + str(self.mine_chars)
        #ipdb.set_trace()

        self.lines = self.string_input.strip().split(self.eol)
        
        # compute height and width
        self.width = len(list(self.string_input.split()[0].strip()))
        self.height = len(self.string_input.split(self.eol))

        #compute depth
        if not self.mine_chars:
            self.depth = 0
        else:
            self.deepest_mine = reduce(lambda lowest,current: current
                                       if self.z_map[current] < self.z_map[lowest]
                                       else lowest, self.mine_chars)
            self.depth = self.z_map[self.deepest_mine]
        
    # generate a cubic data structure of correct dimensions
    # note: z-axis is negatively oriented to allow tracking of planar decent
    def generate_cube_space(self):
        self.cube_space = [[[self.empty_space for z in range(self.depth, 0, 1)]
                            for y in range(self.height)]
                           for x in range(self.width)]
        
    # compute the mine coordinates and place them in cubic space
    def place_mines(self):
        self.mines = []
        # reversing the lines to make y=0 at the bottom
        for y,line in enumerate(reversed(self.lines)):
            for x,char in enumerate(list(line.strip())):
                if char in self.mine_chars:
                    z = self.z_map[char]
                    try:
                        # site the mine
                        self.cube_space[x][y][z] = char
                        self.mines.append(((x,y,z), char))
                    except Exception as ex:
                        ipdb.set_trace()
                        raise ex
                    
        # order the mines by depth
        self.mines = sorted(self.mines, key=lambda mine: mine[0][2])
        print "mines: ", str(self.mines)

    def char_resolver(self, char):
        charv = self.z_map[char]
        resolved = char
        for c, v in self.z_map.iteritems():
            if v == charv - self.decent_level:
                print "adjusting char: ", char, " to ", c
                resolved = c
        self.string_input = self.string_input.replace(char,resolved)
        return resolved
    
    def sweep_mines(self, hit_mines):
        for mine in hit_mines:
            print "removing hit mine: ", mine
            coords, char = mine
            x,y,z = coords
            self.cube_space[x][y][z] = "."
            self.mines = [m for m
                          in self.mines
                      if not coords == m[0]]
        
    def recompute_space(self, coordinates):
        x,y,z = coordinates
        ipdb.set_trace()

    def get_central_coordinates(self):
        # find cartesian center and decrement because we're zero indexed
        return (((self.width / 2)  + (self.width % 2)) - 1,
                ((self.height / 2) + (self.height % 2)) - 1,
                (self.depth / 2) + 1) # depth is negative, so we add 1

        
    def most_east_mine(self):
        most_east_mine = reduce(lambda highest,current: current
                                if current[0][0] > highest[0][0]
                                else highest, self.mines)
        return most_east_mine

    def most_west_mine(self):
        most_west_mine = reduce(lambda lowest,current: current
                                if current[0][0] < lowest[0][0]
                                else lowest, self.mines)
        return most_west_mine

    def most_north_mine(self):
        most_north_mine = reduce(lambda highest,current: current
                                 if current[0][1] > highest[0][1]
                                 else highest, self.mines)
        return most_north_mine

    def most_south_mine(self):
        most_south_mine = reduce(lambda lowest,current: current
                                 if current[0][1] < lowest[0][1]
                                 else lowest, self.mines)
        return most_south_mine

        
    def render(self):
        builder = StringIO()
        # note: we are decrementing height to accomodate for the index being one lowe
        print "BEFORE: \n", self.string_input, "\n"
        for y in range(self.height)[::-1]: 
            y_mines = [m for m in self.mines if m[0][1] == y]
            for x in xrange(self.width):
                xy_mine = next((m for m in y_mines if m[0][0] == x), None)
                if xy_mine is not None:
                    builder.write(xy_mine[1])
                else:
                    builder.write(".")
            builder.write(self.eol)
        matrix = builder.getvalue().rstrip(self.eol)
        return matrix
        

    def __str__(self):
        return self.render()
        
    def __repr__(self):
        return self.__str__()
    
    def clone(self):
        return deepcopy(self)
