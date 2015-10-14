import ipdb
from copy import deepcopy
from cStringIO import StringIO
import computer
from entity import Entity

class Grid(Entity):

    eol = "\n"
    
    def __init__(self, string_input):
        self.string_input = string_input
        self.matrix = map(lambda row: list(row),
                           map(lambda line: line.strip(),
                               self.string_input.split(self.eol)))
        self.height = len(self.matrix)
        self.width =  next((len(r) for r in self.matrix), 0)
        
    # section: shrinking operations
    def valid(self, num):
        return num > 0
  
    
    def shrink_west(self, num):
        if self.valid(num):
            self.matrix = map(lambda row: row[num:], self.matrix)

    def shrink_east(self, num):
        if self.valid(num):
            self.matrix = map(lambda row: row[:-1*num], self.matrix)
            
    def shrink_north(self, num):
        if self.valid(num):
            self.matrix = self.matrix[num:]

    def shrink_south(self, num):
        if self.valid(num):
            self.matrix = self.matrix[:-1*num]

    # section: growth operations
        
    def grow_west(self, num):
            for i in range(num):
                for row in self.matrix:
                    row[:0] = "."
        
    def grow_east(self, num):
            for i in range(num):
                for row in self.matrix:
                    row.append(".")

    def grow_north(self, num):
            for i in range(num):
                row = [map(lambda col: ".",
                           range(len(self.matrix[0])))]
                self.matrix[:0] = row

    def grow_south(self, num):
            for i in range(num):
                row = [map(lambda col: ".",
                           range(len(self.matrix[0])))]
                self.matrix = self.matrix + row

    def grow_face(self, face, xends, yends):

        ## this is here to enable breaking on a specific step during debugging
        # last = self.vessel.steps[-1]
        # if last and last.instructions == "south":
        #     ipdb.set_trace()

        vcoords = self.vessel.get_coordinates()

        xpos,ypos,zpos = vcoords
        
        # grow x
        ax_west, ax_east = computer.get_center_offsets(xends,xpos)
        
        # grow y
        ay_south, ay_north = computer.get_center_offsets(yends,xpos)
 
        g = Grid(face)
        
        # note: the second value in the tuple contains the adjustment

        # fixup for smaller than rect

        print "GROW OFFSETS:", "west:", ax_west[1], "east:", ax_east[1], "south:", ay_south[1], "north:", ay_north[1] 
        
        g.grow_west(ax_west[1])
        g.grow_east(ax_east[1])
        g.grow_south(ay_south[1])
        g.grow_north(ay_north[1])

        grown_face = g.render()
        
        print "grown face: \n" + grown_face
        return face
        
    def render(self):
        builder = StringIO()
        for row in self.matrix:
            for cell in row:
                builder.write(cell)
            builder.write(self.eol)
        output = builder.getvalue().rstrip(self.eol)
        return output

    def get_central_coordinates(self):
        # find cartesian center and decrement because we're zero indexed
        return (((self.width / 2)  + (self.width % 2)) - 1,
                ((self.height / 2) + (self.height % 2)) - 1)
    
    def __str__(self):
        return self.render()
        
    def __repr__(self):
        return self.__str__()
    
    
    def clone(self):
        return deepcopy(self)
