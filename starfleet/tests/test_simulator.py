import unittest

from lib import Options
from lib import Simulation

class TestSimulator(unittest.TestCase):
    def _default_options(self):
        options = Options()
        opts = options.parse()
        return opts

    def setUp(self):
        opts = self._default_options()
        self.sim = Simulation(opts.cuboid_file, opts.steps_file)

    def blow_up(self):
        self.assertTrue(2>3)

if __name__ == '__main__':
    unittest.main()
