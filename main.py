from PID import PID
from HolonomicChassis import HolonomicChassis
from Point import Point
from DiscretePath import DiscretePath
from Bezier import Bezier
import math
import matplotlib.pyplot as plt
"""
# Chassis Test
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
"""

# Pathing Test
path = Bezier([Bezier.Knot(0, 0, 0, 2), Bezier.Knot(4, 4, math.pi/2, 2)]).generate_by_length(0.5)
x = []
y = []
for i in range(path.size()):
    x.append(path[i].x)
    y.append(path[i].y)

plt.plot(x, y, 'b')
plt.show()




    
