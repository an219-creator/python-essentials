n = int(input())
n1 = n//(10**2)
n2 = n % 100
n2_1 = n2//10
n2_2 = n2 % 10
r = n2_2 * 10 + n2_1
t = (r - n1 - 1) * (-1)
print(t)
