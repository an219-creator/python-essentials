n = int(input())
flag = ('+___', ('|', n, ' /'), ('|__', "\\"), '|   ')
s1 = flag[1][0] + str(flag[1][1]) + flag[1][2]
s2 = flag[2][0] + flag[2][1]
for j in range(n):
    print(flag[0],end=' ')
for j in range(n):
    print(s1)
for j in range(n):
    print(s2)
for j in range(n):
    print(flag[3])