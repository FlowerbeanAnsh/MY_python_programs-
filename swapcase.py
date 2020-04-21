x=input()
s=[]
y=[]
for i in x:
    s.append(i)
for i in range(0,len(s)):
    if (ord(s[i])>64 and ord(s[i])<91):
        y.append(chr(ord(s[i])+32))
    elif (ord(s[i])>96 and ord(s[i])<123):
        y.append(chr(ord(s[i])-32))
print("".join(y))

              
