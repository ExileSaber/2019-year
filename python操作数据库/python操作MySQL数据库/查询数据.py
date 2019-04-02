import pymysql

db = pymysql.connect(host='localhost', user='root', password='524930lwm', db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'  #查询年龄20岁以上的学生

try:
    cursor.execute(sql)  #将查询结果传给execute方法
    print('Count:', cursor.rowcount)  #调用cursor的rowcount属性获取查询结构的条数
    one = cursor.fetchone()  #此方法获取结结果地点第一条数据，元组形式返回
    print('One:', one)

    #数据量小时
    results = cursor.fetchall()  #得到指针后面的全部数据，以元组形式一次性返回，数据量越大开销越大
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

db.close()