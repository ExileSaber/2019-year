import requests
url = 'http://192.168.99.100:8050/render.html?url=https://www.baidu.com&wait=5'
response = requests.get(url)
print(response.text)