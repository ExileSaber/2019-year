import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing import Pool

def get_page(offset):  # 发送请求，获取源码
    params = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        'keyword': '风景',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    # 网址有变动，需要按情况更改
    # aid=24&offset=0&format=json&keyword=%E9%A3%8E%E6%99%AF&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):  # 选取数据，并抓下来
    if json.get('data'):
        items = json.get('data')
        for item in items:
            if 'title' in item.keys():
                title = item['title']
            if 'large_image_url' in item.keys():
                image = item['large_image_url']
            yield {
                'image': image,
                'title': title
            }


def save_image(item):  # 保存图片
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))  # 根据item里面的title来创建文件夹
    try:
        response = requests.get(item.get('image'))  # 请求图片链接
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')  # 图片名称可以使用其内容的md5的值，避免重复
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 5


if __name__ == '__main__':
    pool = Pool()  # 调用了多线程的线程池，调用其map方法实现多线程下载
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
