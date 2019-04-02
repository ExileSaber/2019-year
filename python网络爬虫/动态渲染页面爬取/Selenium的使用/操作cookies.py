from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())  # 获取全部cookies
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})  # 新加一项cookie
print(browser.get_cookies())
browser.delete_all_cookies()  # 删除所有cookies
print(browser.get_cookies())