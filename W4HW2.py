import math


def distance(x1, y1, x2, y2):
    r1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return r1

a, b, c, d = float(input()), float(input()), float(input()), float(input())
print(distance(a, b, c, d))
