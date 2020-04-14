dict1 = dict()         #方法一创建空字典
print(type(dict1))

dict2 = {}             #方法二创建空字典
print(type(dict2))
#dict是可变类型

dict3 = {'name':'tom','age':19,'gender':'男'}
print(dict3['name'])        #打印name这个key的值
dict3['name'] = 'hab'       #修改name这个key的值
print(dict3)
dict3['id'] = 13            #如果id这个k存在则修改其值，不存在则新加该k和其值。
print(dict3)
#以下是字典删除操作：  del   clear()函数
del  dict3['name']          #del删除指定键值对。
print(dict3)

# del dict3                   #如不指定则删除整体dict，包括dict对应的变量。
# print(dict3)

dict3.clear()               #clear() 清空dict里的数据，但dict还会保留。
print(dict3)

#查找    get()函数  keys()函数  valuse()函数  items()函数
dict4 = {'name':'tom','age':19,'gender':'男'}
print(dict4['name'])        #直接打印key
tmp1 = dict4.get('name')
tmp2 = dict4.get('names','没有')  #get()函数可以有两个参数，第一个是要获取的key，第二个是如果第一个参数没获取到则返回第二个参数。
print(tmp1)                       #如果get()第一个参数没有找到key，也没有设置第二个参数则返回None
print(tmp2)

tmp3 = dict4.keys()              #keys()函数可以查出dict里全部的key,返回可迭代对象(可以用for遍历的对象)
print(tmp3)
for i in tmp3:
    print(i)

tmp4 = dict4.values()            #像key()一样，values可以查出dict里全部的值。返回的也是可迭代对象。
print(tmp4)
for i2 in tmp4:
    print(i2)

tmp5 = dict4.items()         #items()函数查找dict里所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是key，数据2是vlaues。
print(tmp5)
for i3,i4 in tmp5:
    print(f'{i3} = {i4}')
print(type(tmp5))





