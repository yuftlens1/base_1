#集合去重，集合里的数据是没有重复的。
s1 = {10,20,30,40,50}          #set里的数据没有下标
s2 = {10,20,30,40,50,10,20}    #set里的数据没有下标
print(s1)
print(s2)
print(type(s1))
#set的创建只能用set(),因为set{}是创建空dict的。
s3 = set()                     #创建空set
print(type(s3))
s4 = set('sadsafsdadsa')     #set去重
s5 = set('qwerasdf')
print(s4)
print(s5)

#增加数据   add()   update() 函数
s6 = {10,20,30}
s6.add(100)
s6.add(100)             #因为set去重，所以只会追加进一个100
print(s6)
# s6.add([1,2,3])       #报错，可以得知add只能最佳单一数据，不能追加这种数据序列。update增加的数据是序列的。！
# print(s6)
s6.update([40,50,60])   #可以看到追加进来的序列数据没有成子列表，而是融入到set里了。
print(s6)
print(type(s6))
# s6.update(100)       #报错，TypeError: 'int' object is not iterable  iterable是可迭代对象的意思。可以看出update只能追加序列数据。
# print(s6)

#删除set数据,remove()    discard()     pop()                    discard的意思是抛弃；丢弃    pop是弹出的意思。

s6.remove(60)    #remove删除指定的单一数据
print(s6)
#s6.remove(60)    #如果删除的数据不在set中remov函数会报错
#print(s6)
# s6.discard(50,40)
s6.discard(50)   #discard也是删除单一数据的，但是如果删除的数据不在set中是不会报错的，remove就会报错。
print(s6)
s6.discard(50)
print(s6)

a = s6.pop()     #pop是随机删除某个单一数据，然后把删除的数据返回到pop函数中。
print(a)
print(s6)

# set之查找操作  用in 和not in 俩判断操作 灰常滴简单
print(10 in s6)
print(10 not in s6)







