#_*_conding:utf-8_*_
#@Time    :2020/2/1811:36
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
from PageLocators.user_page_locs import UserPageLoc as loc
from Common.basepage import BasePage

class UserPage(BasePage):
    # 获取用户余额
    def get_user_left_money(self):
        text = self.get_element_text(loc.user_leftMoney, "个人页面_获取用户余额")
        return text.strip("元")