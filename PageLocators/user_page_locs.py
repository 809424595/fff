#_*_conding:utf-8_*_
#@Time    :2020/2/1811:33
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
from selenium.webdriver.common.by import By

class UserPageLoc:

    #可用余额
    user_leftMoney = (By.XPATH,'//li[@class="color_sub"]')