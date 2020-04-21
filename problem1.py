lst=[4,5,6,89,45]
lst.sort()
lst2=[]
for i in range(len(lst)):
    lst2.append(str(lst[i]))   
print("".join(lst2))
