a = ['hello', 'welcome', 'to', 'python', 'and', 'java']
b = []
c = []
#d = []
def find_len(a):
    for i in a:
        b.append((i,len(i)))
        c = b.sort()
        #d = c.reverse()
    print(b)
find_len(a)

