import sys
import ipdb

# our modules
import cuboid
import step
import vessel
import computer
import logger
import logging as log

try:
    reload
except NameError:
    # Python 3
    from imp import reload

reload(cuboid)
reload(step)
reload(vessel)

# our domain
Cuboid = cuboid.Cuboid
Step = step.Step
Vessel = vessel.Vessel

# for easy debugging in ipython, do this: %load_ext autoreload

class Simulation:

    # file sentinals
    default_cuboid_file =  "./test_input/cuboid.dat"
    default_steps_file = "./test_input/student_minesweeping_script.steps"
    
    def __init__(self, cuboid_file=default_cuboid_file,steps_file=default_steps_file):
        log.info("creating new simulation")

        # replay
        self.history = []

        # pre-declare lazy file slots
        self.cuboid_file = cuboid_file
        self.steps_file =  steps_file 
        self.cuboid_input = None
        self.step_inputs = None

        # build out
        self.initialize_cuboid()
        self.initialize_flight_plan()
        self.initialize_vessel()
    
    def engage(self):

        # map over the steps
        self.history = self.history + map(lambda step_input:
                                              self.step(step_input),
                                              self.step_inputs)
        
        
    def step(self, step_input):

        # create step operations
        step = Step(step_input)

        # ship operates in cuboid
        self.vessel.step(step, self.cuboid)

        # cleanup any hits
        self.cuboid.sweep_mines(step.hits)

        # flash freeze and stash the universe
        last_cuboid = self.cuboid.clone()
        
        # now recompute state
        self.recompute_cuboid()

        # collect all the good stuff
        return (step, self.vessel, last_cuboid, self.cuboid) 

    def recompute_cuboid(self):

        cuboid_face = self.cuboid.render()

        print cuboid_face

        self.initialize_cuboid(cuboid_face,
                               self.vessel.decent_rate,
                               self.vessel.decent_level)
        
      

    def initialize_vessel(self):
        
        # use the file to name our ship
        ship_name = self.cuboid_file.split("_")[0]

        # initialize vessel
        self.vessel = Vessel(ship_name)
        self.center_vessel()
    
    def initialize_flight_plan(self, step_inputs=None):

        if step_inputs is None:
            self.step_inputs = open(self.steps_file, "r").read().split("\n")
        else:
            #note we're going to pass in the script as a string here..
            self.step_inputs = step_inputs.read().split("\n")

    def initialize_cuboid(self, cuboid_input=None, decent_rate=0, decent_level=0):

        # read inputs
        if cuboid_input is None:
            self.cuboid_input = open(self.cuboid_file, "r").read()
        else:
            self.cuboid_input = cuboid_input
            
        
        print "initializing cuboid at decent_level: ", decent_level
        
        self.cuboid = Cuboid(self.cuboid_input, decent_rate * -1)
           
    def center_vessel(self):

        #set ship's coordinates to center of 2d plane at decent level on 3d plane
        coords  = self.cuboid.get_central_coordinates()

        self.vessel.x, self.vessel.y, middle  = coords
        
        print "sited vessal at coordinates :" + str((coords))
        

