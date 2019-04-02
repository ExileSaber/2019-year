import pymysql

db = pymysql.connect(host='localhost',user='root',password='524930lwm',db='spiders')
cursor = db.cursor()

#根据操作的不同改变其相应数据
data = {
    'id': '20120004',
    'name': 'Mike',
    'age': 22
}  #设置你要传入的数据内容
table = 'students'  #要操作的表格

#不用更改的部分
keys = ','.join(data.keys())  #设置要插入的字段
values = ','.join(['%s']*len(data))  #设置占位符

sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)  #sql指令
try:
    if cursor.execute(sql, tuple(data.values())):  #执行操作
        print('Successful')
        db.commit()  #确定更改
except:
    print('Failed')
    db.rollback()  #数据回滚

db.close()
