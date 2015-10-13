import sys

from lib import Simulation
from lib import Options

if __name__ == '__main__':
    options = Options()
    opts = options.parse(sys.argv[1:])

    sim  = Simulation(opts.cuboid_file, opts.steps_file)
    sim.engage()

