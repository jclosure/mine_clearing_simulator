
from cuboid import Cuboid
from step import Step
from vessel import Vessel

class Simulation:

    def __init__(self):
        self.history = []

        # read inputs
        self.cuboid_input = open("./cuboid.dat", "r").read()
        self.step_inputs = open("./student_minesweeping_script.steps", "r").read().split("\n")

        # build initial cuboid state
        self.cuboid = Cuboid(self.cuboid_input)

        # initialize vessel
        self.vessel = Vessel(name)
        center_vessel()

    def center_vessel(self):
        #set coordinates to center of 2d plane on top of 3d plane
        self.vessel.coordinates = self.cuboid.center_point + (0,)
        
    def step(self, cuboid_input, step_input):
        cuboid = Cuboid(cuboid_input)
        vessel = self.vessel
        step = Step(step_input)

        # act
        act(vessel, cuboid, step)
        
        # produce output

        # recompute cuboid
    
        pass

    def act(self, vessel, cuboid, step):
        # change position of ship in cuboid
        
    
  
