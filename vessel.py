

class Vessel:

    coordinates = (0,0,0)
    
    def __init__(self, name="Enterprise"):
        self.name = name
    def engage(self, instruction, cuboid):
        pass
    def fire(self, pattern):
        pass
    def move(self, new_coordinates, cuboid, move=None):
        "move ship to new coordinates"
        pass
    def fall(self):
        pass
