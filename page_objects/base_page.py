import allure
from playwright.sync_api import Page, TimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.saucedemo.com/"

    @allure.step("打开页面")
    def open(self, url_path: str = ""):
        """打开指定URL 路径"""
        full_url = self.base_url + url_path
        self.page.goto(full_url)
        return self
    
    @allure.step("输入文本： {text}")
    def fill(self, selector: str, text: str):
        """封装输入操作，带错误处理"""
        try:
            self.page.locator(selector).fill(text)
        except Exception as e:
            allure.attach(f"输入失败： {selector}", attachment_type=allure.attachment_type.TEXT)
            raise e
        
    @allure.step("点击元素： {selector}")
    def click(self, selector: str):
        """封装点击操作"""
        try:
            self.page.locator(selector).click()
        except Exception as e:
            allure.attach(f"点击失败： {selector}", attachment_type=allure.attachment_type.TEXT)
            raise e
        
    @allure.step("获取文本内容")
    def get_text(self, selector: str) -> str:
        """获取元素文本"""
        return self.page.locator(selector).text_content()
    
    @allure.step("等待元素可见")
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """等待元素出现"""
        try:
            self.page.locator(selector).wait_for(state="visible", timeout=timeout)
        except TimeoutError:
            allure.attach(self.page.screenshot(), name="等待超时截图", attachment_type=allure.attachment_type.PNG)
            raise TimeoutError(f"元素 {selector} 在 {timeout}ms 内未出现")