m = int(input())
n = int(input())
k = int(input())
is1 = m * n
is2 = k % m == 0
is3 = k % n == 0
if (is2 or is3) and is1 >= k:
    print('YES')
else:
    print('NO')
