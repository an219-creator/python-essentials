def lagrange(x, n):
    y = int(x ** 0.5)
   # print('d =', x, y, n)
    if x - y ** 2 == 0:
      #  print('d1 =', x, y, n)
        return y
    elif n == 1:
        return -1

    while lagrange(x - y ** 2, n - 1) == -1:
     #   print('d2 =', x, y, n)
        y -= 1
        if y == 0:
            return -1
    print(y, sep=' ', end=' ')
   # print('d3 =', x, y, n)
    return lagrange(x - y ** 2, n - 1)

m = int(input())
n = 4
lagrange(m, n)
