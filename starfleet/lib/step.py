

class Step:

    available_firing_patterns = (('alpha',((-1, -1), (-1, 1), (1, -1), (1, 1))),
                                 ('beta',((-1, 0), (0, -1), (0, 1), (1, 0))),
                                 ('gamma',((-1, 0), (0, 0), (1, 0))),
                                 ('delta',((0, -1), (0, 0), (0, 1))))

    available_moves = (('north', lambda x,y: (x, y+1)),
                       ('south', lambda x,y: (x, y-1)),
                       ('east', lambda x,y: (x-1, y)),
                       ('west', lambda x,y: (x+1, y)))

    fall_distance = -1
    
    def __init__(self, line):
        self.lex(line)
        
    def lex(self, line):
        self.instructions  = line.split()

        # resolve move
        self.move = next((m for m in self.available_moves
                               if m[0] in self.instructions), None)
        # resolve firing_pattern
        self.firing_pattern = next((pat for pat in self.available_firing_patterns
                                    if pat[0] in self.instructions), None)


