from array import *
A1 = array('i',[])
y= int(input('enter len of A1'))
for i in range(y):
    x = int(input('Enter a value to append in A1'))
    A1.append(x)
print(A1)

temp = 0
for i in range(len(A1)):
    if temp>=A1[i]:
        continue
    else:
        temp = A1[i]
print(temp)