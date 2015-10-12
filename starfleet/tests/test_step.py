import ipdb
from lib import Options
from lib import Step
from lib import toolbox

from sure import *

# mockito: https://code.google.com/p/mockito-python/
import sys, os

from base_test import BaseTest

class TestStep(BaseTest):
    def setUp(self):
        pass

    def test_lexing(self):
        s = Step("north")
        print "instructions: " + s.instructions
        print s.operations
