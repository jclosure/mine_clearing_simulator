from affordances import navigation
from affordances import firing_patterns
from copy import deepcopy
import ipdb
from entity import Entity

class Step(Entity):
    
    def __init__(self, instructions):
        self.instructions = instructions
        self.operations = []
        self.hits = []
        self.lex()


    def lex(self):

        ''' kung-fu projection with comprehension generators '''
        
        self.operations

        # probe affordances for lexical dispatchers
        for instruction in self.instructions.split():
            
            resolved = next((("move", instruction, nav)
                             for nav in navigation
                             if nav[0]==instruction), None)
            
            if  resolved is None:
                resolved = next((("fire", instruction, pat)
                                for pat in firing_patterns
                                if pat[0]==instruction), None)
            self.operations.append(resolved)
            

        self.operations = filter(lambda x: x is not None, self.operations) 
        
  
    def render(self):
        return str((self.instructions, self.operations, self.hits))
