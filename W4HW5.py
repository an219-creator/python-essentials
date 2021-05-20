import math


def MinDivisor(b):
    i = 2
    k = int(n ** 0.5)
    while i <= n:
        t = n % i
        if t == 0:
            return i
        elif i > k:
            return n
        else:
            i += 1
n = int(input())
print(MinDivisor(n))
