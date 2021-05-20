n = int(input())
f = 0
i = 0
prev1 = 0
prev2 = 0
while i <= n:
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
    i += 1
print(f)
