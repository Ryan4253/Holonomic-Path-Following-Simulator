import math
import copy
from types import NoneType

class Rotation:
    # THIS IS IN RADIAN
    def __init__(self, a, b = None):
        if(isinstance(a, Rotation)):
            self.theta = copy.deepcopy(a.theta)
            self.sine = copy.deepcopy(a.sine)
            self.cosine = copy.deepcopy(a.cosine)

        elif(not isinstance(b, NoneType)):
            magnitude = math.sqrt(a**2 + b**2)
            if magnitude > 1e-6:
                self.sine = a / magnitude
                self.cosine = b / magnitude
            else:
                self.sine = 0.0
                self.cosine = 1.0
            self.theta = math.atan2(self.sine, self.cosine)

        else:
            self.theta = copy.deepcopy(a)
            self.sine = math.sin(self.theta)
            self.cosine = math.cos(self.theta)

    def __add__(self, rhs):
        return self.rotateBy(rhs)
        
    def __sub__(self, rhs):
        return self + (-rhs);

    def __mul__(self, scalar):
        return Rotation(self.theta * scalar)

    def __div__(self, scalar):
        return Rotation(self.theta / scalar)

    def __neg__(self):
        return Rotation(-self.theta)

    def __eq__(self, rhs):
        return self.theta == rhs.theta
    
    def __ne__(self, rhs):
        return self.theta != rhs.theta 

    def rotateBy(self, rhs):
        return Rotation(self.cosine * rhs.cosine - self.sine * rhs.sine, self.cosine * rhs.sine + self.sine * rhs.cosine)