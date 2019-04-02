import pymysql

db = pymysql.connect(host='localhost', user='root', password='524930lwm', db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'  #设置删除条件：有大于，小于，等于，LIKE等

sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)  #条件连接符有AND，OR等
try:
    cursor.execute(sql)
    print('Successful')
    db.commit()
except:
    print('Failed')
    db.rollback()

db.close()