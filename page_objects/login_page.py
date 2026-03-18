import allure
from page_objects.base_page import BasePage
from page_objects.product_page import ProductPage

class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = ".error-message-container"

    @allure.step("登录操作")
    def login(self, username: str, password: str):
        """执行登录流程"""
        self.open("")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return ProductPage(self.page)
    
    def get_error_massage(self) -> str:
        """获取错误提示信息"""
        return self.get_text(self.ERROR_MESSAGE)
    