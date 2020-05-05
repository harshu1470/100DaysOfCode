#it takes input x, y, z and n then it will make a list of 3 dimensional co-ordinates which is less than i+j+k
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
l = [ [i,j,k] for i in range(x+1)  for j in range(y+1) for k in range(z+1) if n != (i+j+k) ]
print(l) 
