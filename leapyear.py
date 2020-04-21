a=int(input("enter a year:"))
result="leap year" if a%400==0 else "leap year" if a%4==0 and a%100!=0  else "not leap year"
print(result)
