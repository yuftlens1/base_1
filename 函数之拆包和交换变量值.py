#无论 包裹位置传递还是包裹关键字传递，都是一个组包的过程。
#零散的数据组合在一起就叫组包。 拆包和组包相反。

#拆包：元组
def test1():
    return 100,200
print(test1())    #(100, 200)   这里输出的是元组数据，所以下面的是拆元组数据。
num1,num2 = test1()    #test1函数返回两个值，我们用两个变量去等于test1函数，系统就把test1返回的两个值按位置赋到了两个变量上。
print(num1)
print(num2)

#拆包：字典
dict1 = {'name':'tom','age':20}
print(dict1['name'])   #dict靠k找v。
a,b = dict1            #拆包只能取出k，取出k后，就像上面，靠k找v。
print(a)
print(b)
print(dict1[a])        #靠k找v。
print(dict1[b])        #靠k找v。










