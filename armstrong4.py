n=int(input("enter a no. which you want to check is armstrong or not:"))
m=str(n)
o=len(m)
sum=0
temp=n
for i in range(1,o+1):
    rem=n%10
    sum=sum+(rem*rem*rem)
    n=n//10
if sum==temp:
    print("armstrong no")
else:
    print("non armstrong no")

