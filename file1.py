

fp = open(r'D:/test1.txt','r')

#print(fp.read())
#fp.write("\n python is a programming language")

#for i in fp :
lines = [i for i in fp.readlines()]
print(lines)
print(type(lines))
lines.pop()

print(lines)



