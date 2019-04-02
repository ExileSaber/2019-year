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

results = collection.find().sort('name', pymongo.ASCENDING)  #传入排序的字段和升降序标志，升序排列 pymongo.ASCENDING，降序排列 pymongo.DESCENDING
print([result['name'] for result in results])