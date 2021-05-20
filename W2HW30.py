a = int(input())
f = 0
i = 0
prev1 = 0
prev2 = 0
while i >= 0:
    if i == 1:
        prev2 = 1
        f = 1
    elif i == 2:
        prev1 = 1
        f = 1
    elif i > 2:
        f = prev2 + prev1
        prev2 = prev1
        prev1 = f
    if a == f:
        print(i)
        break
    elif a < f:
        print('-1')
        break
    i += 1
