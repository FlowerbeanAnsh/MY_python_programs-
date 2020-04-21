lst1=list(input("enter the list elements of first list:"))
lst2=list(input("enter the list elements of second list:"))
lst3=[]
for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)
        
