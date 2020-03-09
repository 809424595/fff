#_*_conding:utf-8_*_
#@Time    :2020/2/1314:13
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

import time
import logging
from selenium import webdriver
from PageObjects.home_page import HomePage
from PageObjects.bid_page import BidPage
from PageObjects.login_page import LoginPage
from PageObjects.user_page import UserPage
from TestDatas import Common_Datas as CD
from TestDatas import invest_datas as ID
from Common import logger
import pytest

@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.login_url)
    LoginPage(driver).login(CD.user, CD.passwd)
    bp = BidPage(driver)
    yield driver,bp
    driver.quit()

@pytest.fixture
def mysetup():
    logging.info("----这是每个测试用例的前置----")
    yield
    logging.info("----这是每个测试用例的后置----")

@pytest.fixture("class")
def myclass():
    logging.info("----这是测试用例类的前置----")
    yield
    logging.info("----这是测试用例类的后置----")

@pytest.mark.usefixtures("init_driver")
@pytest.mark.usefixtures("myclass")
@pytest.mark.usefixtures("mysetup")
class TestInvest:

    # @pytest.mark.smoke    #为测试用例打标记
    def test_invest_success(self,init_driver):
        """
        正向场景 - 投资成功：投资金额固定为1000
        """
        # 步骤
        logging.info("投资功能 - 正常场景用例：投资1000元成功。用户可用余额减少1000，标余额减少1000 ")
        # 1、首页 - 第一标 - 抢投标
        HomePage(init_driver[0]).click_first_bid()
        # 2、标页面 - 获取输入框当中，投资前的用户余额
        user_money_before_invest = init_driver[1].get_user_money()
        # 3、标页面 - 获取标的余额，投资前。
        bid_money_before_invest = init_driver[1].get_bid_left_money()
        # 4、标页面 - 输入金额20000，点击投标
        init_driver[1].invest(ID.success["money"])
        # 5 、标页面 - 成功弹出框当中，点击查看并激活
        init_driver[1].click_active_button_in_success_popup()
        # 6 、个人页面获取用户的余额
        user_money_after_invest = UserPage(init_driver[0]).get_user_left_money()
        # 7 、 回退到表页面刷新后再次获取表的余额
        init_driver[0].back()
        time.sleep(2)
        init_driver[0].refresh()
        #成功投资后标的余额
        bid_money_after_invest = init_driver[1].get_bid_left_money()
        # 断言
        # 1、用户余额少了1000
        assert  ID.success["money"] == int(float(user_money_before_invest)-float(user_money_after_invest))
        # 2、标的可投余额少了1000
        # assert  ID.success["money"] != int(float(bid_money_after_invest)-float(bid_money_before_invest))

    # # 异常场景: 数据字段 格式校验 - 弹框提示金额格式不对。
    @pytest.mark.huigui
    @pytest.mark.parametrize("case",ID.invalid_data_format)
    def test_invest_failed_invalid_money(self,case,init_driver):
        logging.info("投资功能 - 异常场景用例：投资金额有效性校验 - 投资金额为非100的整数倍、错误的格式等")
        # 1、标页面 - 获取输入框当中，投资前的用户余额
        user_money_before_invest = init_driver[1].get_user_money()
        # 2、标页面 - 获取标的余额，投资前。
        bid_money_before_invest = init_driver[1].get_bid_left_money()
        # 3、标页面：投标动作；
        init_driver[1].invest(case["money"])
        # 4、获取页面提示信息
        error_msg = init_driver[1].get_errorMsg_from_pageCenter()
        # 5、刷新当前页面，获取用户余额、标余额。
        init_driver[0].refresh()
        user_money_after_invest = init_driver[1].get_user_money()
        bid_money_after_invest = init_driver[1].get_bid_left_money()
        # 6、断言 - 提示信息是否正确。标的金额不变，用户的余额也不变。
        assert  error_msg == case["check"]
        assert user_money_before_invest == user_money_after_invest
        assert  bid_money_before_invest == bid_money_after_invest

    # # 异常场景：数据字段 格式校验 - 弹框提示金额格式不对（输入非数字的字符）。
    # # @ddt.data(*ID.invalid_data_no10)
    @pytest.mark.parametrize("datas",ID.invalid_data_no10)
    def test_invest_failed_no_invalid_money(self, datas,init_driver):
        logging.info("投资功能 - 异常场景用例：投资金额有效性校验 - 投资金额为非数字的字符、符号等")
        # 1、标页面 - 获取输入框当中，投资前的用户余额
        user_money_before_invest = init_driver[1].get_user_money()
        # 2、标页面 - 获取标的余额，投资前。
        bid_money_before_invest = init_driver[1].get_bid_left_money()
        # 3、标页面：投标动作；
        init_driver[1].invest(datas["money"])
        # 4、获取按钮提示信息
        button_error_msg = init_driver[1].get_errorMsg_from_buttonCenter()
        # 5、刷新当前页面，获取用户余额、标余额。
        init_driver[0].refresh()
        user_money_after_invest = init_driver[1].get_user_money()
        bid_money_after_invest = init_driver[1].get_bid_left_money()
        # 6、断言 - 提示信息是否正确。标的金额不变，用户的余额也不变。
        assert  button_error_msg == datas["check"]
        assert  user_money_before_invest == user_money_after_invest
        assert  bid_money_before_invest == bid_money_after_invest











