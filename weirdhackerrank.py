n=int(input("please enter a no:"))
if n%2==0:
    if n>=2 and n<=5:
        print("Not Weird")
    if n>=6 and n<=20:
        print("Weird")
    if n>=20:
        print("Not Weird")
elif n%2!=0:
    print("Weird")

