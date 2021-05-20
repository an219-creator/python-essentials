a = int(input())
b = int(input())
c = int(input())
if (c < a + b) or (a < c + b) or (b < c + a) and (a > 0 and b > 0 and c > 0):
    if ((c**2) == (a**2) + (b**2)) or ((a**2) == (c**2) + (b**2))\
            or ((b**2) == (c**2) + (a**2)):
        print('rectangular')
    elif ((c**2) > (a**2) + (b**2)) or ((a**2) > (c**2) + (b**2))\
            or ((b**2) > (c**2) + (a**2)):
        print('obtuse')
    elif ((c**2) < (a**2) + (b**2)) or ((a**2) < (c**2) + (b**2))\
            or ((b**2) < (c**2) + (a**2)):
        print('acute')
elif a <= 0 or b <= 0 or c <= 0:
    print('impossible')
else:
    print('impossible')
