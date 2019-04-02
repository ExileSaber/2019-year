import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost',user='root',password='524930lwm',db='spiders')
cursor = db.cursor()

sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'  #有几个value写几个%s
try:
    cursor.execute(sql,(id, user, age))  #第一个参数是sql指令，第二个参数是元组类型的要传进去的值
    db.commit()  #需要执行commit方法才可以实现插入数据
except:
    db.rollback()  #加了一层异常处理，调用rollback实现数据回滚，相当于什么都没有发生
#加上异常处理的原因！！！
#事务的四个属性
#原子性：事务中包括的诸操作要么都做要么都不做，不会有做到一半的情况
#一致性：事务必须使数据库从一个一致性状态变到另一个一致性状态
#隔离性：一个事务的执行不能被其他事务干扰也不会干扰其他事务
#持久性/永久性：一个事务一旦提交，它对数据库中数据的改变就是永久的，接下来的其他操作或者故障不应该对其有任何影响

#插入，更新，删除操作都是对数据库进行更改的操作，其必为一个事务，因此都应该加上异常处理

db.close()