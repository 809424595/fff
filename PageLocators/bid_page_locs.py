#_*_conding:utf-8_*_
#@Time    :2020/2/1315:18
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
from selenium.webdriver.common.by import By

class BidPageLocs:

    #金额输入框
    money_input= (By.XPATH,'//input[@class="form-control invest-unit-investinput"]')
    #标的余额
    bid_money_text = (By.XPATH,'//div[contains(@class,"money_overplus")]//span[text()="剩余："]/following-sibling::span')
    #投标按钮
    invest_button= (By.XPATH,'// button[text() = "投标"]')
    # 投资成功弹出框 - 查看并激活按钮
    active_button_on_successPop = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败 - 弹出框 - 提示信息
    invest_failed_popup = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]')
    # 投资失败 - 弹出框 - 关闭弹出框
    invest_close_failed_popup_button = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//a')
    # 金额输入框输入符号非100的整数倍 - 按钮 -提示信息
    invest_button_error_form = (By.XPATH,'//div[@class="pd-right"]//button[text()="请输入10的整数倍"]')