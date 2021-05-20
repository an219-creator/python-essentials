s = input()
s1 = s.find('f')
if s1 != -1:
    s1 = s.find('f', s1 + 1)
    if s1 != -1:
        print(s1)
    else:
        print(-1)
else:
    print(-2)
