# 这是基本类
from selenium import webdriver


class BasePage(object):
    # driver = webdriver.Chrome()

    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def locater(self, locater):
        return self.driver.find_element(*locater)

    # 获取URL
    def visit(self, url):
         self.driver.get(url)

    # 网页退出
    def quit_browser(self):
        self.driver.quit()
