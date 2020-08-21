def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x % y)
a=int(input("enter first no:"))
b=int(input("enter second no:"))
out=gcd(a,b)
print(out)
