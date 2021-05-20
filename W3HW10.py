s = input()
s1 = s.find('f')
t = s[::-1]
s2 = t.find('f')
s3 = len(s) - s2 - 1
if s1 != -1 or s2 != -1:
    if s1 == -1:
        s1 = ''
    if s2 == -1:
        s2 = ''
    if s1 == s3:
        print(s1)
    else:
        print(s1, s3)
