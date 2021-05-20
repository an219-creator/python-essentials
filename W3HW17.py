import math
p, x, y, k = float(input()), float(input()), float(input()), float(input())
t = x * 100 + y
j = 1
while j <= k:
    t = int(t + (t * p)/100)
    j += +1
d = t * 10**(-9)
r = int(t // 100)
k1 = int(t % 100)
print(r, k1)
