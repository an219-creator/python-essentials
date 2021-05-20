n = int(input())
t = n % 10
is1 = 10 <= n <= 20
is2 = 5 <= t <= 9
is3 = t == 0
is4 = t == 1
if is1 or is2 or is3:
    print(n, 'korov')
elif is4:
    print(n, 'korova')
else:
    print(n, 'korovy')
