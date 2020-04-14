'''
import pymysql.cursors
db = pymysql.connect("192.168.17.73", "test", "NArwq5F2I%84qyWM","information_schema")
testc = db.cursor()
testc.execute("SELECT TABLE_NAME,TABLE_ROWS,DATA_LENGTH/1024/1024,'MB' FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'vvt' ORDER BY TABLE_ROWS DESC;")
data3 = (testc.fetchall())
data = []
for i in range(len(data3)):
    a = (data3[i]);
    data.append(a)
print(data)
db.close()

import smtplib
from email.mime.text import MIMEText
from_addr = '1606059673@qq.com'
password = 'hfbxmiygmubvjbii'
to_addr = '1606059673@qq.com'
#to_addr = 'yuft@irongbei.com'
smtp_server = 'smtp.qq.com'
msg = MIMEText(f'{data}','plain','utf-8')
msg["Subject"] = 'MySQL状态通知'
msg["From"] = '牛顿'
server = smtplib.SMTP(smtp_server,587)
#server1.connect(smtp_server,465)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
'''
import prettytable as pt
from prettytable import from_db_cursor
import MySQLdb.cursors
db = MySQLdb.connect("prod-irongbei-master.mysql.rds.aliyuncs.com", "ironbei_09981", "LEBYPZgnNEcFGORnw3L3","information_schema",cursorclass = MySQLdb.cursors.DictCursor)
testc = db.cursor()
testc.execute("SELECT TABLE_NAME,TABLE_ROWS as 'table_row',concat(Round(DATA_LENGTH/1024/1024,0),'MB') as 'table_size' FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'vvt' ORDER BY TABLE_ROWS DESC;")
data3 = (testc.fetchall())

tb = pt.PrettyTable()
for line in data3:
    tb.field_names = ['table',"table_row", "table_size"]
    tb.add_row([line['TABLE_NAME'],line['table_row'], line['table_size']])    ##对应sql查询的条件名称。
    tb.right_padding_width = 2
    tb.align['table'] = 'l'
    tb.align['table_row'] = 'l'
    tb.align['table_size'] = 'l'
#vvt库的大小。
testb = db.cursor()
testb.execute("select concat(round(sum(DATA_LENGTH/1024/1024/1024),2),'GB') as data from TABLES where table_schema='vvt';")
data2 = testb.fetchall()

import smtplib
from email.mime.text import MIMEText
from_addr = '1606059673@qq.com'
password = 'qlkgwylisoifjdgh'
to_addr = 'yunweilist@irongbei.com'
smtp_server = 'smtp.qq.com'
mail_msg = f'prod.vvt.总体积:{data2}\nvvt各表详情:\n{tb}'
msg = MIMEText(mail_msg,'plain','utf-8')
msg["Subject"] = 'MySQL状态通知'
msg["From"] = '于芳涛'
server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()