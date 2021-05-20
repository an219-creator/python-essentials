x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
isR1 = x2-x1 == 1
isR2 = y2-y1 == 1
isR3 = x1-x2 == 1
isR4 = y1-y2 == 1
isR5 = y1-y2 == 0
isR6 = x1-x2 == 0
if (isR1 or isR3 or isR6) and (isR2 or isR4 or isR5):
    print('YES')
else:
    print('NO')
