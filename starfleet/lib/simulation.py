import sys
import ipdb

# our modules
import cuboid
import step
import vessel

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

    default_cuboid_file =  "cuboid.dat"
    default_steps_file = "student_minesweeping_script.steps"
    
    def __init__(self, cuboid_file=default_cuboid_file,steps_file=default_steps_file):
        self.history = []

        self.cuboid_file = cuboid_file
        self.steps_file =  steps_file 

        # use the file to name our ship
        ship_name = cuboid_file.split("_")[0]

        # initialize vessel
        self.vessel = Vessel(ship_name)
        
    def run(self):
        # read inputs
        self.cuboid_input = open(self.cuboid_file, "r").read()
        self.step_inputs = open(self.steps_file, "r").read().split("\n")

        # initialize cuboid and vessel state 
        self.cuboid = Cuboid(self.cuboid_input)
        self.center_vessel()

        # run the steps
        for step_input in self.step_inputs:
            print "running step: " + step_input
            #ipdb.set_trace()
            self.step(self.cuboid_input, step_input)
        
    def center_vessel(self):
        #set ship's coordinates to center of 2d plane at decent level on 3d plane
        coords  = self.get_center(self.cuboid.width,
                                  self.cuboid.height,
                                  self.vessel.decent_level)

        self.vessel.x, self.vessel.y, self.vessel.z = coords
        
        print "sited vessal at coordinates :" + str((coords))
        
    def step(self, cuboid_input, step_input):
        self.cuboid = Cuboid(cuboid_input)
        step = Step(step_input)
        vessel = self.vessel

        # "Engage, Numba One!..."
        vessel.engage(step, self.cuboid)

        # now recompute 
        self.compute_new_state()
        
    def compute_new_state(self):
        vx,vy,vz = self.vessel.get_coordinates()

        cx,cy,cz = self.get_center(self.cuboid.width,
                                   self.cuboid.height,
                                   self.vessel.decent_level)

        # now replace self.cuboid with next frame
        # todo:...
            
           
        
    def get_center(self,width, height, depth):
        # find cartesian center and decrement because we're zero indexed
        return (((width / 2)  + (width % 2)) - 1,
                ((height / 2) + (height % 2)) - 1,
                depth)



#Simulation().run()
