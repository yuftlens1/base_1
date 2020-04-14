#格式化输出变量
name = 'tom'
age = 12
weight = 60.5
stu_id = 1
stu_id2 = 1999
#1.我今年的年龄是x岁。
print("我今年的年龄是%d岁。" %age)
#2.我的名字是x。
print('我的名字是%s。' %name)
#3.我的体重是x公斤。
print('我的体重是%f公斤。' %weight)
print('我的体重是%.2f公斤。' %weight)        #默认保留小数点后6位，这里改成2位。
print(f'f格式化输出：我的体重是{weight}公斤。')
#4.我的学号是x。
print('我的学号是%d。' %stu_id)
print('我的学号是%3d。' %stu_id)           #改成占3位显示。
print('我的学号是%03d。' %stu_id)          #改成占3位显示，用0填充占位。
print('我的学号是%03d。' %stu_id2)         #如果超出规定则原样显示。
#5.我的名字是x，今年x岁了。
print('我的名字是%s，今年%d岁了。' %(name,age))  #格式化输出两个变量。
print(f'f格式化输出:我的名字是{name}，今年{age}岁了。')
#5.1.我的名字是x，明年x+1岁了。
print('我的名字是%s，明年%d岁了。' %(name,age+1))
#6.我的名字是x，今年x岁了，体重x公斤，学号是x。
print("我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%03d。" %(name,age,weight,stu_id))
print("我的名字是%s，今年%s岁了，体重%s公斤，学号是%s。" %(name,age,weight,stu_id))
print(f"我的名字是{name}，今年{age}岁了，体重{weight}公斤，学号是{stu_id}。")