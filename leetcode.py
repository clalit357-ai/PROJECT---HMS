target = int(input("enter a number"))
l = []
x1 = int(input("number for the list"))
l.append(x1)
x2 = int(input("number for the list"))
l.append(x2)
x3 = int(input("number for the list"))
l.append(x3)
x4 = int(input("number for the list"))
l.append(x4)
for i in len(l):
    for x in (0,i+1):
        if l[i]==l[x]:
            print(i,x)
        else:
            print("sum is out of the scope of the probable sum by the entered values of the list")
