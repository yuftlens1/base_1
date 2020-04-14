#需求：一个函数有两个返回值
def retrue_num():
    return 1
    return 2
print(retrue_num())   #只返回了1,应该return是返回并退出当前函数的意思。

def retrue_num1():
    return 1,2        #(1, 2)   返回了元组。
result1 = retrue_num1()
print(retrue_num1())

#return后面可以连接 tuple，dict，list 等来返回多个值。set也可以。

def retrue_num2():
    #return (1,2)        #(1, 2)   返回了元组数据。
    #return {1,2}        #{1, 2}   返回了集合数据。
    #return [1,2]        #[1, 2]   返回了list数据。
    return {'name':'yuft','age':'24'}    #{'name': 'yuft', 'age': '24'}   返回了dict数据。
result1 = retrue_num2()
print(retrue_num2())







