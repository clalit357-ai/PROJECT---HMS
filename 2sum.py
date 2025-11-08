#array of statements (n) ints and a target value check if there exists a pair whose sum = to the target
 #(1,2,3,4) is an array say target = x
target = int(input("enter a number"))

L =["1","2","3","4"]
for i in range (L):
    for x in range (0,i):
        i+=1
        x = L[i]
    if (x == target):
        print("succuess")                
                
                
                
                
                
                
                
                
