# 有些操作Selenium没有提供，这时可以通过模拟运行JavaScript，此时通过使用execute_script()来实现
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')