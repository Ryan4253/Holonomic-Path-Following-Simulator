import math
import copy
from Math import *

class DiscretePath:
    def __init__(self, waypoint):
        self.path = copy.deepcopy(waypoint)

    def __add__(self, rhs):
        ret = DiscretePath(self.path)
        if(isinstance(rhs, DiscretePath)):
            for point in rhs.path:
                ret.append(point)
        else:
            ret.append(rhs)
        
        return ret
    
    def __iadd__(self, rhs):
        if(isinstance(rhs, DiscretePath)):
            for point in rhs.path:
                self.path.append(point)
        else:
            self.path.append(rhs)
        
        return self

    def __getitem__(self, i):
        i = max(min(i,len(self.path)-1), 0)
        return self.path[i]

    def size(self):
        return len(self.path)
    
    def getCurvature(self, i):
        if i <= 0 or i > self.size():
            return 0.0

        radius = circumradius(self.path[i-1], self.path[i], self.path[i+1])

        if(math.isnan(radius)):
            return 0.0

        return 1 / radius;

    def print(self):
        for point in self.path:
            print("[", point.x, " ", point.y, "]")