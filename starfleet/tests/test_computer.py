import ipdb

from sure import *

from lib import Options
from lib import Cuboid
from lib import Vessel
from lib import computer
from lib import toolbox


# mockito: https://code.google.com/p/mockito-python/
# py.test stdout: https://pytest.org/latest/capture.html
# run with py.test -s to see print statements
# to run just this class: py.test -s test_computer.py::TestComputer


import sys, os
import yaml
import imp
from inspect import getsourcefile
from os.path import abspath
from os.path import dirname
from os.path import join
dir_path = abspath(join(dirname(getsourcefile(lambda:0))))

# run all these tests automatically from repl
def run():
    import pytest
    args_str = "-k test_computer"
    pytest.main(args_str.split(" "))

# get a ts for running manually from repl
def manual():
    ts = TestSimulator()
    ts.configure_simulator()
    ts.setup_method("just_start_it_up")
    return ts

class TestComputer:

    def setup_method(self, test_method):
        exemplar1 = """..N..
                       .....
                       W...E
                       .....
                       ..S.."""
        
        self.cub = Cuboid(exemplar1)
        self.ves = Vessel("My Test Ship")

    def teardown_method(self, test_method):
        # tear down self.attribute
        pass

    def test_chopping_rectangle_to_coordinates(self):
        cub = self.cub
        ves = self.ves

        # get all mine coords
        mine_coords = [mine[0] for mine in cub.mines]
        # add the ship's coords
        coords = mine_coords + [ves.get_coordinates()]

        # act
        west_edge, east_edge, south_edge, north_edge = computer.smallest_rectangle(coords)
        
        # assert
        this(west_edge[1]).should.be.equal(0)
        this(east_edge[1]).should.be.equal(4)
        this(south_edge[1]).should.be.equal(0)
        this(north_edge[1]).should.be.equal(4)
        
        # finding smallest rectangle
        
        # remove N
        mine_coords = [mine[0] for mine in cub.mines if not mine[1] == "N"]
        coords = mine_coords + [ves.get_coordinates()]
        # act
        west_edge, east_edge, south_edge, north_edge = computer.smallest_rectangle(coords)

        # assert
        this(west_edge[1]).should.be.equal(0)
        this(east_edge[1]).should.be.equal(4)
        this(south_edge[1]).should.be.equal(0)
        this(north_edge[1]).should.be.equal(2) # this was adjusted

    def test_finding_furthest_edge(self):

        # furthest north, moving edge
        point = (2, 2)
        rect = (("west", 0),
                ("east", 4),
                ("south",0),
                ("north",5))
        
        furthest = computer.furthest_edge_from_point(rect, point)
        this(furthest).should.be.equal([("north",5), 3])

        # furthest west, moving point
        point = (3, 2)
        rect = (("west", 0),
                ("east", 4),
                ("south",0),
                ("north",4))
        furthest = computer.furthest_edge_from_point(rect, point)
        this(furthest).should.be.equal([("west",0),3])

    def test_computing_center_offsets(self):
        pos = (1)
        ends = (0, 6)
        offsets = computer.get_center_offsets(ends, pos)
        e1, e2 = offsets
        this(e1).should.be.equal((0, -4))
        this(e2).should.be.equal((6, 0))
        #((0, -5), (6, 0))

    def test_push_out_rectangle(self):
        point = (3, 2)
        rect = (("west", 0),
                ("east", 4),
                ("south",0),
                ("north",4))

        # test only x axis
        pos = point[0] # x
        ends = rect[0][1], rect[1][1] # west ---> east
        
        x_offsets = computer.get_center_offsets(ends, pos)
        we, ee = x_offsets
        
        this(we).should.be.equal((0, 0))
        this(ee).should.be.equal((4, 2))
        
    #todo: ...    
    def test_the_new_center_should_be_the_vessels_location(self):
        pass

    def test_the_edge_should_be_pushed_out_if_ship_position_is_in_that_dir(self):
        pass

    def test_the_edge_should_be_pulled_in_if_ship_position_is_in_the_other_dir(self):
        pass

    def test_the_edge_should_stop_shrinking_at_a_mine(self):
        pass
    
        
