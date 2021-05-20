x = int(input())
maxX = x
while x != 0:
    x = int(input())
    if x == 0:
        break
    if x > maxX:
        maxX = x
print(maxX)
