#推导式又叫生成式

#需求：创建一个list里面数据是 int 0-10
list1 = []
i = 0
while i <= 10:
    list1.append(i)      ##好好看，好好学。
    i += 1
print(list1)

list3 = []
for i in range(3):                   #这个好理解
    for j in '甲乙丙':
        #list3.append(f'{j}-{i}')     #   f可以整合进两个参数，以str追加进list里
        list3.append((i,j))           #   可以整合进两个参数，以子元组追加进list里
print(list3)

print([(i4,i5) for i4 in range(1,3) for i5 in range(3)])   #根据输出的数据结果判断哪个是大循环体，哪个是嵌套循环
#一般就是重复的元素，比如111122223333这样的是大循环体，然后123123123这样的元素是嵌套循环体。
print([[i5,i4] for i4 in '1234' for i5 in range(3)])       #根据输出的数据结果判断哪个是大循环体，哪个是嵌套循环

a = 8
b = 9
list4 = [1,2,3]
print(list4)
list4.append(5)
list4.append([6,7])
list4.append(f'{a}-{b}')            #   f可以整合进两个参数，以str追加进list里
print(list4)

print([i2 for i2 in range(4)])      #直接打印推导


#以下是推导偶数的两种方法。第二种代码量就少的多。
list5 = []
list6 = []
i3 = 0
while i3 <= 10:
#    list5.append(i3)
    i3 += 1
    if  i3 % 2 == 0:
        list5.append(i3)           #偶数追加进list5
    else:
        list6.append(i3)           #奇数数追加进list6
print(list5)
print(list6)

# list2 = [i1 for i1 in range(11)]
list2 = [i1 for i1 in range(11) if i1 % 2 == 0 ]     #推导偶数
print(list2)









