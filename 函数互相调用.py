def test1():
    print('这是test1')

def test2():
    print('这是test2 #start')
    test1()           #调用函数test1。
    test1()
    print('这是test2 #end')
#test2()

def fgx():
    print('--' * 40)


def fgxs(num):
    i = 0
    while i < num:
        fgx()          #调用函数
        i += 1

fgxs(5)

