import unittest
import sys, os
from lib import toolbox

class BaseTest(unittest.TestCase):
    def this_dir(self):
        return this_dir

# ALWAYS FIND THIS DIRECTORY
this_dir = toolbox.module_dir(BaseTest)
