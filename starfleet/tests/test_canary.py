
# load modules in order
import inspect
import sys, os
import yaml
import imp
from inspect import getsourcefile
from os.path import abspath
from os.path import dirname
from os.path import join


from mockito import *
from sure import *
import pytest
import unittest
from base_test import BaseTest


from lib import Options
from lib import toolbox

# sut
from lib import Canary

dir_path = abspath(join(dirname(getsourcefile(lambda:0))))

# run all these tests automatically from repl
def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(CanaryTest)
    unittest.TextTestRunner(verbosity=3).run(suite)

# working correctly in repl!!!
class CanaryTest(BaseTest):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_canary_can_tweet(self):
        from canary import Canary
        can = Canary()
        k,v = can.find_method("tweet")
        this(k).should.be.equal("tweet")
    
