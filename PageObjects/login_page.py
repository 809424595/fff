#_*_conding:utf-8_*_
#@Time    :2020/2/1017:43
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com
from PageLocators.login_page_locs import LoginPageLocs as loc
from Common.basepage import BasePage


class LoginPage(BasePage):
    # 登录行为
    def login(self,username,password):
        #等待
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.login_button))
        #输入用户名和密码点击登录
        # self.driver.find_element(*loc.username_input).send_keys(username)
        # self.driver.find_element(*loc.password_input).send_keys(password)
        # self.driver.find_element(*loc.login_button).click()
        self.input_text(loc.username_input,username,"登陆页面_用户名输入")
        self.input_text(loc.password_input,password,"登陆页面_密码输入")
        self.click_element(loc.login_button,"登陆页面_点击登陆按钮")

    #获取无效用户登录 表单区域的 错误提示信息
    def no_exit_login(self):
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.no_exit_form))
        # return self.driver.find_element(*loc.no_exit_form).text
        return self.get_element_text(loc.no_exit_form,"登陆页面_表单区域错误提示")

    # 获取 表单区域的 错误提示信息
    def get_error_msg_from_login_form(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(loc.error_from_login_form))
        # return self.driver.find_element(*loc.error_from_login_form).text
        return self.get_element_text(loc.error_from_login_form,"登陆页面_页面中间错误提示")





