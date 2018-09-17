a = 0
b = 1
n = int(input('enter any range:'))
for i in range(n):
    if a < n:
        print(a)
        a, b = b, a+b
    else:
        break

