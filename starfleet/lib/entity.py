
from copy import deepcopy

class Entity:

    def __str__(self):
        return self.render()
        
    def __repr__(self):
        return self.__str__()
    
    def clone(self):
        return deepcopy(self)
