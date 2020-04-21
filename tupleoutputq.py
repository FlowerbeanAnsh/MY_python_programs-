lst=[(3,5,6),(5,6,5),(10,0,6)]
newlst=[]
for i in range(0,len(lst)):
    a=list(lst[i])
    a[2]=100
    newlst.append(tuple(a))
    
print(newlst)
