import math
'''y = int(input("enter a numb"))
x = 1       #THE TIME COMPLEXITY OF THIS CODE IS QUITE HIGH IF NOT VERY HIGH
while x<=math.sqrt(y**2):
    if y % x ==0:
        print(x)
    x = x+1'''
#OPTIMAL SOLUTION
L= []
y = int(input("enter a num"))
for i in range(1,int(math.sqrt(y))+1):
    if y%i == 0:
        L.append(i)
        if y//i!=i:
            L.append(i)    '''notice this is kept inside the first for, bcz the condition of remainder =0 
                           should be ment'''
print(L)