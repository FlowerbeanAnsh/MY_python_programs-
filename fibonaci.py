n=int(input("how many terms:"))
t1=0
t2=1
print(t1,t2,end=',')
for i in range(2,n+1):
        nth=t1+t2
        print(nth,end=',')
        t1=t2
        t2=nth
        

