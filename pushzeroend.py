lst=list(map(int,input().split()))
lst2=[]
lst.sort()
y=lst.count(0)
for i in range(len(lst)):
    if lst[i]!=0:
        lst2.append(lst[i])
for i in range(0,y):
    lst2.append(0)
print(lst2)

