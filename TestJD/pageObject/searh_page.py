from TestJD.basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    # 收索框查找
    input_id = (By.ID, "kw")
    # 点击按钮操作
    click_id = (By.ID, "su")

    # 对收索狂进行输入
    def input_text(self, input_keys):
        self.locater(self.input_id).send_keys(input_keys)

    # 点击查询按钮，实现本次收索
    def click_element(self):
        self.locater(self.click_id).click()

    # 校验是否实现查询功能
    def check_click(self, url, input_keys):
        self.visit(url)
        self.input_text(input_keys)
        self.click_element()
        # self.quit_browser()


if __name__ == '__main__':
    url = "http://www.baidu.com"
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    sp.visit(url)
    sp.input_text("何东")
    sp.click_element()
    sp.quit_browser()