import sys
import ipdb



import lib

# singleton modules are not classes

from lib import logger
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




