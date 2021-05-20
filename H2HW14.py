a = int(input())
b = int(input())
c = int(input())
if a <= b <= c:
    print(a, b, c)
elif b <= a <= c:
    (a, b) = (b, a)
    print(a, b, c)
elif a <= c <= b:
    (b, c) = (c, b)
    print(a, b, c)
elif c <= a <= b:
    (a, b, c) = (c, a, b)
    print(a, b, c)
elif b <= c <= a:
    (a, b, c) = (b, c, a)
    print(a, b, c)
elif c <= b <= a:
    (a, b, c) = (c, b, a)
    print(a, b, c)
else:
    print(a, b, c)
