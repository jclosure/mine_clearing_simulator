from cStringIO import StringIO

# stub module

class Scoring:

    # static
    eol = "\n"

    def __init__(self, simulation):

        self.sim = simulation


        
    def compute_score(self):
        
        ''' some logic will go here '''

        # note that we're passing in the event-sourced history spool with the sim.
        # it is a rich set of tuples containing:
        # step -> vessel -> prev_cuboid -> cur_cuboid (including hit mines, etc..)
        
        # implement the scoring rules outlined in the game directions

        # we'll mock the sim for testing this..

        self.score = "todo:.."
        return self.score

    
    # big long excruciatingly pedantic print formatter :)
    
    def print_output(self, output_file_path):

        builder = StringIO()

        ## header - print inputs
        
        # print steps file (script file)

        builder.write("FIELD FILE:")

        builder.write(self.eol)
        builder.write(self.eol)
        
        builder.write(self.sim.field_input)

        builder.write(self.eol)
        builder.write(self.eol)
        
        # print cuboid file (field file)

        builder.write("SCRIPT FILE:")

        builder.write(self.eol)
        builder.write(self.eol)
        
        builder.write(self.sim.script_input)

        builder.write(self.eol)
        builder.write(self.eol)

        ## body - print output
        
        builder.write("OUPUT:")

        builder.write(self.eol)
        builder.write(self.eol)

        for idx,stack_frame in enumerate(self.sim.history):

            vessel, prev_step, step, prev_cuboid, cuboid = stack_frame

            # print step number
            builder.write("step " + str(idx + 1) )
            
            builder.write(self.eol)
            builder.write(self.eol)

            # print prev step's grid
            if prev_step:
                builder.write(prev_step.grid.render())
            else:
                builder.write(self.sim.script_input)

            builder.write(self.eol)
            builder.write(self.eol)
                
            # print instructions
            builder.write(step.instructions)

            builder.write(self.eol)
            builder.write(self.eol)

            # print result cuboid
            builder.write(step.grid.render())

            builder.write(self.eol)
            builder.write(self.eol)

        ## print fass/fail (score)
        builder.write(self.eol)
        builder.write("pass/fail (stubbed)")

        # write it all out
        output = builder.getvalue()
        
        with open(output_file_path, 'a') as output_file:
            output_file.write(output)

        print "\n\nOUTPUT FILE AVAILABLE AT: ", output_file_path
        
