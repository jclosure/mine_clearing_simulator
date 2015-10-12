import ipdb
from lib import Options
from lib import Cuboid
from lib import toolbox

from sure import *

# mockito: https://code.google.com/p/mockito-python/
# py.test stdout: https://pytest.org/latest/capture.html
# run with py.test -s to see print statements
# to run just this class: py.test -s test_cuboid.py::TestCuboid

import sys, os

from base_test import BaseTest

class TestCuboid(BaseTest):


    
    def setUp(self):
        exemplar1 = """..N..
                       .....
                       W...E
                       .....
                       ..S.."""
        
        self.cub = Cuboid(exemplar1)

    def test_mine_placement(self):
        cub = self.cub
        north = cub.most_north_mine()
        south = cub.most_south_mine()
        east = cub.most_east_mine()
        west = cub.most_west_mine()

        print "north: ", north
        print "south: ", south
        print "east: ", east
        print "west: ", west

        this(north).should.be.equal(((2, 4, -45), 'N'))
        this(south).should.be.equal(((2, 0, -40), 'S'))
        this(east).should.be.equal(((4, 2, -31), 'E'))
        this(west).should.be.equal(((0, 2, -49), 'W'))
