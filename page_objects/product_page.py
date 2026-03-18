import allure
from page_objects.base_page import BasePage

class ProductPage(BasePage):
    # 商品列表页定位器
    PRODUCT_TITLE = ".title"
    ADD_TO_CART_BUTTON = "#add-to-cart-sauce-labs-backpack" # 特定商品
    CART_BADGE = ".shopping_cart_badge" # 购物车角标
    CART_BUTTON = ".shopping_cart_link" # 购物车图标

    # 购物车页面定位器
    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"

    # 结算页定位器
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"

    @allure.step("获取页面标题")
    def get_page_title(self) -> str:
        return self.get_text(self.PRODUCT_TITLE)
    
    @allure.step("添加商品到购物车")
    def add_to_cart(self):
        """添加特定商品到购物车"""
        self.click(self.ADD_TO_CART_BUTTON)
        return self
    
    @allure.step("验证购物车角标")
    def verify_cart_badge(self, expected_count: str = "1") -> bool:
        """验证购物车角标数量"""
        actual_count = self.get_text(self.CART_BADGE)
        assert actual_count == expected_count, f"期望{expected_count}, 实际{actual_count}"
        return True
    
    @allure.step("进入购物车页面")
    def go_to_cart(self):
        """点击购物车图标"""
        self.click(self.CART_BUTTON)
        return CartPage(self.page)
    
class CartPage(BasePage):
    """购物车页面"""

    @allure.step("验证商品在购物车中")
    def verify_item_in_cart(self, item_name: str = "Sauce Labs Backpack") -> bool:
        """验证指定商品在购物车列表中"""
        items = self.page.locator(".cart_item").all()
        for item in items:
            if item_name in item.text_content():
                return True
        raise AssertionError(f"商品 {item_name} 不在购物车中")
    
    @allure.step("点击结算按钮")
    def checkout(self):
        """进入结算流程"""
        self.click("#checkout")
        return CheckoutPage(self.page)

class CheckoutPage(BasePage):
    """结算信息页面"""

    @allure.step("填写结算信息")
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """填写收货信息"""
        self.fill("#first-name", first_name)
        self.fill("#last-name", last_name)
        self.fill("#postal-code", postal_code)
        self.click("#continue")
        return CheckoutOverviewPage(self.page)
    
class CheckoutOverviewPage(BasePage):
    """结算确认页面"""

    @allure.step("完成购买")
    def finish_order(self):
        """完成订单"""
        self.click("#finish")
        return OrderCompletePage(self.page)
    
class OrderCompletePage(BasePage):
    """订单完成页面"""

    @allure.step("验证订单完成")
    def verify_order_complete(self) -> bool:
        """验证是否显示完成标题"""
        header = self.get_text(".complete-header")
        assert "Thank you" in header, f"订单为完成，标题：{header}"
        return True