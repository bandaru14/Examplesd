def func_scope():
    global x
    global a
    a = 10
    x = 20
    y = 20
    z = 'hello'
    print(x)
    print(y)
    print(z)
    b = a * x
    print(b)
func_scope()
print(a)
print(x)