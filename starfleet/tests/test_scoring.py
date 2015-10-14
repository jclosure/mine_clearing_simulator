import ipdb

from sure import *

from lib import Options
from lib import Cuboid
from lib import Vessel
from lib import Simulation
from lib import computer
from lib import toolbox

import pytest

# mockito: https://code.google.com/p/mockito-python/
# py.test stdout: https://pytest.org/latest/capture.html
# run with py.test -s to see print statements
# to run just this class: py.test -s test_scoring.py::TestScoring

# sure dsl: https://github.com/gabrielfalcao/sure/blob/master/tests/test_assertion_builder.py

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
    args_str = "-k test_scoring"
    pytest.main(args_str.split(" "))


# get a tester for running manually from repl
def manual():
    tester = TesScoring()
    tester.configure_simulator()
    tester.setup_method("just_start_it_up")
    return tester

class TestScoring:

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

    #todo: i have not implemented these yet. setting the specs to fail for now.
    
    def test_passed_a_mine(self):
        pytest.fail("not implemented yet")

    def test_script_completes_but_mines_still_remaining(self):
        pytest.fail("not implemented yet")

    def test_all_mines_cleared_but_steps_remaining(self):
        pytest.fail("not implemented yet")

    def test_all_mines_cleared_with_no_steps_remaining(self):
        pytest.fail("not implemented yet")
        
