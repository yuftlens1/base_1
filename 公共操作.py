#所学的数据序列都支持公共操作。
#公共操作之 + 合并   (数据合并,支持str list tuple)
str1 = 'aa'
str2 = 'bb'
#print(str1 + str2)
list1 = [1,2,3]
list2 = [4,5,6]
#print(list1 + list2)
tuple1 = (1,2,3)
tuple2 = (4,5,6)
#print(tuple1 + tuple2)
dict1 = {'name':'tom','id':'101'}
dict2 = {'love':'python'}  #dict不支持合并运算
# print(dict1 + dict2)       #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

#公共操作之 * 复制   (数据复制,支持str list tuple)
print(str1 * 3,list1 * 3,tuple1 * 3)
print('-' * 60)

#公共操作之 in和not in   (布尔值判断,支持str list tuple dict)
print('aa' in str1,1 in list1,1 in tuple1,'name' in dict1,'tom' in dict1) #注意dict只能判断key！
print('aa' not in str1)

set1 = {10,20,30,40,50,50}

#一些公共操作函数  step的意思是 步；步骤。
# len()  del或del()  max()  min()  range(start,end,step)  enumerate()
#len 统计对象内元素的树里  #对于set的len是去重后的结果。对于dict的len是统计键值对。
print(len(str1),len(list1),len(tuple1),len(dict1),len(set1))

#del and del()
# del(str1[1])   #TypeError: 'str' object doesn't support item deletion  str是不可变数据类型
del str1         #把str1的数据及自身变量全部删除。
print(list1)
del(list1[0])
print(list1)

#max() min()
print(max(set1))
print(min(set1))
print(list1)
print(min(list1))

#range(start,end,step)  range()可以生成start到end之间的数字，步长是step，供for循环遍历/迭代使用！
print(range(len(tuple1)))
print(range(0,10,2))    ##range只供for循环使用
# import sys
# print(sys.version)

for ia in range(0,11,2):   #range不指定开始默认从0开始,range生成的序列不包含end数字。
#for ia in range('g'):   #TypeError: 'str' object cannot be interpreted as an integer,可见range只能处理整数
    print(ia)

#enumerate返回的结果是元组，元组里的第一个数据是原迭代对象的数据对应的下标，第二个数据是原迭代对象的数据
list3 = ['a','b','c','d','e','f']
print(list3)
print(list3[2])  #输出打印下标
for ib in enumerate(list3):
    print(ib)

print('试验分割')

for i1 in enumerate(list3,start=1):  #enumerate的第二个参数可以更改结果起始下标位置数据。默认下标0开始，这改成1开始。
    print(i1)











