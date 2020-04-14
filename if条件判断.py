'''
if False:
    print('1')  ##可以看到缩进和未缩进就是两块代码。
print('2')      #没有缩进的代码不属于 if下的代码块，即和条件的成立与否无关。

age=int(input('请输入你的年龄:'))   ##input默认为str数据，这转为int数据。
if age >= 18:                      ##if条件判断，条件成立则只执行if下缩进的代码。
    print(f'{age}岁,可以上网')
else:                              ##else下缩进的代码是只执行条件不成立的代码。
    print('滚')
print('系统关闭')

age = int(input('how old are you?:'))
if (age < 18) and (age >= 1):
    print('小学生')
#elif (age >= 18) and (age < 60):
elif 18 <= age < 60:     #简化and条件判断语句。
    if 25 <= age <=35:
        print('精壮男子')      ###if嵌套,但是会把被嵌套的条件结果也一起打出来。

    print('成年人')
elif age < 1:
    print('什么鬼？')
else:
    print('老东西')

#坐公交
qian = int(input('现在有多少元钱：'))
if qian >= 2:
    print(f'{qian}元可以坐公交。')
    zuowei = int(input('车上还有几个座位：'))  # 哪个环节需要哪个变量，手动输入的变量最好放在需要的环节里，不然一开始就让输入各个环节的变量体验就很差。
    if zuowei >= 1:
        print('不用站着')
    else:
        print('得站着')
else:
    print(f'{qian}元不能坐公交。')

#猜拳游戏    下面这个实验有问题，以后回来研究吧
import random    #random 随机数模块
cpu = random.randint(0,2)
print(cpu)
wanjia = int(input('0-石头,1-剪刀,2-布.出什么？:'))
if cpu == 0 and wanjia == 1 or cpu == 1 and wanjia == 2 or cpu == 3 and wanjia == 0:
    print('电脑获胜')
elif wanjia == cpu:
    print('平局')
else:
    print('玩家获胜')

#elif ((cpu==0) or (wanjia==1)) and ((cpu==1) or (wanjia==2)) and ((cpu==2) or (wanjia==0)):
#    print('电脑获胜')
#    print(f'电脑出的是{cpu}')
'''
a = 5
b = 3
#c = a if a > b else b      ##  c = 条件成立执行的表达式 | if 条件 else | 条件不成立执行的表达式。
c = b - a if b > a else a - b
print('%d' %c)

if a > b:                  ##正常if算出来是正常的，三目算出来的全是绝对值；正整数。
    c = b -a
    print(c)
else:
    c = a - b
    print(c)