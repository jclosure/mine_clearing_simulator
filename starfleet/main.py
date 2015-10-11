import sys

from lib import Simulation
from lib import Options

if __name__ == '__main__':
    options = Options()
    opts = options.parse(sys.argv[1:])

    sim  = Simulation()

    #v.date()
    #v.print_example_arg()
