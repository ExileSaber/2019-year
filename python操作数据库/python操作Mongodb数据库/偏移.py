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

results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)  #此处用skip方法向后便宜2个位置，limit方法限制返回的数据数量为2
print([result['name'] for result in results])

#注意
#数据库数量非常庞大时，最好不要使用大偏移量，可能导致内存溢出
#一般采取 _id 属性来定位
#from bson.objectid import ObjectId
#collection.find({'_id':{'$gt':ObjectId('5c650ffa70dfb94e6cfd7466')}})  需要记录好上次查询的 _id
