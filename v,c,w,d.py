a=input("enter something:")
v=0
w=0
c=0
d=0
for i in a:
    if i=='a' or i=='i' or i=='e' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
       v+=1
    elif i.isdigit():
         d+=1
    elif i.isalpha():
         c+=1
    elif i in [' ','/','\n']:
         w+=1
print("the no of vowels is",v)
print("the no of consonats is",c)
print("the no of whitespace is",w)
print("the no of digits is:",d)
