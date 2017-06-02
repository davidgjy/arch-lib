import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='apache', db='mysql', port=3306, charset='utf8')
cur = conn.cursor()
cur.execute("USE smt")
cur.execute("SELECT * FROM users")
print(cur.fetchone())
cur.close()
conn.close()