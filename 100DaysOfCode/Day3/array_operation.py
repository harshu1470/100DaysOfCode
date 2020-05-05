#array opration's


from array import *
array1 = [1,2,4,5,6,7]
a1= array('i',array1)
print(a1[3])
a1.insert(1,20)
print(a1.index(20))
a2 = array('i',[2,4,22,1,2,3])
a1[4]= 80
for c in a1:
    print(c,'\n')
a3=a1 + a2
for i in a3:
    print(i)
