import inspect


from mockito import *

from lib import Options
from lib import Simulation
from lib import toolbox


# mockito: https://code.google.com/p/mockito-python/
import sys, os

from base_test import BaseTest

class TestSimulator(BaseTest):


    
    def _default_options(self):
        options = Options()
        opts = options.parse()
        return opts

    def setUp(self):
        opts = self._default_options()
        input_dir = self.this_dir() + "/test_input/"
        self.sim = Simulation( input_dir + opts.cuboid_file,
                               input_dir + opts.steps_file)
        self.sim_spy = spy(self.sim)

    def test_run_sequence(self):
        self.sim_spy.run()        
        verify(self.sim_spy).center_vessel()
        verify(self.sim_spy).step()
        verify(self.sim_spy).compute_new_state()

        
if __name__ == '__main__':
    unittest.main()


    
