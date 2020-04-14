#定义两个函数，第一个函数有返回值，第二个函数把第一个函数的返回值作为参数传入(第二个函数要有形参)
def test1():
    return 50
test1()         ##！！！直接调用该函数是不会输出的，因为其内部是return返回值。 所以我们可以拿变量接收一下！！！！！！！！
result = test1()

# return的参数值可以被其他函数调用
# print只能打印函数的结果，这些结果只能看，不能被其他函数调用
# print(test1())

def test2(num):
    a = num
    print(num)

test2(result)    #test1函数的return值赋在了result变量里。test2函数有形参
test2(test1())   #直接在test2参数传入test1函数也可以啊。


def user(username):
    """内部代码块"""
    print("Hello World," + username) #在定义函数的时候传入变量username，在调用该函数的时候就可以通过传值来让函数实现相应的功能
    print("Hello World,"f'{username}') #在定义函数的时候传入变量username，在调用该函数的时候就可以通过传值来让函数实现相应的功能
user("尼古拉斯赵四")
#从名字就可以看出，实参是一个实实在在存在的参数，是实际占用内存地址的，而形参只是意义上的一种参数，
# 在定义的时候是不占内存地址的，如在上面例子中，username就是一个形参，尼古拉斯赵四是我在调用函数时传入的一个实参，


