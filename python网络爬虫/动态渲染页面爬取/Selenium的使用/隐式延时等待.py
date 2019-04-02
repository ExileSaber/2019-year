from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)  # 如果selenium没有在DOM中找到节点，将继续等待超出设定时间后，则抛出找不到节点的异常
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)