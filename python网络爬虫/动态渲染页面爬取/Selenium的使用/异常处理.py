# 超时，节点未找到等错误，用try except来捕获异常

# 节点未找到异常
'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.find_element_by_id('hello')
# 这里会抛出节点未找到异常
'''
# 更改后的程序
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://baidu.com')
except TimeoutException:
    print('Time Out')

try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

