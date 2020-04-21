a=int(input("please ansh enter a no which you want to check:"))
if a<2:
    print("not prime no")
for i in range(2,a):
     if a%i==0:
        print("not a prime no")
        break
else:
     print("a prime no")
