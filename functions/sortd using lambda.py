a = ['hello', 'python', 'welcome', 'to', 'java']
b = sorted(a, key = lambda x : len(x))
#c = sorted(a, key = lambda x : len(x), reverse = true)
print(b)
#print(c)
d = [('sachin', 500, 50), ('virat', 250, 35), ('sourav', 350, 40), ('youvi', 400, 38), ('sehwag', 350, 36)]
z = sorted(b, key = lambda x: x[2], reverse = true)
print(z)