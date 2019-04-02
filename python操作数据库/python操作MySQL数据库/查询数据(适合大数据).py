import pymysql

db = pymysql.connect(host='localhost', user='root', password='524930lwm', db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'  #查询年龄20岁以上的学生

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:',row)
        row = cursor.fetchone()
except:
    print('Error')