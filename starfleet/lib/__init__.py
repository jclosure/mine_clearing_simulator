import sys
import ipdb


import simulation
import step
import cuboid
import vessel
import options
import process
import grid
import scoring
import entity

# singleton modules are not classes
import toolbox
import computer
import logger

logger.setup_logging()

try:
    reload
except NameError:
    # Python 3
    from imp import reload

# inject test_shim before we load the domain    
from sys import modules
try:
    test_shim = modules['test_shim']
except KeyError:
    import test_shim as test_shim


reload(cuboid)
reload(step)
reload(vessel)
reload(grid)
reload(computer)
reload(scoring)
reload(entity)
    
# domain class constant's are exposed from the "lib" module's api
Process = process.Process
ProcessException = process.ProcessException
Options = options.Options
Simulation = simulation.Simulation
Step = step.Step
Cuboid = cuboid.Cuboid
Vessel = vessel.Vessel
Grid = grid.Grid
Scoring = scoring.Scoring
Entity = entity.Entity

# testbed
import canary
reload(canary)
Canary = canary.Canary
