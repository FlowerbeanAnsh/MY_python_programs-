a=input("enter somethig:")
if a.isnumeric():
    print("digits")
elif a.isalpha():
     if a.upper():
        print("uppercase")
     else:
          print("lowecase alphabet")
else:
     print("special character")
    

