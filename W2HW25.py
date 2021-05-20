x = int(input())
cnt = 0
if x % 2 == 0 and x != 0:
    cnt = 1
while x != 0:
    x = int(input())
    if x == 0:
        continue
    elif x % 2 == 0:
        cnt = cnt + 1
print(cnt)

