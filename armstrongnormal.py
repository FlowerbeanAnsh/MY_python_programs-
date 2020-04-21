n=int(input("enter a no. which you want to check is armstrong or not:"))
sum=0
temp=n
while n!=0:
    rem=n%10
    sum=sum+(rem*rem*rem)
    n=n//10
if sum==temp:
    print("armstrong no")
else:
    print("non armstrong no")
