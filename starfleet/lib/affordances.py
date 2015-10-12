
decent_rate = 1

navigation = (('north', lambda x,y: (x, y+1)),
              ('south', lambda x,y: (x, y-1)),
              ('east', lambda x,y: (x+1, y)),
              ('west', lambda x,y: (x-1, y)))

firing_patterns = (('alpha',((-1, -1), (-1, 1), (1, -1), (1, 1))),
                   ('beta',((-1, 0), (0, -1), (0, 1), (1, 0))),
                   ('gamma',((-1, 0), (0, 0), (1, 0))),
                   ('delta',((0, -1), (0, 0), (0, 1))))
