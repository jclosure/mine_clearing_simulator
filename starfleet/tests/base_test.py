import unittest
import sys, os
from inspect import getsourcefile
from os.path import abspath
from os.path import dirname
from os.path import join


import imp

test_path = abspath(join(dirname(getsourcefile(lambda:0))))

lib_path = join(test_path, '../lib') 

sys.path.append(lib_path)

import test_shim

class BaseTest(unittest.TestCase):

    in_dir = join(test_path, "test_input")
    out_dir = join(test_path, "test_output")

    def input_dir(self):
        return self.in_dir
    
    def output_dir(self):
        return self.out_dir
        
    def this_dir(self):
        return test_path

    def setup_method(self, method):
        self.setUp()

    def teardown_method(self, method):
        self.tearDown()

    


