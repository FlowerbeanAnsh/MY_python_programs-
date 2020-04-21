x=float(input("enter the first no:"))
y=float(input("enter the second no:"))
if x>y:
    maxm=x
else:
    maxm=y
while True:
    if maxm%x==0 and maxm%y==0:
        print("\n LCM of x and y is",maxm)
        break
    maxm+=1

