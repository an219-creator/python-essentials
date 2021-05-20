x = int(input())
cnt = 1
cnt1 = 1
prev = x
while x != 0:
    x = int(input())
    if x == 0:
        cnt = max(cnt1, cnt)
        print(cnt)
        break
    elif x != prev:
        prev = x
        if cnt1 <= cnt:
            cnt1 = cnt
        cnt = 1
    elif x == prev:
        cnt += 1
