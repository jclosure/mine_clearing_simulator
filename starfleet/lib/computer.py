import ipdb
# steps:
# 1. chop rectangle to mines and ship
# 2. find longest diff between ship and edges
# 3. offset remaining 3 edges ensuring that length


def smallest_rectangle(coords):   
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]

    # send back new edges
    return (("west", find_lowest(xs)),
            ("east", find_highest(xs)),
            ("south", find_lowest(ys)),
            ("north", find_highest(ys)))
    
def find_lowest(seq):
    return reduce(lambda lowest,current: current
                  if current < lowest
                  else lowest, seq)

def find_highest(seq):
    return reduce(lambda highest,current: current
                  if current > highest
                  else highest, seq)
    
def furthest_edge_from_point(rect, point):
    ew,ee,es,en = rect
    exs = (ew,ee)
    eys =(es,en)
    px, py = point

    furthest = ew # just in case all dimensions are 0
    largest = 0
    for ey in eys:
        diff = abs(py - ey[1])
        if diff > largest:
            largest = diff
            furthest = ey
            
    for ex in exs:
        diff = abs(px - ex[1])
        if diff > largest:
            largest = diff
            furthest = ex
    
    return [furthest, largest]

def get_center_offsets(ends, pos):
    le,he = ends
        
    ldif = abs(pos - le)
    hdif = abs(pos - he)
    
    if hdif > ldif:
        offset = hdif - ldif
        return ((le, offset * -1), (he, 0))
    elif ldif > hdif:
        offset = ldif - hdif
        return ((le, 0), (he, offset))
    
        
    
# def push_out_rectangle(rect, furthest, offset):
#     # ensure that all edges except furthest are at least 'offset' away
#     for edge in rect:
#         if not edge == furthest:
            


def resize_cube_space(cuboid, vessel_coordinates):
    vx,vy,vz = vessel_coordinates
    
    cx,cy = self.get_center(cur_cuboid.width,
                            cur_cuboid.height)

    ncenter = (vx, vy)
    
    # make new dotmap
    cheight = cur_cuboid.height
    cwidth = cur_cuboid.width

    
    # measure the distance between the vessel and the current 
    
    c_west_edge = 0
    c_east_edge = cwidth - 1
    c_south_edge = 0
    c_north_edge = cheight - 1
    
    
    cndiff = ('north_diff', ncenter - c_north_edge)
    csdiff = ('south_diff',ncenter - c_south_edge)
    cediff = ('east_diff', ncenter - c_east_edge)
    cwdiff = ('west_diff', ncenter - c_west_edge)
    
    cdiffs = [cndiff,csdiff,cediff,cwdiff]
    longest_cdiff = reduce(lambda highest,current: current
                           if current > highest
                           else highest, cdiffs)


    
    
    
def get_center(self,width, height):
    # find cartesian center and decrement because we're zero indexed
    return (((width / 2)  + (width % 2)) - 1,
            ((height / 2) + (height % 2)) - 1)

