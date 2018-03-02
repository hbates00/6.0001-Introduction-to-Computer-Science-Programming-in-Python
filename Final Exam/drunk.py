import random

# Study code, already posted as Lecture 13 code
#################################################
### DO NOT MODIFY THESE CLASSES AND FUNCTIONS ###
#################################################
class Location(object):
     def __init__(self, x, y):
         """x and y are floats"""
         self.x = x
         self.y = y

     def move(self, deltaX, deltaY):
         """deltaX and deltaY are floats"""
         return Location(self.x + deltaX, self.y + deltaY)

     def getX(self):
         return self.x

     def getY(self):
         return self.y

     def distFrom(self, other):
         ox = other.x
         oy = other.y
         xDist = self.x - ox
         yDist = self.y - oy
         return (xDist**2 + yDist**2)**0.5

     def __str__(self):
         return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Drunk(object):
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
     def takeStep(self):
         stepChoices =\
             [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
         return random.choice(stepChoices)

class ColdDrunk(Drunk):
     def takeStep(self):
         stepChoices = [(0,0.9), (0,1.1), (1, 0), (-1, 0)]
         return random.choice(stepChoices)

class Field(object):
     def __init__(self):
         self.drunks = {}

     def addDrunk(self, drunk, loc):
         if drunk in self.drunks:
             raise ValueError('Duplicate drunk')
         else:
             self.drunks[drunk] = loc

     def moveDrunk(self, drunk):
         if not drunk in self.drunks:
             raise ValueError('Drunk not in field')
         xDist, yDist = drunk.takeStep()
         currentLocation = self.drunks[drunk]
         #use move method of Location to get new location
         self.drunks[drunk] = currentLocation.move(xDist, yDist)

     def getLoc(self, drunk):
         if not drunk in self.drunks:
             raise ValueError('Drunk not in field')
         return self.drunks[drunk]

class OddField(Field):
     def moveDrunk(self, drunk):
         if not drunk in self.drunks:
             raise ValueError('Drunk not in field')
         xDist, yDist = drunk.takeStep()
         currentLocation = self.drunks[drunk]
         #use move method of Location to get new location
         self.drunks[drunk] = currentLocation.move(xDist, yDist)
         locSums = self.drunks[drunk].getX() + self.drunks[drunk].getY()
         if locSums%5 < 1:
             self.drunks[drunk] = Location(0, 0)

def walk(f, d, numSteps):
     """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
        Moves d numSteps step times, and returns the difference between
        the final location and the location at the start of the walk."""
     start = f.getLoc(d)
     for s in range(numSteps):
         f.moveDrunk(d)
     return(start.distFrom(f.getLoc(d)))


class NewField(Field):
    def __init__(self):    
        """ initializes a new field """
        Field.__init__(self)
        self.stuckdrunks = []
        
    def getDrunks(self):
        """ returns the drunks in the field"""
        the_drunks = self.drunks.keys()
        return the_drunks

    def moveDrunk(self, drunk):
        """ Moves drunk one step from its current location. 
            Assume the origin is Location(0, 0).
            If a drunk lands on a location that is more than 3 units 
            from the origin and already has a drunk on it, that 
            location becomes sticky and no drunk on that location 
            ever moves again. If a drunk moves to a location that 
            is already sticky, that drunk gets stuck too."""
        origin = Location(0,0)
        locations = self.drunks.copy().values()
        
        if drunk in self.stuckdrunks:
            pass
        else:
            self.moveDrunk(drunk)
            if (self.getLoc(drunk) in locations) and (origin.distFrom(self.getLoc(drunk)) > 3):
                self.stuckdrunks.append(drunk)
            else:
                pass
                
    def __str__(self):
        return str(self.drunks)
        
        
        
##############################################################################
'''
class NewField(Field):
    def __init__(self):    
        """ initializes a new field """
        Field.__init__(self)
        self.stuckdrunks = []
        
    def getDrunks(self):
        """ returns the drunks in the field"""
        the_drunks = self.drunks.copy()
        return the_drunks

    def moveDrunk(self, drunk):
        """ Moves drunk one step from its current location. 
            Assume the origin is Location(0, 0).
            If a drunk lands on a location that is more than 3 units 
            from the origin and already has a drunk on it, that 
            location becomes sticky and no drunk on that location 
            ever moves again. If a drunk moves to a location that 
            is already sticky, that drunk gets stuck too."""
        if drunk in self.stuckdrunks:
            pass
        pre = self.drunks.copy()
        locations = pre.values()
        self.moveDrunk(drunk)
        if self.drunks[drunk] in locations:
            self.stuckdrunks.append[drunk]
            
    def __str__(self):
        return str(self.drunks)
        '''