

class Step:

    available_firing_patterns = (('alpha',((-1, -1), (-1, 1), (1, -1), (1, 1))),
                                 ('beta',((-1, 0), (0, -1), (0, 1), (1, 0))),
                                 ('gamma',((-1, 0), (0, 0), (1, 0))),
                                 ('delta',((0, -1), (0, 0), (0, 1))))

    available_moves = (('north', lambda x,y: (x, y+1)),
                       ('south', lambda x,y: (x, y-1)),
                       ('east', lambda x,y: (x-1, y)),
                       ('west', lambda x,y: (x+1, y)))
    
    def __init__(self, instructions):
        self.fall = -1
        self.lex(instructions)
        
    def lex(self):
        self.instructions  = self.instructions.split()

        # resolve move
        self.move = (m for m in self.available_moves
                     if m[0] in self.instructions).next()
        
        # resolve firing_pattern
        self.firing_pattern = (pat for pat in self.available_firing_patterns
                               if pat[0] in self.instruction).next()



