lst=list(map(str,input().split()))
if len(lst)==0:
        print('empty')
        
        
else:
    for i in lst:
        if i.isnumeric():
            print('Yes')
            break
    else:
        print('no')
print(lst)
