#_*_conding:utf-8_*_
#@Time    :2020/2/1315:14
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

from Common.basepage import BasePage
from PageLocators.bid_page_locs import BidPageLocs as loc


class BidPage(BasePage):

    #获取用户余额
    def get_user_money(self):
        return self.get_element_attribute     (loc.money_input, "data-amount", "标页面_获取用户余额")

    #获取标的余额
    def get_bid_left_money(self):
        return self.get_element_text(loc.bid_money_text,"标页面_标当前剩余的可投余额")

    #投标
    def invest(self,money):
        self.input_text(loc.money_input, money, "标页面_输入框当中输入投资金额", )
        self.click_element(loc.invest_button, "标页面_提交投资操作")

    # 点击 投资成功提示框 当中的  查看并激活按钮
    def click_active_button_in_success_popup(self):
        self.click_element(loc.active_button_on_successPop, "标页面_投资成功的提示框 - 点击查看并激活")

    # 错误提示框 - 页面中间
    def get_errorMsg_from_pageCenter(self):
        msg = self.get_element_text(loc.invest_failed_popup, "标页面_投资失败提示框 - 提示信息获取")
        self.click_element(loc.invest_close_failed_popup_button, "标页面_关闭投资失败提示框")
        return msg
    #错误提示框 - 按钮中间
    def get_errorMsg_from_buttonCenter(self):
        return self.get_element_text(loc.invest_button_error_form,"标页面_输入非数字_投标按钮信息获取")
