s = input()
s1 = s.find('h')
t = s[::-1]
s2 = t.find('h')
s3 = len(s) - s2 - 1
it = s[:s1] + s[s3 + 1:]
print(it)
