def outer():
    print('i am in outer')
    def inner():
        print('i am in inner')
    return inner()
a = outer()
a()
