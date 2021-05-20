import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if a != 0 and b != 0:
    x1 = (-b - d ** (0.5)) / (2 * a)
    x2 = (-b + d ** (0.5)) / (2 * a)
    x1 = x2 = -b / (2 * a)
elif b != 0 and a == 0:
    x1 = (-c) / b
elif b == 0 and a != 0:
    x = (-c / a) ** (0.5)
if d < 0:
    print(0)
else:
    if a != 0 and b != 0:
        x1 = (-b - d**(0.5)) / (2 * a)
        x2 = (-b + d**(0.5)) / (2 * a)
        if x1 == x2:
            print(1, x2)
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            print(2, x1, x2)
    elif b != 0 and a == 0:
        x2 = (-c) / b
        print(1, x2)
    elif b == 0 and a != 0:
        x1 = (-c / a) ** (0.5)
        print(1, x1)
