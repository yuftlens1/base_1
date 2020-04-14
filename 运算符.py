a=11//2     #//整除
print(a)

b=3**3      #3的3次方
print(b)

c=1+2*2
print(c)

d=(1+2)*2    #()提高优先级
print(d)

num1,num2,num3='q','w','e'   #多变量赋值
print(num2)

num4=num5=10        #多变量赋相同值
print(num4)
print(num5)
#以下是复合赋值运算符
num6=5
#num6+=6       #num6=num6+6  #num6=5+6 # 11
#num6-=6      #num6=num6-6  #num6=5-6 # -1
#num6*=6        #30
num6 *= 6 + 2   #先算运算符右面的 6+2=8    #num6=num6*8    #num6=5*8  #40
print(num6)
#布尔值
print(1==1)    #判断，布尔值。 注意python在运算的时候 == 才是等于。
#逻辑运算符
num7=1
num8=2
num9=3
print(num7 < num8 and num7 < num9)  #and都对为真
print((num7 < num8) and (num7 < num9))  #and都对为真  ##and作用最好加上括号，方便看。
print(num7 > num8 or num7 > num9)   #or一对为真，全错为假。
print(not num8 < num8)  #not取反
#数字间的逻辑运算。
print((1) and (2))   #and只要有一个值为0，则结果为0，否则结果为最后一个非0的数字。
print((0) and (2))
print((1) or (2))    #or 只要全部为0才返回0，否则返回第一个非0的数字。
print((0) or (3))    #因为不返回0，直接返回第二位的3了？？？