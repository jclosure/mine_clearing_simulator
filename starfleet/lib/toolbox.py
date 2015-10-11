import os
import inspect

def module_path(local_function):
   ''' returns the module path without the use of __file__.  Requires a function defined 
   locally in the module.
   from http://stackoverflow.com/questions/729583/getting-file-path-of-imported-module'''
   return os.path.abspath(inspect.getsourcefile(local_function))

def script_path():
    ''' get's the fully qualified path of the called script '''
    return os.path.abspath(__file__)


def module_dir(local_function):
    ''' just the directory name please '''
    return os.path.dirname(module_path(local_function))

def script_dir():
    ''' just the directory name please '''
    return os.path.dirname(script_dir)
