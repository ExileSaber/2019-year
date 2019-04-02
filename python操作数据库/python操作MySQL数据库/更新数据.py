import pymysql

db = pymysql.connect(host='localhost',user='root',password='524930lwm',db='spiders')
cursor = db.cursor()

sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (20, 'Bob'))
    db.commit()
except:
    db.rollback()

db.close()