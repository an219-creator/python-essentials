x = int(input())
maxX = x
prev = 0
while x != 0:
    x = int(input())
    if x == 0:
        print(prev)
        break
    elif x > maxX:
        prev = maxX
        maxX = x
    elif x < maxX and x >= prev:
        prev = x
    elif maxX == x and x >= prev:
        prev = x
