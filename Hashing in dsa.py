n = [1,2,3,4,5,2,3,4,10]
m = [10,0,12,1,3,1,3,3,2]
hash = [0]*11    # a list with 11 elemnts all of which are 0's
for i in n:
    hash[i]+=1
for i in m:
    if i<0 or i>10:
        print(0)
    else:
        print(hash[i], end = "  ")


