a, b, c = float(input()), float(input()), float(input())
s = 0
p = (a + b + c)/2
s = ((p - a) * (p - b) * (p - c) * p) ** 0.5
print(s)
