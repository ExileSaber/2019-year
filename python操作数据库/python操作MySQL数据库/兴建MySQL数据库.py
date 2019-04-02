import pymysql
db = pymysql.connect(host='localhost',user='root',password='524930lwm',port=3306)  #连接MySQL数据库
cursor = db.cursor()  #获得MySQL的操作游标，利用游标来执行SQL语句
#
# execute为执行方法，执行内容为字符串指令
cursor.execute('SELECT VERSION()')  #用于获得当前MySQL版本
data = cursor.fetchone()  #获得第一条数据，即版本号
print('Database version:',data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")  #创建名为spiders的数据库，默认编码为UTF-8
db.close()