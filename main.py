from PID import PID
from HolonomicChassis import HolonomicChassis
from Point import Point
from Bezier import Bezier
from PurePursuit import PurePursuit

drivePID = PID(5, 0, 0)
chassis = HolonomicChassis(3, 0, 0)
pptenshi = PurePursuit(chassis, drivePID, 0.5)

path = Bezier([Bezier.Knot(0, 0, 0, 2), Bezier.Knot(4, 4, 3.14/2, 2)]).generate_by_length(0.1)
pptenshi.followPath(path)

chassis.setPos(0, 1.5)
path = Bezier([Bezier.Knot(0, 0, 0, 2), Bezier.Knot(4, 2, 0, 2)]).generate_by_length(0.1)
pptenshi.followPath(path)





    
