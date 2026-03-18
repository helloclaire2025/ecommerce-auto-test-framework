# ui_tests/test_shopping.py
import allure
import pytest
from config.config_loader import load_config
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage

# 确保能导入 config 模块
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

@allure.feature("购物流程")
@allure.story("完整下单流程")
class TestShoppingFlow:
    """
    ⚠️ 注意：类方法不要写 self 参数！
    Pytest 不会自动注入 self
    """
    
    @pytest.fixture(autouse=True)
    def setup_method(self, browser_context):
        """
        每个测试前自动执行
        ⚠️ 注意：fixture 方法可以有 self，但测试方法不能有
        """
        self.page = browser_context
        self.config = load_config()

    @allure.title("完整购物流程测试")
    def test_complete_shopping_flow(self):
        """
        ⚠️ 关键：测试方法不要 self 参数！
        但可以通过 self.xxx 访问 setup_method 中设置的属性
        """
        login_page = LoginPage(self.page)
        product_page = login_page.login(
            self.config['login']['username'],
            self.config['login']['password']
        )
        
        assert product_page.get_page_title() == "Products"
        product_page.add_to_cart()
        product_page.verify_cart_badge("1")
        
        cart_page = product_page.go_to_cart()
        cart_page.verify_item_in_cart("Sauce Labs Backpack")
        
        checkout_page = cart_page.checkout()
        overview_page = checkout_page.fill_checkout_info(
            first_name="Test",
            last_name="User",
            postal_code="12345"
        )
        
        complete_page = overview_page.finish_order()
        assert complete_page.verify_order_complete() == True

    @allure.title("只加入购物车不结算")
    def test_add_to_cart_only(self):
        """测试场景：只验证加入购物车功能"""
        login_page = LoginPage(self.page)
        product_page = login_page.login(
            self.config['login']['username'],
            self.config['login']['password']
        )
        
        product_page.add_to_cart()
        product_page.verify_cart_badge("1")
        
        cart_page = product_page.go_to_cart()
        assert cart_page.verify_item_in_cart("Sauce Labs Backpack")