import math


def IsPointInCircle(x, y, xc, yc, r):
    return ("YES" if (x - xc) ** 2 + (y - yc) ** 2 <= r * r else "NO")

a, b, c, d, f = float(input()), float(input()), float(input()),\
                float(input()), float(input())
print(IsPointInCircle(a, b, c, d, f))
