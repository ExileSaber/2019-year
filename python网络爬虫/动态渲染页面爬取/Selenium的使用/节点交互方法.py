from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')  # 先找到搜索框
input.send_keys('iPhone')  # 在搜索框中输入内容的方法
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')  # 找到按钮
button.click()  # 点击按钮的方法


# 更多操作方法见：http://selenium-python.redthedoes.io/api.html#module-selenium.webdriver.remote.webelement