a, b = int(input()), int(input())
if a < b:
    for i in range(a, b + 1):
        print(i, sep=' ', end=' ')
elif a > b:
    for j in range(a, b - 1, -1):
        print(j, sep=' ', end=' ')
else:
    print(a)
