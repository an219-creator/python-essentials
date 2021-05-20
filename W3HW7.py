import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
x1 = (-b - d ** (0.5)) / (2 * a)
x2 = (-b + d ** (0.5)) / (2 * a)
x1 = x2 = -b / (2 * a)
if a != 0:
    if d < 0:
        print('')
    else:
        x1 = (-b - d ** (0.5)) / (2 * a)
        x2 = (-b + d ** (0.5)) / (2 * a)
        if x1 == x2:
            print(x2)
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            print(x1, x2)
