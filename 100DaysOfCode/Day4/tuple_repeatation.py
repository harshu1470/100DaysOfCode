#This program is to find out how much time's a tuple repeat in a list

def count(l1): 
    dic_count = {} 
    for i in l1: 
        dic_count[i] = dic_count.get(i, 0) +1
    print(dic_count, "\n")
    
    
    for key, value in dic_count.items():
        print( "this" + " " + str(key) + " " +"tuple repeat" + " "+ str(value) + " " + "Times")
    
l1 = [('a' ,'b') , ('c','d') , ('a','b') , ('c','f'),('c','d')]  
count(l1)
  
