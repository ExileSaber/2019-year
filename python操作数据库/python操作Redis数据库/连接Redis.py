from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password=None)
redis.set('name', 'Bob')
print(redis.get('name'))

#方法二
'''
from redis import StrictRedis,ConnectionPool
pool = ConnectionPool(host='localhost', port=6379, db=0, password=None)
redis = StrictRedis(connection_pool=pool)
#更多用法见书222面
'''
#其他操作见书222面
