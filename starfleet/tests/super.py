import unittest
from mockito import *
from lib import Options
from lib import Simulation

# mockito: https://code.google.com/p/mockito-python/

class TestSimulator2(unittest.TestCase):
    def _default_options(self):
        options = Options()
        opts = options.parse()
        return opts

    def setUp(self):
        opts = self._default_options()
        self.sim = Simulation(opts.cuboid_file, opts.steps_file)
        self.sim_spy = spy(self.sim)

    def verify_run_sequence(self):
        self.sim.run()        
        verify(self.sim_spy).center_vessel()
        verify(self.sim_spy).foo()
        verify(self.sim_spy).compute_new_state()

        
if __name__ == '__main__':
    unittest.main()
