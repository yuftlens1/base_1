'''
i = 0
while i < 2:       #i 不能大于 5
    print('haha')
    i = i + 1       #while条件代码块下i循环着加1.  #这句可以写成 i += 1  运算符里的复合运算符。
    #i=0+1也就是 i=1了。
    #i=1+1 ; i=2了 #接上面的
    #i=2+1 ; i=3了 #接上面的；这样循环到条件里的 <5,也就是4。
    print('dandan')  #只有和i += 1 在一个代码块里，就也会跟着条件循环。
print('STOP')

##  1到3相加结果。
a = 1
result = 0      #结果变量,从0开始。
while a <= 6:
    #a = a + 1    #先获得1到100增量数字;这个得放后面，因为a=1+1，放这现在是2，从2开始加肯定不准确。
    #print(a)
    result = result + a   #因为是循环语句也要循环着加，a循环着变大到100，
    # result=0+1=1；result现在等于1了，然后进入到下一个循环；
    # result=1+2=3；result现在是等于3了 = 上层result是1；2是a，因为这是第二个循环，；
    # result=3+3=6；result现在是等于6了 = 上层result是3；3是a，因为这是第三个循环，；以此循环到100.
    a += 1
print(result)

a = 0
result = 0      #结果变量,从0开始。
while a <= 100:
    result = result + a   #因为是循环语句也要循环着加，a循环着变大到100，
    a += 2
print(result)

a1 = 0
result1 = 0      #结果变量,从0开始。这必须从0开始，从1的话结果会多一。
while a1 <= 100:
    if a1 % 2 == 0:
        result1 += a1
    a1 += 1
print(result1)

i = 1
while i <= 5:
    if i == 3:
        print('卧槽，游从之')
        i += 1               ##注意计数器，一定要在continue之前处理计数器，不然会陷入死循环。
        continue
    print(f'我吃了{i}个苹果')
    i += 1
#    if i == 4:
#        print('卧槽，游从之')
#        continue

#一套嘿嘿，一个第几套标志
j = 1
while j <= 5:
    i = 1
    while i <= 5:
        print('嘿嘿')
        i += 1
    print(f'第{j}套')
    j += 1

j = 1
while j <= 5:
    i = 1
    while i <= 5:
        print('*',end='')   #end=''就不会换行，循环打5个
        i += 1
    print('')               #让上面的内部代码块执行完以后换行。print默认换行嘛。
    j += 1


j1 = 1
while j1 <= 5:
    i1 = 1                 #第二次进入循环，i1刷新为1，而j1还是大循环加到的2。
    while i1 <= j1:        #第一次循j1=1 <= i1=1,条件满足往下走，然后打印一个*不换行，然后i1+1=2了，j1=1 <= i1=2也就不成立了。
        print('*',end='')
        i1 += 1
    print('')
    j1 += 1                #i1和j1联动，一起飞翔。也就做到了，你几次我就几次。
'''

j2 = 1
while j2 <= 9:
    i2 = 1                   #第二次进入循环，i2刷新为1，而j2还是大循环加到的2。
    while i2 <= j2:          #第一次循j2=1 <= i2=1,条件满足往下走，然后打印一次不换行，然后i2+1=2了，j2=1 <= i2=2也就不成立了。
        z = j2*i2            #j2=1 <= i2=2也就不成立了，嵌套在大while里的小while也就没法循环了。
        print(f'{j2}*{i2}={z}',end='\t')
        i2 += 1
    print('')
    j2 += 1
else:
    print('你看着乘法口诀表行不行？')

for i in 'hello':
    if i == 'x':
        print('跳过x')
        continue          ##如果这是break的话，下面的else也不会执行,不管是while还是for。
        print(i)
else:                 ##for循环结束循环后执行else。
    print('wocao')