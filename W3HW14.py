s = input()
s1 = s.count(' ')
if len(s) != 0:
    if s1 == 0:
        print('1')
    else:
        print(s1 + 1)
else:
    print(0)
