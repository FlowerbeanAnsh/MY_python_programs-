lst0=list(map(int,input("enter elements:").split()))
lst=[]
fact = 1
for item in lst0:
    for number in range(1,item+1):
        fact = fact * number
    lst.append(str(fact))
    fact=1
print(','.join(lst))
    
