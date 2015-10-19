
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
from lib import Simulation
from lib import Step
from lib import toolbox

dir_path = abspath(join(dirname(getsourcefile(lambda:0))))

# run all these tests automatically from repl
def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimulator)
    unittest.TextTestRunner(verbosity=3).run(suite)

# working correctly in repl!!!
    
class TestSimulator(BaseTest):

    
    def configure_simulator(self,
                            cuboid_file="cuboid.dat",
                            steps_file="student_minesweeping_script.steps"):
        self.cuboid_file = join(self.input_dir(), cuboid_file)
        self.steps_file = join(self.input_dir(), steps_file)


    def setUp(self):
        # configure self.attribute
        self.configure_simulator()
        self.sim = Simulation(self.cuboid_file,
                              self.steps_file)


    def tearDown(self):
        # tear down self.attribute
        pass


    def test_run_sequence_is_stable(self):
       sim = self.sim
       sim.engage()      
       this(len(sim.history)).should.equal(len(sim.step_inputs))


    def test_vessel_movement(self):
        sim = self.sim
        # act
        # assert initial state
        this(sim.vessel.get_coordinates()).should.equal((2,2,0))
        # does the ship move and drop correctly?
        sim.step("north")
        this(sim.vessel.get_coordinates()).should.equal((2,3,-1))
        sim.step("east")
        this(sim.vessel.get_coordinates()).should.equal((3,3,-2))


    def test_vessel_targeting(self):
        #arrange
        sim = self.sim
        #act

        vessel, step, nstep, ocuboid, ncuboid = sim.step("north")
        this(nstep.hits).should.be.empty
        vessel, step, nstep, ocuboid, ncuboid = sim.step("delta south")
        this(nstep.hits).should_not.be.empty
        
        
    
        
# autoexecute
if __name__ == '__main__':
    unittest.main()


    
