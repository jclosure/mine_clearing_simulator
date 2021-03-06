import ipdb

# steps:
# 1. chop rectangle to mines and ship
# 2. find longest diff between ship and edges
# 3. offset remaining 3 edges ensuring that length


def smallest_rectangle(coords):
    # if len(coords) > 4:
    #     pad = 4 - len(coords)
    #     for i in range(pad):
    #         coords.append((0,0)) # we need at least 4 points for rectangles

    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]

    # send back new edges
    return (("west", find_lowest(xs)),
            ("east", find_highest(xs)),
            ("south", find_lowest(ys)),
            ("north", find_highest(ys)))


def find_lowest(seq):
    return reduce(lambda lowest, current: current
                  if current < lowest
                  else lowest, seq)


def find_highest(seq):
    return reduce(lambda highest, current: current
                  if current > highest
                  else highest, seq)


def furthest_edge_from_point(rect, point):
    ew, ee, es, en = rect
    exs = (ew, ee)
    eys = (es, en)
    px, py = point

    furthest = ew  # just in case all dimensions are 0
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
    le, he = ends

    ldif = abs(pos - le)
    hdif = abs(pos - he)

    if hdif > ldif:
        offset = hdif - ldif
        return ((le, offset * -1), (he, 0))
    elif ldif > hdif:
        offset = ldif - hdif
        return ((le, 0), (he, offset))
    else:
        return (le, 0), (he, 0)


def get_center(self, width, height):
    # find cartesian center and decrement because we're zero indexed
    return (((width / 2) + (width % 2)) - 1,
            ((height / 2) + (height % 2)) - 1)
