lst1=list(input("enter the list elements of first list:"))
lst2=list(input("enter the list elements of second list:"))
lst2=[i for i in lst1 if i in lst2]
print(lst2)

