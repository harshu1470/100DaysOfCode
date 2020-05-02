k=4
c='H'
for i in range(k):
    print((c*i).rjust(k-1) + c + (c*i).ljust(k-1))
    
for i in range(k+1):
    print((c*k).center(k*2)+ (c*k).center(k*6))

for i in range((k+1)//2):
    print((c*k*5).center(k*6))    

for i in range(k+1):
    print((c*k).center(k*2)+(c*k).center(k*6))    

for i in range(k):
    print(((c*(k-i-1)).rjust(k)+c+(c*(k-i-1)).ljust(k)).rjust(k*6))
