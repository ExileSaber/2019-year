from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)

# 获取属性
logo = browser.find_element_by_id('zh-top-link-logo')  # 获取logo节点
print(logo)
print(logo.get_attribute('class'))  # 获取其class

# 获取文本值（属性值）
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

# 获取id，位置，标签名和大小（属性值）
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
