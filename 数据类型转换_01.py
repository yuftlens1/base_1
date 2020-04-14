num=1
str1='20'
print(type(num))         #默认num是int整数类型
print(type(float(num)))  #这个可以给转换成小数float类型。
print(float(num))        #转换完小数类型并print出来
print(type(str(num)))    #把默认的int转换为str
print(str(num))          #把默认的int转换为str，并print出来。

print(type(str1))
#print(type(float(str)))  #这个可以给转换成小数float类型。
print(float(str1))         #这个连转换完小数类型并显示出来

list1=[1,2,3]
print(type(list1))        #[]是list类型
print(tuple(list1))       #把默认list转换为tuple元组类型，并print出来。   ()元组；[]列表；{}set集合

str2='1'
str3='1.11'
str4='(1,2,3,4)'
str5='[1,2,3,4]'
str6='1'
print(type(eval(str5)))  #正常来说，''号内应该就成str类型了，eval把其打回原形。
print(f'hello {eval(str4)}')
print(str4)