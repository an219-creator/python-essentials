a = int(input())
b = int(input())
n1 = a % b
n2 = (n1 - 1) * (-1)
n3 = (n2 - 1) * (-1)
n4 = 'NO' * n3
print('YES' * n2, n4[:2], sep='')
