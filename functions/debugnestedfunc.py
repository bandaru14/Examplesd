import pdb
pdb.set_trace()
def outer(x):
    print('i am in outer',x)
    def inner(y):
        c = x + y
        print(c)
    return inner
out = outer(5)
print(out(6))