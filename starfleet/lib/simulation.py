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

    default_cuboid_file =  "./test_input/cuboid.dat"
    default_steps_file = "./test_input/student_minesweeping_script.steps"
    
    def __init__(self, cuboid_file=default_cuboid_file,steps_file=default_steps_file):
        print "creating new simulation"
        
        self.history = []
        self.steps_run = []

        self.cuboid_file = cuboid_file
        self.steps_file =  steps_file 

        # read inputs
        self.cuboid_input = open(self.cuboid_file, "r").read()
        self.step_inputs = open(self.steps_file, "r").read().split("\n")

        # initialize cuboid and vessel state 
        self.cuboid = Cuboid(self.cuboid_input)

        # use the file to name our ship
        ship_name = cuboid_file.split("_")[0]

        # initialize vessel
        self.vessel = Vessel(ship_name)
        self.center_vessel()

        
    def engage(self):
        # run the steps
        self.steps_run = self.steps_run + map(lambda step_input:
                                              self.step(step_input),
                                              self.step_inputs)
        
        
    def step(self, step_input):
        step  = Step(step_input)
        cur_cuboid = self.cuboid
        
        # "Engage, Numba One!..."
        self.vessel.step(step, cur_cuboid)

        # cleanup any hits
        self.remove_mines(step.hits, cur_cuboid)
            
        # now recompute dimensions and chars
        new_cuboid = self.compute_new_state(cur_cuboid)
        
        return (step, self.vessel, cur_cuboid) 

    def remove_mines(self, mines, cuboid):
        for mine in mines:
            print "removing hit mine: ", mine
            coords, char = mine
            x,y,z = coords
            cuboid.cube_space[x][y][z] = "."
            cuboid.mines = [m for m
                            in mines
                            if not coords == m[0]]
    
    def compute_new_state(self, cur_cuboid):
        vx,vy,vz = self.vessel.get_coordinates()

        cx,cy,cz = self.get_center(cur_cuboid.width,
                                   cur_cuboid.height,
                                   self.vessel.decent_level)
        # make new dotmap
        cw = cur_cuboid.width
        ch = cur_cuboid.height

        

        
        




            
           
    def center_vessel(self):
        #set ship's coordinates to center of 2d plane at decent level on 3d plane
        coords  = self.get_center(self.cuboid.width,
                                  self.cuboid.height,
                                  self.vessel.decent_level)

        self.vessel.x, self.vessel.y, self.vessel.z = coords
        
        print "sited vessal at coordinates :" + str((coords))
        
    def get_center(self,width, height, depth):
        # find cartesian center and decrement because we're zero indexed
        return (((width / 2)  + (width % 2)) - 1,
                ((height / 2) + (height % 2)) - 1,
                depth)



#Simulation().run()
