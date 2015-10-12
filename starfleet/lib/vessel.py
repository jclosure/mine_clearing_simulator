from step import Step
from affordances import decent_rate

class Vessel:

    def __init__(self, name="Enterprise"):
        self.name = name
        # initialize defaults
        self.decent_level = 0
        self.x,self.y,self.z = 0,0,0
        
    def engage(self, steps_input, cuboid):
        steps = [Step(s) for s in steps_input]
        for step in steps:
            self.step(step, cuboid)
        
    def step(self, step, cuboid):
        print "running step: " + step.instructions
        
        #run the step's operations
        for operation in step.operations:
            op,instruction,arg = operation
            if op == "fire":
                pattern = arg
                step.hits = self.fire(pattern, cuboid, step)
            if op == "move":
                movement_calculator = arg[1]
                x,y = movement_calculator(self.x,self.y)
                self.move(x, y, cuboid)
                
        return step
    
    def fire(self, pattern, cuboid, step=None):
        name, offsets = pattern
        print "firing ", name, offsets
        hits = [mine for mine in cuboid.mines
                if self.hit_p(mine, offsets, cuboid)]
        return hits
         
    def hit_p(self, mine, shots, cuboid):
        ''' predicate to determine hits '''
        mx,my,mz = mine[0]
        for shot in shots:
            ox, oy = shot
            rx = self.x + ox
            ry = self.y + oy
            if rx == mx and ry == my:
                return True
        return False
    
    def move(self, x, y, cuboid):
        print "moving ship to new coordinates"
        self.decent_level = self.decent_level - decent_rate
        self.x, self.y, self.z = x, y, self.decent_level
        print "new coordinates ", self.get_coordinates()

    def get_coordinates(self):
        return (self.x,self.y,self.z)

