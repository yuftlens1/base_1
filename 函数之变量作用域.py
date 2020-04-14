#变量作用域就是变量生效的范围：有局部变量和全局变量
b = 200                     #全局变量，函数里可以调用。
c = 300
def test1():
    a = 100                 #这就是局部变量#函数里的变量在外面没法调用
    # return a
    print(a)
    print(b)

# print(a)   #报错 NameError: name 'a' is not defined

test1()

def test2():
    b = 199
    print(b)               #如果函数里的局部变量和全局变量重复了，该函数执行时优先调用其局部变量。
    global c               #global可以在函数里修改全局变量值
    c = 301

test2()
print(c)           #该变量的值被上面函数里已修改。

def test3():
    print(c)        #只要上面的函数里global修改过全局变量的值，下面再调用都是修改过的值。

test3()

# import sysconfig
# print(sysconfig.get_config_vars())       #查看python编译安装参数
glo_num = 1
def gol():
    global glo_num
    glo_num = 2

def test4():
    print(glo_num)

# gol()        #如果该函数里global修改了全局变量的值，但是没调用该函数的话下面其他代码函数调用的时候是不会变得。
test4()









