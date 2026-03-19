import allure
import pytest
import yaml
import os
from api_tests.api_client import api_client

# 加载测试数据
def load_test_data():
    """加载商品测试数据"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(
        os.path.dirname(current_dir),
        'config', 'data', 'products.yaml'
    )
    with open(data_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

test_data = load_test_data()

@allure.feature("商品 API")
@allure.story("商品查询")
class TestProductAPI:
    """商品接口测试"""

    @allure.title("获取所有商品列表")
    def test_get_all_products(self):
        """测试获取商品列表接口"""
        response = api_client.get("/products")

        # 使用封装的断言方法
        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_content_type(response)
        api_client.assertions.assert_json_list_length(response, min_length=1)
        api_client.assertions.assert_response_time(response, max_time=3000)

    
    @allure.title("获取单个商品详情 - 参数化测试")
    @pytest.mark.parametrize("product", test_data.get('products', []))
    def test_get_product_by_id(self, product):
        """测试获取单个商品接口"""
        response = api_client.get(f"/products/{product['id']}")

        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_field_value(response, "id", product['id'])
        api_client.assertions.assert_json_field_value(response, "price", product['price'])


    @allure.title("边界测试 - 不存在的商品")
    @pytest.mark.parametrize("edge_case", test_data.get('edge_cases', []))
    def test_get_nonexistent_product(self, edge_case):
        """
        边界测试：无效商品 ID
        """
        response = api_client.get(f"/products/{edge_case['id']}")

        # 预期返回404 或空数据
        api_client.assertions.assert_status_code(response, edge_case['expected_status'])

        # 记录测试描述到报告
        allure.attach(
            edge_case['description'],
            name="测试场景",
            attachment_type=allure.attachment_type.TEXT
        )
        # 可选：记录响应内容到报告
        allure.attach(
            f"响应内容：{response.text[:200]}",
            name="响应内容",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title("获取商品分类列表")
    def test_get_categories(self):
        """测试获取商品分类接口"""
        response = api_client.get("/products/categories")

        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_list_length(response, min_length=1)


    @allure.title("按分类查询商品 - 参数化测试")
    @pytest.mark.parametrize("category", test_data.get('categories', []))
    def test_get_products_by_category(self, category):
        """参数化测试：多个商品分类"""
        response = api_client.get(f"/products/category/{category}")

        api_client.assertions.assert_status_code(response, 200)
        api_client.assertions.assert_json_list_length(response, min_length=1)

        # 验证所有商品都属于该分类
        products = response.json()
        for product in products:
            assert product['category'] == category, \
                f"商品分类不匹配: 期望 {category}, 实际 {product['category']}"