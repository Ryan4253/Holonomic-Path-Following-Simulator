from HolonomicChassis import HolonomicChassis
from PID import PID
from DiscretePath import DiscretePath
from Point import Point
import math
import matplotlib.pyplot as plt
from matplotlib import patches

class PurePursuit:
    def __init__(self, chassis, distPID, lookAheadRadius):
        self.chassis = chassis
        self.distPID = distPID
        self.lookAheadRadius = lookAheadRadius
        self.path = None
        self.pos = None
        self.target = None
        self.output = None
        self.pathX = []
        self.pathY = []
        self.motionX = []
        self.motionY = []

        self.prevIndex = 0

    def followPath(self, path, visualize = True):
        self.path = path
        self.distPID.reset()
        self.prevIndex = 0
        self.pathX = []
        self.pathY = []
        self.motionX = []
        self.motionY = []

        for i in range(self.path.size()):
            self.pathX.append(self.path[i].x)
            self.pathY.append(self.path[i].y)

        while(self.distPID.getError() > 0.01):
            self.pos = self.chassis.getPos()
            self.target = self.getLookAheadPoint(self.pos)
            self.output = self.distPID.step(self.pos.distTo(self.target), 0.01)
            self.chassis.setVector(self.output, self.pos.angleTo(self.target))
            self.chassis.step(0.01)

            self.motionX.append(self.pos.x)
            self.motionY.append(self.pos.y)

            if(visualize):
                self.draw()

        self.chassis.setVector(0, 0)
            
    def getLookAheadPoint(self, pos):
        if(pos.distTo(self.path[self.path.size()-1]) < self.lookAheadRadius):
            return self.path[self.path.size()-1]

        for i in range(self.prevIndex, self.path.size()-1):
            start = self.path[i]
            end = self.path[i+1]
            t = self.findIntersection(start, end, pos)

            if(t != None):
                self.prevIndex = i
                return self.path[i] + (self.path[i+1] - self.path[i]) * t

        return self.closestPoint(pos)

    def findIntersection(self, start, end, pos):
        d = end - start
        f = start - pos

        a = d.dot(d)
        b = 2 * (f.dot(d))
        c = f.dot(f) - self.lookAheadRadius * self.lookAheadRadius
        discriminant = b * b - 4 * a * c

        if discriminant > 0:
            dis = math.sqrt(discriminant)
            t1 = ((-b - dis) / (2 * a))
            t2 = ((-b + dis) / (2 * a))

            if t2 >= 0 and t2 <= 1:
                return t2
            
            elif t1 >= 0 and t1 <= 1:
                return t1

        return None

    def closestPoint(self, pos):
        return min(self.path.path, key = lambda node : node.distTo(pos))

    def getIntersection(self):
        return self.intersectionPt

    def draw(self):
        plt.cla()
        plt.title("Pure Pursuit")
        plt.axis('square')
        plt.xlabel('X (Feet)')
        plt.ylabel('Y (Feet)')
        plt.xlim(0, 5, auto = False)
        plt.ylim(0, 5, auto = False)

        plt.plot(self.pathX, self.pathY, 'b')
        plt.plot(self.motionX, self.motionY, 'r')
        plt.plot(self.pos.x, self.pos.y, 'ro')
        plt.plot(self.target.x, self.target.y, 'go')
        plt.gca().add_patch(patches.Circle((self.pos.x, self.pos.y), self.lookAheadRadius, color='k', fill = False))
        plt.pause(0.01)
        

    