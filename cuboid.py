
import re

class Cuboid:

    z_map = {c:(i+1)*-1 for i,c in enumerate([chr(c) for c in range(ord('a'), ord('z')+1)] + [chr(c) for c in range(ord('A'), ord('Z')+1)])}

    eol = "\n"
    
    def __init__(self, input):
        if self.validate(input):
            self.input = input

            #build out cuboid
            self.compute_characteristics()              
            self.generate_cube_space()
            self.place_mines()
        
    # stub validation
    def validate(self, input):
        # must be an odd number on x and y
        # all x lines must be same width
        # all y lines must be same width
        return True

    # compute the state of the cuboid
    def compute_characteristics(self):        

        # get the set of mine characters
        self.mine_chars = list(set(re.findall(r'[a-zA-Z]', self.input)))
        
        # compute height and width
        self.width = len(list(self.input.split()[0].strip()))
        self.height = len(self.input.split(self.eol))

        #compute depth
        self.deepest_mine = reduce(lambda lowest,current: current
                                   if self.z_map[current] < self.z_map[lowest]
                                   else lowest, self.mine_chars)
        self.depth = self.z_map[self.deepest_mine]

        # find cartesian center
        self.center_point = ((self.width / 2) + (self.width % 2), (self.height / 2) + (self.height % 2))
        
    # generate a cubic data structure of correct dimensions
    # note: z-axis is negatively oriented to allow tracking of planar decent
    def generate_cube_space(self):
        self.cube_space = [[['.' for z in range(self.depth, 0, 1)] 
                            for y in range(self.height)] 
                           for x in range(self.width)]
        
    # compute the mine coordinates and place them in cubic space
    def place_mines(self):
        self.mines = []
        for y,line in enumerate(input.strip().split(self.eol)):
            for x,char in enumerate(list(line.strip())):
                if char in self.mine_chars:
                    z = self.z_map[char]

                    # site the mine
                    self.cube_space[x][y][z] = char
                    self.mines.append(((x,y,z), char))

        # order the mines by depth
        self.mines = sorted(self.mines, key=lambda mine: mine[0][2])
        
  
