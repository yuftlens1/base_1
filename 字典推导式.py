#dict推导式
list1 = ['name','age','gender']
list2 = ['tom','19','man']
#以上两个列表合并为字典
print(len(list2)) #len统计个数，len(list2)也就是len(3)
print(range(len(list2)))  #range(len(3)) 也就是rang(0,3) #也就是0，1，2 range不算本身最后一位
#然后0，1，2也就是两个list1和2的下标。以读取list下标数据写进dict里。
dict1 = {list1[i]:list2[i] for i in range(len(list2))}   #该实验里的俩list的下标必须一致！！

print(dict1)

#快速创建一个dict，k是1-5，v是k的平方
dict2 = {i2:i2 ** 2 for i2 in range(1,6)}
print(dict2)

#提取dict中的目标数据
counts = {'mac':209,'hp':198,'dell':300,'hw':301}
print(counts.items())    #items()函数查找dict里所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是key，数据2是vlaues。
dict3 = {k:v for k,v in counts.items() if v >= 300}   ##值大于300的
print(dict3)


list3 = []
for i3 in counts.values():      ##把字典key追加进list里
    if i3 >= 200:
        list3.append(i3)
print(list3)

list4 = [i4 for i4 in counts.values() if i4 >= 200]    ##把字典key追加进list里,推导式
print(list4)

##set推导式   ##注意 set有去重功能
list5 = [1,2,2,3]
set1 = {i5 ** 2 for i5 in list5}
print(set1)




