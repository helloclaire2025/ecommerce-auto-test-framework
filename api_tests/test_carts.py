# api_tests/test_orders.py
import allure
import pytest
from api_tests.api_client import api_client

@allure.feature("购物车 API")
@allure.story("购物车管理")
class TestCartAPI:
    """购物车接口测试（替代订单 API）"""
    
    @allure.title("获取所有购物车列表")
    def test_get_all_carts(self):
        """测试获取所有购物车接口"""
        response = api_client.get("/carts")
        
        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_list_length(response, min_length=1)
    
    @allure.title("获取单个购物车详情")
    def test_get_cart_by_id(self):
        """测试获取单个购物车接口"""
        cart_id = 1
        response = api_client.get(f"/carts/{cart_id}")
        
        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_field_value(response, "id", cart_id)
        api_client.assertions.assert_json_has_field(response, "userId")
        api_client.assertions.assert_json_has_field(response, "products")
    
    @allure.title("获取用户的购物车")
    def test_get_user_carts(self):
        """测试获取用户购物车接口"""
        user_id = 1
        response = api_client.get(f"/carts/user/{user_id}")
        
        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_list_length(response, min_length=0)
    
    @allure.title("创建购物车 - 模拟测试")
    def test_create_cart(self):
        """
        测试创建购物车接口
        注意：FakeStoreAPI 的 POST 接口是模拟的
        """
        cart_data = {
            "userId": 1,
            "date": "2025-01-15T10:30:00.000Z",
            "products": [
                {"productId": 1, "quantity": 2},
                {"productId": 5, "quantity": 1}
            ]
        }
        
        response = api_client.post("/carts", json=cart_data)
        
        # 验证创建成功
        api_client.assertions.assert_status_code(response, 201)
        api_client.assertions.assert_json_has_field(response, "id")
        
        # 验证返回数据
        cart = response.json()
        assert cart["userId"] == cart_data["userId"]
        assert len(cart["products"]) == len(cart_data["products"])
    
    @allure.title("更新购物车 - 模拟测试")
    def test_update_cart(self):
        """
        测试更新购物车接口
        注意：FakeStoreAPI 的 PUT 接口是模拟的
        """
        cart_id = 1
        cart_data = {
            "userId": 1,
            "date": "2025-01-15T10:30:00.000Z",
            "products": [
                {"productId": 3, "quantity": 5}
            ]
        }
        
        response = api_client.put(f"/carts/{cart_id}", json=cart_data)
        
        # 验证更新成功
        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_field_value(response, "id", cart_id)
    
    @allure.title("删除购物车 - 模拟测试")
    def test_delete_cart(self):
        """
        测试删除购物车接口
        注意：FakeStoreAPI 的 DELETE 接口是模拟的
        """
        cart_id = 1
        response = api_client.delete(f"/carts/{cart_id}")
        
        # 验证删除成功
        api_client.assertions.assert_status_code(response, 200)
        
        # 验证返回删除确认
        result = response.json()
        assert "message" in result or "id" in result