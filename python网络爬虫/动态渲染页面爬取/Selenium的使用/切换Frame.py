# 网页中有一种节点叫作iframe，也就是子frame，相当于页面的子页面，用Selenium打开网页后，默认为在父级Frame里面操作
# 要获取子frame里面的节点就需要切换frame
import time
from selenium import webdriver
# from selenium.common.exceptions import NoSuchAttributeException 由于库的更新，NoSuchAttributeException这个东西被移除了

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')  # 切换到子frame
try:
    logo = browser.find_element_by_class_name('logo')
except:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)