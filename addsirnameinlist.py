a=['ansh kumar','vansh kumar','prachi kumar','neha kumar','devendra kumar','savitri kumar']
b=[i.replace('kumar','saxena') for i in a if i.endswith('kumar')]
print(b)
b.append('ashish saxena')
print(b)
