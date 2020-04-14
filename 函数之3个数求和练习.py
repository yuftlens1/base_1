def sum_num(a,b,c):
    return a + b + c

number1 = int(input('请输入整数:'))
number2 = int(input('请输入整数:'))
number3 = int(input('请输入整数:'))
# result = sum_num(number1,number2,number3)
# result = sum_num(1,2,3)
#print(result)

def average_num(a,b,c):         #result是结果的意思。
    numresult = sum_num(a,b,c)
    # numresult = sum_num(a,b,d)     #求和和平均都用的是同样的一组数据(a,b,c)，所以这sum_num的参数必须是(a,b,c)
    return numresult / 3
# resultaverage = average_num(1,2,3)
resultaverage = average_num(number1,number2,number3)
print(resultaverage)
