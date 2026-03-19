# api_tests/test_users.py
import allure
import pytest
from api_tests.api_client import api_client

@allure.feature("用户 API")
@allure.story("用户管理")
class TestUserAPI:
    """用户接口测试"""
    
    @allure.title("获取所有用户列表")
    def test_get_all_users(self):
        """测试获取所有用户接口"""
        response = api_client.get("/users")
        
        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_list_length(response, min_length=1)
    
    @allure.title("获取单个用户详情")
    def test_get_user_by_id(self):
        """测试获取单个用户接口"""
        user_id = 1
        response = api_client.get(f"/users/{user_id}")
        
        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_field_value(response, "id", user_id)
        api_client.assertions.assert_json_has_field(response, "username")
        api_client.assertions.assert_json_has_field(response, "email")
    
    @allure.title("查询不存在的用户")
    def test_get_nonexistent_user(self):
        """测试查询不存在的用户"""
        response = api_client.get("/users/99999")
        
        # 预期返回 200
        api_client.assertions.assert_status_code(response, 200)