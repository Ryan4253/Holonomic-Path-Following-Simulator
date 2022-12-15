from PID import PID
from HolonomicChassis import HolonomicChassis
from Point import Point
import math
import matplotlib.pyplot as plt

drivePID = PID(2, 0, 0)
chassis = HolonomicChassis(3, 1, 1)
target = Point(0, 4)

for i in range(200):
    pos = chassis.getPos()
    output = drivePID.step(pos.distTo(target), 0.01)
    chassis.setVector(output, pos.angleTo(target))
    chassis.step(0.01)

    plt.cla()
    plt.plot(pos.x, pos.y, 'bo')
    plt.plot(target.x, target.y, 'ro')
    plt.ylim(0, 10, auto = False)
    plt.xlim(0, 10, auto = False)
    plt.pause(0.001)


    
