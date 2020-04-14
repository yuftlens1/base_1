# def h():       #def 定义函数 , ()里面可以写参数，需要的时候就加上参数。
#     print('hello')    #函数内容代码
#
# h()    #调用函数 , ()里面可以写参数，需要的时候就加上参数。
#
#函数的执行流程：当调用函数的时候，解释器会回到定义函数的地方执行函数下缩进的代码。当这些代码执行完，就回到调用函数的地方继续向下执行。
# def sum(a,b):
#     result = a + b
#     print(result)
# sum(1,2)
#
# def sum1(a,b):     ##不同函数使用一样的参数是可以的。
#     result = a + b
#     print(result)
# sum1(2,2)

number1 = int(input('请输入整数:'))
number2 = int(input('请输入整数:'))
def sum3(a,b):     ##不同函数使用一样的参数是可以的。
#    '''输入两个数字后求和'''   ##低级版解释该函数，在help(sum3)可以输出该解释内容
    '''                       
    输入两个数字后求和
:param a:输入第一个数字参数
:param b:输入第二个数字参数
:return:返回求和值
'''                           #以上几行绿色字段为高级版解释函数，在help(sum3)可以输出该解释内容。param是参数的意思。
    result = a + b
    # print(result)
    print('231')       #必须放到return 之前，不然该print不执行.
    return (result)   #return返回结果给调用函数的地方  #return的意思是返回。#他也是结束当前函数的一个功能作用。
    # print('123')
he = sum3(number1,number2)
print(f'和是{he}')


def buy():
    """

    :return:'烟'
    """
    return '烟'
test = buy()
print(test)

#help() #help函数就是查看其他函数的说明文档的。
help(sum3)
help(buy)






