def counter():
    a = 20
    def val():
        nonlocal a
        a = a + 20
        print(a)
    return val
x = counter()
x()
x()
x()
