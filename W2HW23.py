x = int(input())
cnt = 0
if x != 0:
    cnt = 1
while x != 0:
    x = int(input())
    if x == 0:
        continue
    cnt = cnt + 1
print(cnt)
