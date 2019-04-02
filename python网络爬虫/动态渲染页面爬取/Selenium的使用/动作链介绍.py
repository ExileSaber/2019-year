# 此处实现了一个拖拽操作，动作链还包括键盘按键
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')  # 找到要拖拽的节点
target = browser.find_element_by_css_selector('#droppable')  # 找到要拖拽到的目标节点
actions = ActionChains(browser)  # 声明ActionChains对象并将其赋值给actions
actions.drag_and_drop(source, target)  # 接着就可以调用其drag_and_drop方法
actions.perform()  # 执行操作