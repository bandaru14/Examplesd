def var_args(a, b, c=100,*venkat):
    print('a is:', a)
    print('b is:', b)
    print('c is:', c)
    print(venkat)
var_args(100, 200)
var_args(10, 20, 30, 40, 50, 60, 70, 80,)