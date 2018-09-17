a = 0
b = 1
n = int(input('enter any number:'))
for i in range(n):
    if i == 0:
        continue
    if a < n:
        print(a)
        a, b = b, a+b
    else:
        break