import math


def IsPointInSquare(x, y):
    r1 = -1 <= x <= 1 and -1 <= y <= 1
    return r1

a, b = float(input()), float(input())
r = IsPointInSquare(a, b)
if r is True:
    print('YES')
else:
    print('NO')
