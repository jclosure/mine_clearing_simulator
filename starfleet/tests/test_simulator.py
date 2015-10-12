import inspect


from mockito import *

from lib import Options
from lib import Simulation
from lib import Step
from lib import toolbox

from sure import *

# mockito: https://code.google.com/p/mockito-python/
import sys, os

from base_test import BaseTest

class TestSimulator(BaseTest):


    
    def configure_simulator(self,
                            cuboid_file="cuboid.dat",
                            steps_file="student_minesweeping_script.steps"):
        self.input_dir = self.this_dir() + "/test_input/"
        self.output_dir = self.this_dir() + "/test_output/"
        self.cuboid_file = self.input_dir + cuboid_file
        self.steps_file = self.input_dir + steps_file
        self.output_file = self.output_dir + steps_file + ".out"

    def setup_method(self, test_method):
        # configure self.attribute
        self.configure_simulator()
        self.sim = Simulation(self.cuboid_file,
                              self.steps_file)

    def teardown_method(self, test_method):
        # tear down self.attribute
        pass
    
    # def test_run_sequence_is_stable(self):
    #    sim = self.sim
    #    sim.engage()      
    #    this(sim.steps_run).should.equal(sim.step_inputs)
       
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

    # def test_vessel_firing(self):
    #     #arrange
    #     sim = self.sim
    #     #act
    #     step, vessel = sim.step("gamma")
    #     #this(step.hits).should_not.be.empty
        
    # def test_step_engages(self):
    #     self.fail("implement")

    # def test_compute_new_state(self):
    #     self.fail("implement")

    # def test_simulator_writes_output(self):
    #     self.fail("implement")

    
        
# autoexecute
if __name__ == '__main__':
    unittest.main()


    
