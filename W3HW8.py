a, b, c, d, e, f = float(input()), float(input()), float(input()), \
                   float(input()), float(input()), float(input())
if a != 0.00 and (d * a - c * b) != 0.00:
    y = (f * a - c * e)/(d * a - c * b)
    x = (e - b * y)/a
    print(x, y)
elif a == 0.00 and b != 0 and c != 0:
    y = e/b
    x = (f - (d * e)/b)/c
    print(x, y)
