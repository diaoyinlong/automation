import pymysql

from Public.Toolkit import Toolkit

UserName = 'TestUser_' + Toolkit.get_random_value()

with pymysql.connect(host='localhost', user='root', passwd='', db='test') as conn:
    cur = conn.cursor()
    x = "insert into person values ('" + UserName + "','123456','OK')"
    cur.execute(x)
    conn.commit()
