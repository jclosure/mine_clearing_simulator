import sys
import contextlib
import ipdb
import os
from cStringIO import StringIO

# our modules
import cuboid
import grid
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
reload(grid)
reload(computer)

# our domain
Cuboid = cuboid.Cuboid
Step = step.Step
Vessel = vessel.Vessel
Grid = grid.Grid

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
       
        self.spool_output()    
        
    def step(self, step_input):

        print "----------- START STEP -----------------"
        
        # create step operations
        step = Step(step_input)
        
        # ship operates in cuboid
        self.vessel.step(step, self.cuboid)
        
        # cleanup any hits
        self.cuboid.sweep_mines(step.hits)

        # flash freeze and stash the universe
        last_cuboid = self.cuboid.clone()

        # now recompute state
        try:
            self.recompute_cuboid()
        except Exception as ex:
            print ex
            
        # collect all the good stuff
        return (step, self.vessel, last_cuboid, self.cuboid) 

    def recompute_cuboid(self):

        cuboid_face = self.cuboid.render()

        print "untrimmed face: \n" + cuboid_face

        cuboid_face = self.trim_face(cuboid_face)
        print "trimmed face: \n" + cuboid_face

        cuboid_face = self.grow_face(cuboid_face)
        print "grown face: \n" + cuboid_face

       
        self.initialize_cuboid(cuboid_face,
                               self.vessel.decent_rate,
                               self.vessel.decent_level)

        print "----------- END STEP -----------------"
        
    def trim_face(self, face):

         # get all mine coords
        mine_coords = [mine[0] for mine in self.cuboid.mines]
        # add the ship's coords
        coords = mine_coords + [self.vessel.get_coordinates()]

        print "OBJECT COORDS: ", coords

        west_edge, east_edge, south_edge, north_edge = computer.smallest_rectangle(coords)

        print "EDGES: ",  west_edge, east_edge, south_edge, north_edge
        
        g = Grid(face)

        western_offset = abs(west_edge[1])
        eastern_offset = abs(g.width - east_edge[1] - 1)
        northern_offset = abs(g.height - north_edge[1] - 1)
        southern_offset = abs(south_edge[1])

        print "OFFSETS: ", western_offset, eastern_offset, northern_offset, southern_offset

        # GOOD
        g.shrink_west(western_offset)
  
        g.shrink_east(eastern_offset)
  
        g.shrink_north(northern_offset)
   
        # todo: ...
        # g.shrink_south(southern_offset)
    
        new_face = g.render()

        return new_face

    def grow_face(self, face):
        #todo: ..
        return face
        
    def initialize_vessel(self):
        
        # use the file to name our ship
        ship_name = self.cuboid_file.split("_")[0]

        # initialize vessel
        self.vessel = Vessel(ship_name)
        self.center_vessel()
    
    def initialize_flight_plan(self, step_inputs=None):

        if step_inputs is None:
            self.step_inputs = open(self.steps_file, "r").read().split("\n")
            self.steps_file_output = self.steps_file+ ".out"
            os.remove(self.steps_file_output) if os.path.exists(self.steps_file_output) else None
  
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
        self.vessel.z = 0
        
        print "sited vessal at coordinates :" + str((self.vessel.x, self.vessel.y, self.vessel.z))
        

    def spool_output(self):
         # spit out the simulation results
        with open(self.steps_file_output, 'a') as output_file:
            initial = None
            for stack_frame in self.history:
                step, vessel, prev_cuboid, curr_cuboid = stack_frame
                if initial is None:
                    output_file.write(self.render_stack_frame(step, vessel, prev_cuboid))
                    output_file.write(self.render_stack_frame(step, vessel, curr_cuboid))
                    initial = True
                else:
                    output_file.write(self.render_stack_frame(step, vessel, curr_cuboid))
        
    def render_stack_frame(self, step, vessel, cuboid):
        builder = StringIO()
        builder.write("-------------")
        builder.write(cuboid.render())
        return builder.getvalue()
        
        
