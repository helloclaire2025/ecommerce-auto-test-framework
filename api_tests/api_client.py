import requests
import allure
from config.config_loader import load_config
from common.assert_util import APIAssertions

class APIClient:
    """API 请求封装类"""

    def __init__(self):
        self.config = load_config()
        self.base_url = self.config['api']['base_url']
        self.timeout = self.config['api']['timeout']
        self.headers = self.config['api'].get('headers', {})
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.assertions = APIAssertions()

    @allure.step("GET 请求: {url}")
    def get(self, url, params=None):
        """发送 GET 请求"""
        full_url = self.base_url + url
        with allure.step(f"请求 URL: {full_url}"):
            response = self.session.get(
                full_url,
                params=params,
                timeout=self.timeout
            )
        self._log_response(response)
        return response
    
    @allure.step("POST 请求: {url}")
    def post(self, url, json=None, data=None):
        """发送 POST 请求"""
        full_url = self.base_url + url
        with allure.step(f"请求 URL: {full_url}"):
            response = self.session.post(
                full_url,
                json=json,
                data=data,
                timeout=self.timeout
            )
        self._log_response(response)
        return response
    
    @allure.step("PUT 请求: {url}")
    def put(self, url, json=None):
        """发送PUT 请求"""
        full_url = self.base_url + url
        with allure.step(f"请求 URL: {full_url}"):
            response = self.session.put(
                full_url,
                json=json,
                timeout=self.timeout
            )
        self._log_response(response)
        return response
    
    @allure.step("DELETE 请求： {url}")
    def delete(self, url):
        """发送 DELETE 请求"""
        full_url = self.base_url + url
        with allure.step(f"请求 URL： {full_url}"):
            response = self.session.delete(
                full_url,
                timeout=self.timeout
            )
        self._log_response(response)
        return response
    
    def _log_response(self, response):
        """记录响应信息到 Allure 报告"""
        allure.attach(
            f"状态码: {response.status_code}",
            name="响应状态",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            response.text,
            name="响应内容",
            attachment_type=allure.attachment_type.JSON
        )

# 单例模式，全局使用
api_client = APIClient()