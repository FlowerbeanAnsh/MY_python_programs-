n=int(input("enter a no:"))
temp=n
sum=0
while n!=0:
     r=n % 10
     sum=sum*10 + r
     n=n//10
if temp==sum:
    print("palindrme")
else:
    print("non palindrome")
     
