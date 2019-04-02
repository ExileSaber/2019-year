import pymongo

#创建数据库连接
client = pymongo.MongoClient(host='localhost', port=27017)
#另一种连接方式
#client = pymongo.MongoClient('mongodb://localhost:27017/')

#指定数据库
db = client.test
# 或者
#db = client['test']

#指定集合
collection = db.students
#collection = db['students']

condition = {'name': 'Jordan'}  #指定查询条件
student = collection.find_one(condition)  #先查询数据
student['age'] = 29  #改变的数据
result = collection.update(condition, student)  #再更新数据，指定更新的条件和更新后的数据即可，官方不推荐使用此方法
print(result)  #输出结果中 ok代表执行成功，nModified代表影响的数据条数


#官方推荐的，update_one / update_many
condition = {'name': 'Mike'}  #指定查询条件
student = collection.find_one(condition)  #先查询数据
student['age'] = 25
result = collection.update_one(condition, {'$set': student})  #只更新student字典内存在的字段，原先的其他字段不会更新，也不会删除，第二个参数格式必须按要求
print(result)  #上一个函数返回结果为UpdateResult类型
print(result.matched_count, result.modified_count)  #调用两个属性，分别为匹配的数据条数和影响的数据条数

#update_one和update_many的区别
'''
#update_one方法
condition = {'age': {'$gt': 20}}  #查询条件为年龄大于20
result = collection.update_one(condition, {'$inc': {'age': 1}})  #更新条件为年龄+1，用update_one只将找到的第一个符合条件的数据更新
print(result)
print(result.matched_count, result.modified_count)

#update_many方法
condition = {'age': {'$gt': 20}}  #查询条件为年龄大于20
result = collection.update_one(condition, {'$inc': {'age': 1}})  #更新条件为年龄+1，用update_many将找到的所有符合条件的数据更新
print(result)
print(result.matched_count, result.modified_count)
'''