h=10
r=5
f=15
t=float(input("enter the time:"))
voltnk=3.14*r*r*h
volwat=f*t
if voltnk==volwat:
    print("tank full")
elif volwat>voltnk:
    print("overflow")
    x=volwat-voltnk
    print(x)
else:
    print("underflow")
    print(voltnk-volwat)
    
