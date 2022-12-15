from Point import Point
import math

class HolonomicChassis:
    def __init__(self, maxVelocity, x = 0, y = 0):
        self.x = x
        self.y = y
        self.maxVelocity = maxVelocity
        self.velocity = 0
        self.angle = 0

    def setVector(self, velocity, angle):
        self.velocity = max(min(velocity, self.maxVelocity), -self.maxVelocity)
        self.angle = angle
    
    def step(self, dt):
        self.x += (self.velocity * math.cos(self.angle)) * dt
        self.y += (self.velocity * math.sin(self.angle)) * dt

    def getPos(self):
        return Point(self.x, self.y)

