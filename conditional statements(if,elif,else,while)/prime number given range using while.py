n = int(input('enter any number:'))
i = 2
while i < n:
    if n % i == 0:
        print("not a prime number")
        break
    i += 1
else:
    print("it is a prime number")


