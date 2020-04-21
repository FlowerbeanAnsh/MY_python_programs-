x=eval(input())
y=[]
from itertools import permutations
a=permutations(map(str,x))
for i in a:
    number=''.join(i)
    y.append(number)
print(max(y))
