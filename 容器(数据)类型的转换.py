#有时候已有的数据类型和我们想用的数据类型不一致,也就是数据类型转换.
list1 = [1,2,3,4,5]
set1 = {10,20,30,40,50}
tuple1 = (100,200,300,400)
print(type(list1),type(set1),type(tuple1))

#把list1和set1转换为元组数据类型。
tuple2 = tuple(list1),tuple(set1)
print(tuple2)               # 结果      ((1, 2, 3, 4, 5), (40, 10, 50, 20, 30))
print(type(tuple2))
tuple3 = tuple(list1)
tuple4 = tuple(set1)
print(tuple3,tuple4)        # 结果      (1, 2, 3, 4, 5) (40, 10, 50, 20, 30)
print(tuple3 + tuple4)      # 结果      (1, 2, 3, 4, 5, 40, 10, 50, 20, 30)

#把set1和tuple1转换为list数据。
list2 = list(tuple1),list(set1)   #这样的变量输出基本都是元组类型，里面套着子列表或者子其他数据类型。
print(list2)               #结果 ([100, 200, 300, 400], [40, 10, 50, 20, 30])  注意看这是元组类型数据！！！
print(type(list2))
print(list(list2))         #把它转换成list，嘿嘿。 结果 [[100, 200, 300, 400], [40, 10, 50, 20, 30]]
print(list(tuple1) + list(set1))  #结果 [100, 200, 300, 400, 40, 10, 50, 20, 30] 直接打印转换结果

#把list1和tuple1转换为set集合数据类型
print(set(list1),set(tuple1))    #结果 {1, 2, 3, 4, 5} {200, 100, 400, 300}
#print((set(list1)) + (set(tuple1)))    #结果 TypeError: unsupported operand type(s) for +: 'set' and 'set' + 不支持set集合数据。








