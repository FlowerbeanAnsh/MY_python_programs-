def info_show(**dt):
    dt.lower()
    dt.pop
    re='''
    Name:{}
    Rolln:{}
    Section:{}
    Address:{}
    '''.format(dt.get('name'),dt.get('rolln'),dt.get('section'),dt.get('address'))
    return re
k=info_show(name='Ravi',address='gla university',rolln=20,cpi=9.0)
print(k)
