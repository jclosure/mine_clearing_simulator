import sys
import contextlib
import ipdb
import os


# our modules
import cuboid
import grid
import step
import vessel
import computer
import scoring

import logger
import logging as log

# for easy debugging in ipython, do this: %load_ext autoreload
# we do this trick to turn off module caching for the REPL
try:
    reload
except NameError:
    # Python 3
    from imp import reload

reload(cuboid)
reload(step)
reload(vessel)
reload(grid)
reload(computer)
reload(scoring)

# our domain
Cuboid = cuboid.Cuboid
Step = step.Step
Vessel = vessel.Vessel
Grid = grid.Grid
Scoring = scoring.Scoring

class Simulation:

    # file sentinals
    default_cuboid_file =  "./test_input/cuboid.dat"
    default_steps_file = "./test_input/student_minesweeping_script.steps"
    
    def __init__(self, cuboid_file=default_cuboid_file,steps_file=default_steps_file):
        log.info("creating new simulation")
        
        # replay
        self.history = []
        self.steps = []

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

        # run the sim:
        
        # 1. map over the steps
        self.history = self.history + map(lambda step_input:
                                              self.step(step_input),
                                              self.step_inputs)
        # 2. output results to file
        
        # keep score
        score = Scoring(self)
        score.compute_score()
        score.print_output(self.steps_file_output)
        
    def step(self, step_input):

        
        
        print "----------- START STEP -----------------"
        
        # create step operations
        step = Step(step_input)

        # ship operates in the cuboid
        self.vessel.step(step, self.cuboid)
        
        # cleanup any hits
        self.cuboid.sweep_mines(step.hits)

        # manual control
        #step.swept_face = Cuboid(self.cuboid.render())
        
        # flash freeze and stash the universe
        prev_cuboid = self.cuboid.clone()

        # now recompute state
        try:
            self.recompute_cuboid(step)
        except Exception as ex:
            print ex
            
        # collect all the good stuff
        prev_step = [s for s in reversed((self.steps or [None]))][0]
        event_data = (self.vessel.clone(),
                      prev_step,
                      step,
                      prev_cuboid,
                      self.cuboid)
        
        self.steps.append(step)
        
        return event_data

    print "----------- END STEP -----------------"

    
    def recompute_cuboid(self, step):

        cuboid_face = self.cuboid.render()

        # attach adjusted face and dims to step
        
        step.untrimmed_face = cuboid_face
        step.trimmed_face, step.grown_face = self.generate_faces(cuboid_face)
       
        print "UNTRIMMED: \n",  cuboid_face

        
        
        if cuboid_face:  
            self.initialize_cuboid(self.cuboid.render(),
                                   self.vessel.decent_rate,
                                   self.vessel.decent_level)
            
       

        
    
    def generate_faces(self, face):

        ## this is here to enable breaking on a specific step during debugging
        # last = self.vessel.steps[-1]
        # if last and last.instructions == "south":
        #     ipdb.set_trace()
        
         # get all mine coords
        mine_coords = [mine[0] for mine in self.cuboid.mines]
        # add the ship's coords
        coords = mine_coords + [self.vessel.get_coordinates()]

        print "OBJECT COORDS: ", coords

        west_edge, east_edge, south_edge, north_edge = computer.smallest_rectangle(coords)

        print "EDGES: ",  west_edge, east_edge, south_edge, north_edge
        
        g = Grid(face)
        
        western_offset = abs(0 - west_edge[1])
        eastern_offset =  abs(g.width - 1 - east_edge[1])
        northern_offset = abs(g.height - 1 - north_edge[1])
        southern_offset = abs(0 - south_edge[1])

        print "TRIM OFFSETS:", "west:", western_offset, "east:", eastern_offset, "north:", northern_offset, "south:", southern_offset
        
        g.shrink_west(western_offset)
        g.shrink_east(eastern_offset)
        g.shrink_north(northern_offset)
        g.shrink_south(southern_offset)
    
        trimmed_face =  g.render()
        print "TRIMMED: \n", trimmed_face

        # # now grow:
        xends = (west_edge[1], east_edge[1])
        yends = (south_edge[1], north_edge[1])

        ## this is here to enable breaking on a specific step during debugging
        # last = self.vessel.steps[-1]
        # if last and last.instructions == "south":
        #     ipdb.set_trace()

        # get the vessel coords for growing face
        vcoords = self.vessel.get_coordinates()
        xpos,ypos,zpos = vcoords
        
        grown_face = g.grow_face(trimmed_face, xends, yends, (xpos, ypos)) 

        print "GROWN: \n", grown_face
        
        return (trimmed_face, grown_face)

    
    def initialize_vessel(self):
        
        # use the file to name our ship
        ship_name = self.cuboid_file.split("_")[0]

        # initialize vessel
        self.vessel = Vessel(ship_name)
        self.center_vessel()

        
    def initialize_flight_plan(self, step_inputs=None):

        if step_inputs is None:
            self.script_input = open(self.steps_file, "r").read()
            self.step_inputs = self.script_input.split("\n")
            self.steps_file_output = self.steps_file + ".out"
            os.remove(self.steps_file_output) if os.path.exists(self.steps_file_output) else None
  
        else:
            #note we're going to pass in the script as a string here..
            self.step_inputs = step_inputs.read().split("\n")

            
    def initialize_cuboid(self, cuboid_input=None, decent_rate=0, decent_level=0):

        # read inputs
        if cuboid_input is None:
            self.field_input = open(self.cuboid_file, "r").read()
            self.cuboid_input = self.field_input
        else:
            self.cuboid_input = cuboid_input
            
        print "initializing cuboid at decent_level: ", decent_level
        
        self.cuboid = Cuboid(self.cuboid_input, decent_rate * -1)

        
    def center_vessel(self):

        #set ship's coordinates to center of 2d plane at decent level on 3d plane
        coords  = self.cuboid.get_central_coordinates()

        self.vessel.x, self.vessel.y, middle  = coords
        self.vessel.z = 0
        
        print "sited vessal at coordinates :" + str((self.vessel.x, self.vessel.y, self.vessel.z))



        

def run():
    Simulation().engage()
