import unittest
from selenium import webdriver
from TestJD.pageObject.searh_page import SearchPage
from ddt import ddt, data, unpack
import time


@ddt
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        driver = webdriver.Chrome()
        # driver.implicitly_wait(10)
        # WebDriverWait(driver, 20, 0.5).until(lambda el:driver.find_element_by_id('//*[@id = "kw"]'))
        self.sp = SearchPage(driver)

    def tearDown(self) -> None:
        self.sp.quit_browser()

    @data(["http://www.baidu.com", "波斯猫"])
    @unpack
    def test_1(self, url, input_keys):
        self.sp.check_click(url, input_keys)
        time.sleep(30)


if __name__ == '__main__':
    unittest.main()
