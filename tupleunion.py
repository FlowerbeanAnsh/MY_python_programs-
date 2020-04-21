t1=list(map(int,input().split()))
t2=list(map(int,input().split()))
t3=t1+t2
t4=[]
for i in t3:
    if i not in t4:
        t4.append(i)
print(tuple(t4))
