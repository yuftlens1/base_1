t1 = (10,20,30)   #tuple
t2 = (10,)        #tuple
t3 = (10)
t4 = ('10')
t5 = ('10',)      #tuple
print(type(t1))
print(type(t2))
print(type(t3))
print(type(t4))
print(type(t5))

#tuple数据只支持查找，不支持修改。(用下标查找)
tuple1 = (11,22,33,44,55,[66,77])
print(tuple1[1])
print(tuple1.index(33))
print(tuple1.count(11))
print(len(tuple1))
tuple1[5][0] = 88     ##元组数据是不能修改，但是元组里的子列表里的数据可以修改。！！！
print(tuple1)