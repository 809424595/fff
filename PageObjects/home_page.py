#_*_conding:utf-8_*_
#@Time    :2020/2/1017:42
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.home_page_locs import HomePageLocs as loc

class HomePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 用户名是否存在
    def user_is_existed(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.my_user_name))
        except:
            return False
        else:
            return True

    #点击首页第一个抢投标
    def click_first_bid(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.bid_button))
        self.driver.find_element(*loc.bid_button).click()

