from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
# from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'  # 定义base_url来表示请求的URL的前半部分

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


# 请求函数，获取网页内容
def get_page(page):
    params = {  # 构造参数字典，唯一变量page设为函数参数
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1005052830678474',
        'page': page,
    }
    url = base_url + urlencode(params)  # 调用urlencode方法将字典类型转化为URL的GET请求参数，即类似于type=uid&value=2830678474&containerid=1076032830678474的形式，再拼接
    try:
        response = requests.get(url, headers=headers)  # 用requests请求这个链接
        if response.status_code == 200:  # 判断响应的状态码
            print('page', page, 'Connect successful')
            return response.json()  # 调用json方法将内容解析为JSON返回
    except requests.ConnectionError as e:
        print('Error', e.args)  # 捕获异常k


# 解析函数，筛选需要的信息
def parse_page(json):
    if json:
        items = json.get('data').get('userInfo')  # 选择data节点中的userInfo节点
        weibo = {}
        for item in items:
            weibo[item] = items[item]
        yield weibo  # 类似于return的效果，得到一个数值返回一个数值

# 保存到mongoDB数据库
'''
client = MongoClient()
db = client['weibo']
collection = db['weibo']


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')
'''

def get_weibo_information(weibo):
    print('博主id：', weibo['id'])
    print('博主昵称：', weibo['screen_name'])
    print('博主头像：', weibo['profile_image_url'])
    print('微博网址：', weibo['profile_url'])
    print('博客数量：', weibo['statuses_count'])
    print('是否认证：', weibo['verified'])
    print('微博说明：', weibo['description'])
    print('博主性别：', weibo['gender'])
    print('微博等级：', weibo['urank'])
    print('粉丝数量：', weibo['followers_count'])
    print('关注数量：', weibo['follow_count'])
    print('背景图片：', weibo['cover_image_phone'])


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            print('部分整理格式后：')
            get_weibo_information(result)
            # save_to_mongo(result)





