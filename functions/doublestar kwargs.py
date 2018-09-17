def var_args(a, b, c=10, *venkat, **ramana):
    print('a is:', a)
    print('b is:', b)
    print('c is:', c)
    print(venkat)
    print(ramana)
var_args(100, 200)
var_args(10, 20, 30, 40, 50, 60, 70, 80, name = 'python', year = 1992)

