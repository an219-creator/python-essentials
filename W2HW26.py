x = int(input())
maxX = x
prev = x
cnt = 1
while x != 0:
    x = int(input())
    if x == 0:
        break
    if x > maxX:
        maxX = x
        cnt = 0
    if maxX == x:
        cnt += 1
print(cnt)
