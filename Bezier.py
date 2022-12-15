from DiscretePath import DiscretePath
from Point import Point
from Rotation import Rotation
import math

class Bezier:
    class Knot:
        def __init__(self, x, y, angle, magnitude = 1):
            self.x = x
            self.y = y
            self.angle = angle
            self.magnitude = magnitude

    def __init__(self, waypoint):
        self.p1 = []
        self.p2 = []
        self.c1 = []
        self.c2 = []

        for i in range(len(waypoint)-1):
            point1 = Point(waypoint[i].x, waypoint[i].y)
            point2 = Point(waypoint[i+1].x, waypoint[i+1].y)
            self.p1.append(point1)
            self.p2.append(point2)
            self.c1.append(point1 + Point(waypoint[i].magnitude, Rotation(waypoint[i].angle)))
            self.c2.append(point2 + Point(waypoint[i+1].magnitude, Rotation(waypoint[i+1].angle-math.pi)))
    
    def getPoint(self, t):
        index = int(t * len(self.p1))
        t_ = t * len(self.p1) - index
        if(t == 1):
            index = len(self.p1) - 1
            t_ = 1
        return self.p1[index] * (1-t_)**3 + self.c1[index] * 3 * (1-t_)**2 * t_ + self.c2[index] * 3 * (1-t_) * t_**2 + self.p2[index] * t_**3
        
    def generate_by_size(self, step, end = True):
        ret = []
        inc = 1 / step
        for i in range(step):
            t = i * inc
            ret.append(self.getPoint(t))

        if(end):
            ret.append(self.getPoint(1))

        return DiscretePath(ret)
    
    def generate_by_length(self, length, end = True):
        totaldist = 0;
        for t in range (0, 100, 1):
            totaldist += self.getPoint(t / 100.0).distTo(self.getPoint(t / 100.0 + 0.01))
        
        distPerSegment = totaldist / math.ceil(totaldist / length)
        traversed = 0
        ret = [self.getPoint(0)]

        for t in range(0, 1000, 1):
            traversed += self.getPoint(t / 1000.0).distTo(self.getPoint(t / 1000.0 + 0.001))
            if(traversed >= distPerSegment):
                traversed = 0
                ret.append(self.getPoint(t/1000.0))

        if(ret[len(ret)-1].distTo(self.getPoint(1)) < distPerSegment / 2):
            ret.pop()

        if(end):
            ret.append(self.getPoint(1))

        return DiscretePath(ret)