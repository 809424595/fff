#_*_conding:utf-8_*_
#@Time    :2020/2/1114:54
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
from selenium.webdriver.common.by import By


class HomePageLocs:
    # 我的帐号  元素
    my_user_name = (By.XPATH, '//a[contains(text(),"我的帐户")]')
    #首页抢投标按钮
    bid_button = (By.XPATH,'//a[@class="btn btn-special"]')