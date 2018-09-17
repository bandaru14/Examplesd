def cancatination_string(a, b, d=10):
    print(d)
    if type(a) == str and type(b) == str:
        c = a + b + d
        print(c)
    else:
        print('please enter the same type')
cancatination_string('hai', 'bandaru', 'tryit')
cancatination_string('hai', 'hello', 'world')
cancatination_string(67, 89, 90)