import random

class Wandering:
    
    def __init__(self, name, x=0, y=0):
         self.name = name
         self.x = x
         self.y = y
         
    def position(self):
        return (self.x, self.y)
    
    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5

class ComunWandering(Wandering):

    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy =  random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.x += dx
        self.y += dy
        return [dx,dy]

class CrazyWandering(Wandering):

    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy =  random.choice([(0, 3), (0, -3), (3, 0), (-3, 0)])
        self.x += dx
        self.y += dy
        return [dx,dy]
    
class RightWandering(Wandering):

    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy =  random.choice([(0,5), (5,0), (-1,0), (0,-1)])
        self.x += dx
        self.y += dy
        return [dx,dy]
    
class LeftWandering(Wandering):

    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy =  random.choice([(0,1), (1,0), (-5,0), (0,-5)])
        self.x += dx
        self.y += dy
        return [dx,dy]
    