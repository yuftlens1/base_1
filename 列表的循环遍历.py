#依次打印列表里的数据。
list1 = ['aa','bb','cc','dd']
#print(len(list1))
i = 0
while i < len(list1):      ##len是统计函数，在这可以把list里有多少数据统计出来。
    print(list1[i])
    i += 1

for i in list1:            #for是这样写的
    print(i)

#列表嵌套，大列表里包含了许多小列表，又叫子列表。
#三年级有三个班(大列表)：1班(子列表)，2班(子列表)，3班(子列表).
list2 = [['aa','bb','cc'],['dd','ee','ff'],['gg','hh','ii']]
print(list2[0][2])    ##打印下标为0的子列表里的2下标'cc'
list2.append(['jj','kk','ll'])
print(list2)
print(list2[3][1])
print(list2[2].index('hh'))

import random
techer = ['aa','bb','cc','dd','ee','ff','gg','hh']
offices = [[],[],[]]
#num = random.randint(0,2)          ##如果放在循环外面的话，循环里num的值就是一个死数据了。
for ii in techer:
    num = random.randint(0, 2)
    offices[num].append(ii)
print(offices)
i1 = 1
for office in offices:       #这一步已经把offices里的子列表分开了，并且把子列表附在了office上。看上面的依次打印帮助理解。
    print(f'办公室{i1}的人数是{len(office)}，分别是{office}')
    i1 += 1