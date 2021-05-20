s = input()
s1 = s.find(' ')
t1 = s[:s1]
t2 = s[s1 + 1:]
t = t2 + ' ' + t1
print(t)
