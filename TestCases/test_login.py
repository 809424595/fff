#_*_conding:utf-8_*_
#@Time    :2020/2/1017:41
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
import time
import ddt
import logging
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import Common_Datas as CD
from TestDatas import login_datas as LD
from Common import logger
import pytest

@pytest.fixture
def setup():
    # 打开浏览器
    driver = webdriver.Chrome()
    #窗口最大化
    driver.maximize_window()
    #访问登录页面
    driver.get(CD.login_url)
    lp = LoginPage(driver)

    yield  driver,lp   #yield为分割线及返回值之前为前置条件之后为后置条件（如果范围多个参数是就会返回一个元组）
    driver.quit()

@pytest.fixture
def mysetup():
    logging.info("----这是每个测试用例的前置----")
    yield
    logging.info("----这是每个测试用例的后置----")

@pytest.fixture("class")
def myclass():
    logging.info("----这是测试类级别的前置")
    yield
    logging.info("----这是测试类级别的后置")


# @ddt.ddt
@pytest.mark.usefixtures("myclass")   #前置条件根据其escope的作用域的级别可放在测试用例类的前面或每个测试用例的前面
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("mysetup")
class TestLogin:

    # def setUp(self) -> None:
    #     #打开浏览器
    #     self.driver = webdriver.Chrome()
    #     #窗口最大化
    #     self.driver.maximize_window()
    #     #访问登录页面
    #     self.driver.get(CD.login_url)
    #     self.lp = LoginPage(self.driver)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()
    # @pytest.mark.usefixtures("setup")  #如果是单个用例执行前置条件就写在用例前面，如过类里面的所有用例需执行就写在类前面
    @pytest.mark.smoke
    def test_success_login(self,setup):
        logging.info("登录功能 - 正常场景用例：输入正确的用户名登录成功")
        #输入用户名登录
        setup[1].login(LD.success_data["username"],LD.success_data["passwd"])
        time.sleep(2)
        #url发生改变
        assert LD.success_data["check_url"] == setup[0].current_url
        #登录的用户是否存在
        assert  HomePage(setup[0]).user_is_existed() is True

    def test_no_login(self,setup):
        logging.info("登录功能 - 异常场景用例：输入不存在用户名登录失败")
        # 输入用户名登录
        setup[1].login(LD.no_exit_datas["username"], LD.no_exit_datas["passwd"])
        assert  setup[1].no_exit_login() == LD.no_exit_datas["check"]

    def test_error_passwd_login(self,setup):
        logging.info("登录功能 - 异常场景用例：输入错误的用户密码登录失败")
        setup[1].login(LD.passwd_error["username"], LD.passwd_error["passwd"])
        assert  setup[1].no_exit_login(), LD.passwd_error["check"]

    # @ddt.data(*LD.wrong_datas)
    @pytest.mark.parametrize("case",LD.wrong_datas)
    # @pytest.mark.parametrize("user,passwd,check",LD.wrong_datas)  #这是pytest的DDT的第二种方法
    def test_login_failed_by_wrong_datas(self,case,setup):
        # 步骤
        logging.info("登录功能 - 异常场景用例：不输入用户名或者密码登录失败")
        # 1、登陆页面 - 登陆操作
        setup[1].login(case["username"],case["passwd"])
        # setup[1].login(["username"], passwd["passwd"])   #对应上面的第二种方法
        # 断言
        assert  setup[1].get_error_msg_from_login_form() == case["check"]

