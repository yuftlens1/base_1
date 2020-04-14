a = 'aa'
b = 'bb'
c = 'cc'
d = [a,b,c]
print(d)
print(d[0])
print(d.index('aa'))   #index函数可以返回指定数据的下标；
print(d.count('aa'))   #count函数可以统计指定数据在list里出现的次数。
print(len(d))          #len函数可以统计list里有多少数据(以,为分割统计)。
print('aa' in d)       #判断 aa 是否在list d里，在的话为真
print('aa' not in d)   #判断 aa 是否在list d里，不在的话为真
'''
##一个注册小程序。
name = input('请输入您注册的用户名：')
if name not in d:
    print(f'{name} 可以注册')
else:
    print(f'{name} 已经存在，请更换。')
'''
d.append([11,22])   ##给list里追加数据,append是追加的意思。extend是延申；扩大的意思。 insert可以指定下标插入到list。
print(d)
print(d.index([11,22]))
#append是list结尾追加数据。
d.extend('ee')     #extend是把一串str分开挨个追加进list里，一个字符一个下标； append是一串全部追加进list，一个下标。！！
print(d)
d.extend([22.33])
print(d)
print(d.index(22.33))
d.insert(1,'qwe')   #下标1 插入qwe，原来的下标1及其后面的下标统统往后移。
print(d)

#del d       ##del函数直接删除整个list，也可以删除指定下标的数据。
del d[0]
print(d)

pop_name = d.pop(1)  #pop也可以指定下标删除数据，不指定下标默认删除最后一个数据并返回(pop函数会返回删除的数据)！！
print(d)
print(pop_name)

d.remove('e')        #从左往右删除遇到的第一个。
print(d)

d.clear()            #清空列表数据，列表还在。del是直接全部删除。
print(d)

#修改list指定下标的数据。
list1 = ['11','22','33']
list1[0] = 'aa'
print(list1)

#list逆序
list1.reverse()      #逆序，把数据反过来显示。  #reverse是逆向；反转；相反的意思。
print(list1)

#sort排序，升序或者降序。
list2 = ['1','3','2','4','6','5']   ##sort默认升序
list3 = [1,3,2,4,6,5]   ##sort默认升序
list2.sort(reverse=True)            #reverse是逆向；反转；相反的意思。
list3.sort(reverse=False)
print(list2)
print(list3)             ##可见，int和str的数字都可以sort排序，但是int和str不能混着来。

##list的复制 copy函数。
list4 = list3.copy()
print(list4)