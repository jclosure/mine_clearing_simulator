

class Vessel:

    x,y,z = 0,0,0
    
    decent_rate = 1
    decent_level = 0
    
    def __init__(self, name="Enterprise"):
        self.name = name

    def engage(self, step, cuboid):

        #do optional move and/or fire
        if not step.move is None:
            x,y = step.move[1](self.x,self.y)
            self.move(x, y, cuboid)
        if not step.firing_pattern is None:
            name, pattern = step.firing_pattern
            self.fire(name, pattern)
            
    def fire(self, name, pattern):
        print ("firing " + name)
        print pattern
        for attempt in pattern:
            self.find_hits(attempt)
        
        
    def move(self, x, y, cuboid):
        print "moving ship to new coordinates"
        self.decent_level = self.decent_level - self.decent_rate
        self.x, self.y, self.z = x, y, self.decent_level
        print "new coordinates ", self.get_coordinates()

    def find_hits(self, attempt):
        attempt_x, attempt_y = attempt

    def get_coordinates(self):
        return (self.x,self.y,self.z)
