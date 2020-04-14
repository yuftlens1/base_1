
a = 'hell' \
    'o1'
print(a[0])     ##下标；索引，这玩意存在内存里，从0开始算。
b = '''hello2'''
c = """hello
       3"""            ##三引号也是字符串类型。
d = input('输入：')
print(a)               ##注意观察a和c。单引和三引的区别。单引换行系统自动加 \ ,显示效果还是一行。
print(type(b))                       #三引换行显示也是换行了。
print(c)
print(type(c))
print(type(d))

e = ' I\'m tom '      ##三个引号会语法错误，把本该就是字符串的 ' ，直接转义成字符串。
print(e)
str1 = 'abcdefg'
print(str1[2])