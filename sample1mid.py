s=input("enter the string :")
m=input("input substring:")
count=0
for i in range(len(s)):
    if s[i:i+len(m)]==m:
        count+=1
print(count)

