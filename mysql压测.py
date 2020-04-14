import pymysql.cursors
conn = pymysql.connect("192.168.17.73", "test", "NArwq5F2I%84qyWM","information_schema")
cur = conn.cursor()

def timer(fn):
    def _wrapper(count):
        start = time.time()
        fn(count)
        seconds = time.time() - start
        print(u"{func}函数每 {count} 条数数据写入耗时 {sec}秒".format(func=fn, count=count, sec=seconds))
    return _wrapper
# 普通写入
@timer
def ordinary_insert(count):
    sql = "insert into students1 (name, age, sex,id,cellphone,address,score) values ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66')"
    for i in range(count):
        cur.execute(sql)



# 批量处理
@timer
def many_insert(count):
    sql = "insert into students1 (name, age, sex,id,cellphone,address,score)values(%s,%s,%s,%s,%s,%s,%s)"

    loop = count / 20
    stus = (('tom666','66','boy','10066','13900000066','shanghai','66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'),
            ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66'),('tom666','66','boy','10066','13900000066','shanghai','66'))

    for i in range(int(loop)):
        cur.executemany(sql, stus)



# 事务处理
@timer
def transaction_insert(count):
    sql = "insert into students1 (name, age, sex,id,cellphone,address,score)values(%s,%s,%s,%s,%s,%s,%s)"
    stus = ('tom666', '66', 'boy', '10066', '13900000066', 'shanghai', '66')

    if count > 0:
        try:
            for i in range(count):
                cur.execute(sql, stus)
        except Exception as e:
            conn.rollback()  # 事务回滚
            print('事务处理失败', e)
        else:
            conn.commit()  # 事务提交
            print('事务处理成功, 关闭连接', cur.rowcount)
            cur.close()
            conn.close()
    else:
        print("输入的count有问题，无法执行数据库操作！")


def test_insert(count):
    ordinary_insert(count)
    many_insert(count)
    transaction_insert(count)


test_insert(20)