import math
n = int(input())
x = float(input())
p = 0
prev = 0
i = 1
while i <= n + 1:
    j = float(input())
    if i < n + 1:
        p += j
        p *= x
    elif i == n + 1:
        p = p + j
    i += +1
print(p)
