def revers():
    n = int(input())
    if n == 0:
        return print(n)
    elif n != 0:
        revers()
        print(n)


revers()
