import ipdb
from cStringIO import StringIO

class Grid:

    eol = "\n"
    
    def __init__(self, string_input):
        self.string_input = string_input
        self.matrix = map(lambda row: list(row),
                           map(lambda line: line.strip(),
                               self.string_input.split(self.eol)))
        self.height = len(self.matrix)
        self.width =  next((len(r) for r in self.matrix), 0)
        
    # section: shrinking operations

    def valid_resize(self, num):
        return num > 0
    
    def shrink_west(self, num):
        if self.valid_resize(num):
            self.matrix = map(lambda row: row[num:], self.matrix)

    def shrink_east(self, num):
        if self.valid_resize(num):
            self.matrix = map(lambda row: row[:-1*num], self.matrix)
            
    def shrink_north(self, num):
        if self.valid_resize(num):
            self.matrix = self.matrix[num:]

    def shrink_south(self, num):
        if self.valid_resize(num):
            self.matrix = self.matrix[:-1*num]

    # section: growth operations
        
    def grow_west(self, num):
        if self.valid_resize(num):
            for i in range(num):
                for row in self.matrix:
                    row[:0] = "."
        
    def grow_east(self, num):
        if self.valid_resize(num):
            for i in range(num):
                for row in self.matrix:
                    row.append(".")

    def grow_north(self, num):
        if self.valid_resize(num):
            for i in range(num):
                row = [map(lambda col: ".",
                           range(len(self.matrix[0])))]
                self.matrix[:0] = row

    def grow_south(self, num):
        if self.valid_resize(num):
            for i in range(num):
                row = [map(lambda col: ".",
                           range(len(self.matrix[0])))]
                self.matrix = self.matrix + row

        
    def render(self):
        builder = StringIO()
        for row in self.matrix:
            for cell in row:
                builder.write(cell)
            builder.write(self.eol)
        output = builder.getvalue().rstrip(self.eol)
        return output

    
    def __str__(self):
        return self.render()
        
    def __repr__(self):
        return self.__str__()
    
