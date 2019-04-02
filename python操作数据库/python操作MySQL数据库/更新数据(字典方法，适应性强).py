import pymysql

db = pymysql.connect(host='localhost', user='root', password='524930lwm', db='spiders')
cursor = db.cursor()

# 根据操作的不同改变其相应数据
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 23
}  # 设置你要传入的数据内容
table = 'students'  # 要操作的表格

# 不用更改的部分
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)  # 如果主键不存在就执行插入操作，存在就执行更新操作
update = ','.join(["{key} = %s".format(key=key) for key in data])
sql += update  # 完整的sql指令：INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s
try:
    if cursor.execute(sql, tuple(data.values())*2):  # 此处出入的参数就要有六个
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()

db.close()