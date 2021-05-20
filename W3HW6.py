import math
p, x, y = float(input()), float(input()), float(input())
t = x * 100 + y
i = t + (t * p/100)
d = i * 10**(-9)
r = int(i // 100)
k = int(i % 100)
print(r, k)
