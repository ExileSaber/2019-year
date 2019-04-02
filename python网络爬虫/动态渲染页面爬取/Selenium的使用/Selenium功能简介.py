from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')  # get方法请求网页
    input = browser.find_element_by_id('kw')  # 根据id值提取节点（此处为搜索框），find_element_by_name()根据name值提取节点，返回类型为WebElement类型
    '''
    find_element_by_css_selector('#q')  # 根据CSS选择器和XPath获取
    find_element_by_xpath('//*[@id="q"]')  # 根据XPath获取
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    还有一个通用的方法
    find_element() 需要传入两个参数，一个是查找方式By，另一个是值
    find_element_by_id(id)等价于find_element(By.id, id)
    如果需要查找所有满足条件的节点
    find_elements()
    '''

    input.send_keys('Python')  # send_keys方法用于输入文字
    input.send_keys(Keys.ENTER)  # 按enter
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
    print(browser.current_url)  # 获取url
    print(browser.get_cookies())  # 获取cookies
    print(browser.page_source)  # page_source属性是页面源代码
finally:
    browser.close()


# 最终结果说明
'''
自动弹出一个Chrome浏览器，浏览器首先跳转到百度，然后再搜索框中输入Python，接着调转到搜索结束页，最后关闭
控制台分别输出当前的URL，当前的Cookies，网页源代码
'''