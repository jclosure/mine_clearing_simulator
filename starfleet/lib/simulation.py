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

    # file sentinals
    default_cuboid_file =  "./test_input/cuboid.dat"
    default_steps_file = "./test_input/student_minesweeping_script.steps"
    
    def __init__(self, cuboid_file=default_cuboid_file,steps_file=default_steps_file):
        print "creating new simulation"

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

        # run the steps (pythonic event-sourcing)
        self.history = self.history + map(lambda step_input:
                                              self.step(step_input),
                                              self.step_inputs)
        
        
    def step(self, step_input):
        step = Step(step_input)
        
        # "Engage, Numba One!..."
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

        #TODO:!!!!
        # noop for now
        return self.cuboid

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

    def initialize_cuboid(self, cuboid_input=None):

        ''' cheeky generate cuboid '''

        # read inputs
        if cuboid_input is None:
            self.cuboid_input = open(self.cuboid_file, "r").read()
        else:
            self.cuboid_input = cuboid_input

        # initialize cuboid and vessel state 
        self.cuboid = Cuboid(self.cuboid_input)



    # OLD CARGO NEED TO GO THROUGH
        
    # def compute_new_state(self, cur_cuboid):
    #     vx,vy,vz = self.vessel.get_coordinates()

    #     cx,cy,cz = self.get_center(cur_cuboid.width,
    #                                cur_cuboid.height,
    #                                self.vessel.decent_level)

    #     ncenter = (vx, vy, vz)

    #     # make new dotmap
    #     cheight = cur_cuboid.height
    #     cwidth = cur_cuboid.width
        

    #     # measure the distance between the vessel and the current 

    #     c_north_edge = cheight - 1
    #     c_south_edge = 0
    #     c_east_edge = cwidth - 1
    #     c_east_edge = 0

    #     cndiff = ('north_diff', ncenter - c_north_edge)
    #     csdiff = ('south_diff',ncenter - c_south_edge)
    #     cediff = ('east_diff', ncenter - c_east_edge)
    #     cwdiff = ('west_diff', ncenter - c_west_edge)

    #     cdiffs = [cndiff,csdiff,cediff,cwdiff]
    #     longest_cdiff = reduce(lambda highest,current: current
    #                            if current > highest
    #                            else highest, cdiffs)

    #     # now make extend or shrink each axis accordingly,
    #     # if there is a mine at a distance greater than
    #     # the cdiff, that edge changes and it's peer edge
    #     # must be expanded to keep the ship centered
    #     # do this on both dimensions.
        
    #     # # current furthes mine axis values
    #     # north_most_mine = cur_cuboid.most_north_mine()
    #     # south_most_mine = cur_cuboid.most_south_mine()
    #     # east_most_mine = cur_cuboid.most_east_mine()
    #     # west_most_mine = cur_cuboid.most_west_mine()
        
        
    #     # current furthes mine axis values
    #     m_north_edge = cur_cuboid.most_north_mine()[0][1]
    #     m_south_edge = cur_cuboid.most_south_mine()[0][1]
    #     m_east_edge = cur_cuboid.most_east_mine()[0][0]
    #     m_west_edge = cur_cuboid.most_west_mine()[0][0]

    
        
        
             
    #     # # new dimensions
    #     # nheigth_d = abs(north_edge) - abs(south_edge)
    #     # nwidth_d = abs(east_edge) - abs(west_edge)

    #     # nheigth = cheight - nheigth_d
    #     # nwidth = cwidth - nwidth_d

        
    #     ## figure this out by looking at the successful exemplar's moves
    #     ## vx_center = nwidth - (nwidth / vx)

        
        
    #     ## need to push out or pull in to ensure the ship is at the center of the new 
        
    #     # new center
    #     # ncenter = self.get_center(nwidth, nheigth, ndepth)

    #     # # compute the adjustments to the sited elements
    #     # ny_offset =  abs(cheight) - abs(nheigth)
    #     # nx_offset =  abs(cwidth) - abs(nwidth) 

        
    #     # ensure odd dimensions
    #     if nheigth % 2 == 0:
    #         nheigth = nheigth + 1
    #     if nwidth % 2 == 0:
    #         nwidth = nwidth + 1

        
    #     # compute the new positions of the mines
    #     nmines = []
    #     for mine in cur_cuboid.mines:
    #         coords, char = mine
    #         x,y,z = coords
    #         # computing new mine coordinates and a new char
    #         nmine = ((x-nx_offset, y-ny_offset, z+1), cur_cuboid.z_map[z+1])
    #         nmines.append(nmine)

           
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
