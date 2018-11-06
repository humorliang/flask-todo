# coding:utf-8
import pymysql

con = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='qQwer@@1234',
    port=3306,
    database='android_app'
)
print(con)
cur = con.cursor()
print(cur)
cur.execute("select * from user")
print(cur.fetchone())
