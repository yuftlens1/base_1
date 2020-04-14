import pymysql.cursors
db = pymysql.connect("192.168.17.73", "test", "NArwq5F2I%84qyWM","information_schema")
testc = db.cursor()
testc.execute("SELECT TABLE_NAME,TABLE_ROWS,DATA_LENGTH/1024/1024,'MB' FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'vvt' ORDER BY TABLE_ROWS DESC;")
data3 = testc.fetchall()
#print(eval(data3))
print(data3)
db.close()