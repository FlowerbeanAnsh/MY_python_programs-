a=input("enter somethig:")
b=ord(a)
if b>=65 and b<=90:
    print("uppercase alphabet")
elif b>=97 and b<=122:
    print("lowecase alphabet")
elif b>=48 and b<=57:
    print("digits")
else:
    print("special character")
    
