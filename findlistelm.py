lst=list(map(int,input().split()))
lst2=[]
for i in range(lst[0],lst[-1]+1):
    if i not in lst:
        lst2.append(i)
print(lst2)
    
