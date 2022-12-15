from Rotation import Rotation
from Point import Point

def circumradius(A, B, C):
    a = B.distTo(C)
    b = C.distTo(A)
    c = A.distTo(B)

    a2 = a**2
    b2 = b**2
    c2 = c**2

    pa = A * (a2 * (b2 + c2 - a2) / ((b+c)*(b+c)-a2) / (a2-(b-c)*(b-c)))
    pb = B * (b2 * (a2 + c2 - b2) / ((a+c)*(a+c)-b2) / (b2-(a-c)*(a-c)))
    pc = C * (c2 * (a2 + b2 - c2) / ((a+b)*(a+b)-c2) / (c2-(a-b)*(a-b)))

    center = pa + pb + pc

    return center.distTo(A)