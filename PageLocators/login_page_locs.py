#_*_conding:utf-8_*_
#@Time    :2020/2/1114:54
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
from selenium.webdriver.common.by import By

class LoginPageLocs:
    # 用户名输入框
    username_input = (By.XPATH, '//input[@name="phone"]')
    # 用户密码输入框
    password_input = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_button = (By.TAG_NAME, 'button')
    # 输入不存在的用户名点击登录的提示信息
    no_exit_form = (By.XPATH, '//div[@class="layui-layer-content"]')

    error_from_login_form = (By.XPATH, '//div[@class="form-error-info"]')