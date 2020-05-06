#left list rotaion by user input value using function

def rotation(x,d):
    for j in range(d):
        a=x[0]
        for i in range(len(x)-1):
            x[i] =x[i+1]
        x[len(x)-1] = a
    return x

x=[1,2,3,4,5,6,7,8]
d=int(input("enter number"))
rotation(x,d)
