def sum1(n):
    global m
    n = int(input())
    m += n
    if n == 0:
        return m
    return sum1(m)

m = int(input())
if m == 0:
    print(0)
else:
    k = sum1(m)
    print(k)
