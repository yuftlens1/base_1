'''
e = ' I\'m tom '      ##三个引号会语法错误，把本该就是字符串的 ' ，直接转义成字符串。
print(e)
str1 = 'abcdefg'
#正数测试
print(str1[2])        #下标
print(str1[0:4:1])    #切片；[开始位置下标:结束位置下标:步长]   #取开始下标位置到结束位置前一位的数据。
print(str1[0:4:2])    #步长就是选举间隔，默认为1.
print(str1[0:4])
print(str1[:4])       #如果切片不指定开始位置下标，默认从0开始。
print(str1[2:])       #如果切片不指定结束位置下标，默认取到最后。
print(str1[:])        #开始和结尾都不指定则全取。
#负数测试
print(str1[::-1])     #步长-1的话则倒取全部。
print(str1[::-2])     #步长倒取，两步取一个值。
print(str1[-4:-1])    #开始结束为-则从数据后往前取（反过来取），-1就是f，-4就是c的后一位d。
#终极测试##onenote里有这块笔记。
print(str1[-4:-1:1])
print(str1[-4:-1:-1])   ##-取值遇到-步数不输出！！！
print(str1[-1:-4:-1])
'''
mystr = 'hello word and itcast and itheima and Python!'
print(mystr.find('and'))       ##空格也算一个字符
print(mystr.find('ands'))      #如果字串不存在，则返回-1.

print(mystr.index('and'))      #index检查子串是否存在不存在直接报错。
#print(mystr.index('ands'))     #index如果不存在直接报错。

print(mystr.count('and'))      #count统计次数

print(mystr.replace('and','ands')) # replace替换，把and替换成ands。
print(mystr.replace('and','ands',1)) # replace替换，把and替换成ands,只替换一次。
print(mystr)                       # 可以发现，replace并没有对原有str做修改。
#以上说明原有str是不可变数据类型，后期会遇到列表和字典可以直接修改的，是可变数据类型。

list1 = mystr.split('and')
list2 = mystr.split('and',2)      #以2个and作为点分割为list。
list3 = mystr.split(' ')          #以空格作为点分割为list。
print(list1)                      #split分割，以and分割为列表类型数据。
print(type(list1))
print(list2)
print(list3)

list4 = ['aa','bb','cc']
str1 = '...'.join(list4)          #join将list转换为str，并且以...为分割。
print(str1)
print(type(str1))
str2 = '..'.join(list3)
print(str2)
print(str2.capitalize())          #把str第一个字符转为大写
print(str2.title())               #把str里每段子串开头转为大写。

print(str2.startswith('hello',0,6))  #判断str2是否以'hello开始'，下标0开始6结束。
print(str2.endswith('python!'))      #判断ste2是否以'python！结尾'，区分大小写。