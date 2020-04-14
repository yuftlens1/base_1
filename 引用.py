#可变和不可变  int是不可变。
a = 1
b = 1
print(id(a))  #140704677552976
print(id(b))  #140704677552976

a1 = 2
b1 = a1
print(b1)
print(id(b1))
print(a1)
print(id(b1))

#list是可变
aa = [10,20]
bb = aa
print(bb)
print(id(aa))
print(id(bb))
aa.append(30)
print(aa)
print(bb)      #list是可变的数据类型，aa里追加了数据，bb里也加上了。
print(id(aa))
print(id(bb))

#引用当作实参。
def test(a2):
    print(a2)
    print(id(a2))    ##140704782217136
    a2 += a2
    print(a2)
    print(id(a2))    ##140704782217136

b2 = 100
test(b2)
print(id(b2))        ##140704782217136  # a2 += a2之前，实参b2的id和形参a2的id一样。之后就不一样了。

c = [11,22]
print(id(c),'c的id')
test(c)              #list在a2 += a2之前 , id都一样。



