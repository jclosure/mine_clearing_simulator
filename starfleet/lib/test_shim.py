import sys
import os
import yaml
import imp
from inspect import getsourcefile
from os.path import abspath
from os.path import dirname
from os.path import join


######### HOW TO: TEST IN IPYTHON ############

'''

this file fixes the "lib" path for unittesting in ipython.

you simply need to C-c C-c a buffer with this file into ipython, 

then you can C-c C-c unit tests from the ./tests dir and the lib modules will

resolve correctly. 

'''

##############################################


dir_path = abspath(join(dirname(getsourcefile(lambda:0))))
lib_path = join(dir_path, "__init__.py")
shim_path = join(dir_path, "test_shim.py")
import sys
sys.path.insert(1,dir_path)


from sys import modules
try:
    lib = modules['lib']
except KeyError:
    lib = imp.load_source('lib',lib_path) 

try:
    test_shim = modules["test_shim"]
except KeyError:
    test_shim = imp.load_source('test_shim', shim_path) 


# pm = __import__(path)
# print("test_shim importing ", dir(pm)) # just for fun :)


# global __modpath__
# __modpath__ = module_path(main)
