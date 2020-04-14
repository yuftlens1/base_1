'''
和shell里 read -p 用户输入变量一样
read -p "输入fpm运行用户(当前系统必须有该用户,root不行。[ctrl+c退出])：" user
read -p "输入fpm运行组(当前系统必须有该组,root不行。[ctrl+c退出])：" gp
'''
#password=input('请输入密码:')         ##input默认输入的都是str类型数据。
password=int(input('请输入密码:'))    ##修改输入类型为int整数。这时候在执行过程中只能输入整数，输入其他字符都报错。

#print('你输入的密码是:%s'%(password))
print(f'你输入的密码是:{password}')
print(type(password))            ##input默认输入的都是str类型数据。

