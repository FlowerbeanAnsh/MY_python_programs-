def my_fun():
    def fun_1():
        global d
        d=1
    def fun_2():
        nonlocal d
        d=2
    def fun_3():
        d=3
    d=0 #nonlocal variable
    fun_1()
    print(d)
    fun_2()
    print(d)
    fun_3()
    print(d)
d=100 #gloabal variable
my_fun()
print(d)
    
    
