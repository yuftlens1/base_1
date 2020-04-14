#交换变量值
a = 10
b = 20

#开始操作
c = 0       #先定义一个工具变量c
c = a       #把a的值覆盖进c
print(c)

a = b       #把b的值覆盖进a
b = c       #再把c的值覆盖进b里就ok了。
print(a,b)

#上面是方法一，下面是方法二
a1 = 1
b1 = 2
a1,b1 = b1,a1      #这个方法简单快速.
print(a1)
print(b1)




