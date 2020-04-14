import pymysql.cursors
db = pymysql.connect("192.168.17.73", "test", "NArwq5F2I%84qyWM","information_schema")
#db = pymysql.connect("192.168.17.73", "dev_rbv2_ac", "QeTcdhqYP7lGjkwJ8yKaXfON","dev_rongbei_v2_account")
'''
#vvt库里的各个表行数。
test = db.cursor()
test.execute("select table_name,table_rows from tables where TABLE_SCHEMA = 'vvt' order by table_rows desc;")
data = test.fetchall()
print(data)
#所有数据库的总大小
testa = db.cursor()
testa.execute("select concat(round(sum(DATA_LENGTH/1024/1024/1024),2),'GB') as data from TABLES;")
data1 = testa.fetchall()
print(data1)
#vvt库的大小。
testb = db.cursor()
testb.execute("select concat(round(sum(DATA_LENGTH/1024/1024),2),'MB') as data from TABLES where table_schema='vvt';")
data2 = testb.fetchall()
print(data2)
'''
testc = db.cursor()
testc.execute("SELECT TABLE_NAME,TABLE_ROWS,DATA_LENGTH/1024/1024,'MB' FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'vvt' ORDER BY TABLE_ROWS DESC;")
data3 = testc.fetchall()
print('(tables_name    rows        size)')
for i in range(len(data3)):
   print(data3[i])
db.close()