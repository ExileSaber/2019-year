from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')  # 指定要查找的节点，然后指定一个最长等待时间，规定时间加载出来这个节点就返回该节点，若果超过规定时间没有找到，则抛出异常
wait = WebDriverWait(browser, 10)  # 引入WebDriverWait对象，并指定最长等待时间
input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
# 调用其until方法，传入要等待条件，此处传入presence_of_elements_located这个条件，代表节点出现的意思，其参数是节点的定位元素，也就是ID为q的节点搜索框

button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))  # 按钮的等待条件element_to_be_clickable，也就是可以点击，查找按钮时查找CSS选择器为.btn-search的按钮
print(input, button)


# 其他等待条件见书259面