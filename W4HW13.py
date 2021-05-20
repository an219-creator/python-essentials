def lagrange(x, n):
    y = int(x ** 0.5)
    if x - y ** 2 == 0:
        return y
    if n == 1:
        return -1
    while lagrange(x - y ** 2, n - 1) == -1:
        y -= 1
        if y == 0:
            return -1
    print(y, sep=' ', end=' ')
    return lagrange(x - y ** 2, n - 1)

m = int(input())
n = 4
print(lagrange(m, n))
