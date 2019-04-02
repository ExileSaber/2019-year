import pymongo

#创建数据库连接
client = pymongo.MongoClient(host='localhost', port=27017)
#另一种连接方式
#client = pymongo.MongoClient('mongodb://localhost:27017/')

#指定数据库
db = client.test
#或者
#db = client['test']

#指定集合
collection = db.students
#collection = db['students']

#查询数据,find_one查询单个结果
result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

#查询数据，find查询多个结果,返回一个生成器对象
results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)

#查询数据，用 MongoDB在插入过程中自动添加的自动添加的 _id 属性
from bson.objectid import ObjectId
result = collection.find_one({'_id': ObjectId('5c650ffa70dfb94e6cfd7466')})
print(result)

#比较符号
#查询年龄大于20的数据，写法如下
#results= collection.find({'age': {'$gt': 20}})
#特定的比较符号网上查

#功能符号
#查询名字以M开头的学生数据，实例如下
#results = collection.find({'name': {'$regex': '^M.*'}})  此处使用 $regex 来指定正则匹配，'^M.*'代表以M开头的正则表达式
#特定的功能符号网上查

#MongoDB官方文档：http://docs.mongoDB.com/manual/reference/operator/query
