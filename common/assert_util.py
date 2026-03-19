import allure
import json

class APIAssertions:
    """API 响应断言封装类"""

    @staticmethod
    @allure.step("断言状态码")
    def assert_status_code(response, expected_code: int):
        """断言HTTP 状态码"""
        actual_code = response.status_code
        assert actual_code == expected_code, \
            f"状态码不匹配: 期望 {expected_code}, 实际 {actual_code}"
        
    @staticmethod
    @allure.step("断言响应时间")
    def assert_response_time(response, max_time: int = 1000):
        """断言响应时间（毫秒）"""
        actual_time = response.elapsed.total_seconds() * 1000
        assert actual_time < max_time, \
            f"响应时间超时： 期望 < {max_time}ms, 实际 {actual_time:.2f}ms"
        

    @staticmethod
    @allure.step("断言JSON字段存在")
    def assert_json_has_field(response, field: str):
        """断言响应JSON 包含指定字段"""
        json_data = response.json()
        assert field in json_data, \
            f"响应缺少字段: {field}"
        
    @staticmethod
    @allure.step("断言JSON字段值")
    def assert_json_field_value(response, field: str, expected_value):
        """断言响应JSON 字段值匹配"""
        json_data = response.json()
        actual_value = json_data.get(field)
        assert actual_value == expected_value, \
            f"字段值不匹配: {field} 期望 {expected_value}, 实际 {actual_value}"
        
    @staticmethod
    @allure.step("断言JSON列表长度")
    def assert_json_list_length(response, min_length: int = 0):
        """断言响应JSON 列表长度"""
        json_data = response.json()
        assert isinstance(json_data, list), "相应不是列表"
        assert len(json_data) >= min_length, \
            f"列表长度不足，期望 >={min_length}, 实际 {len(json_data)}"

    @staticmethod
    @allure.step("断言响应内容类型")
    def assert_content_type(response, expected_type: str = "application/json"):
        """断言响应 Content-Type """
        actual_type = response.headers.get("Content-Type", "")
        assert expected_type in actual_type, \
            f"Content-Type 不匹配: 期望 {expected_type}, 实际 {actual_type}"

    @staticmethod
    @allure.step("断言返回空数据")
    def assert_empty_response(response):
        """断言返回空数组或空对象"""
        json_data = response.json()
        assert json_data in ([], {}, None), \
            f"期望空数据，实际返回: {json_data}"