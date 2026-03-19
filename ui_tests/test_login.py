import allure
import pytest
import sys
import os
from config.config_loader import load_config  # 假设你写了这个加载函数
from page_objects.login_page import LoginPage

# 确保能导入 config 模块
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

@allure.feature("用户模块")
@allure.story("登录功能")
def test_login_success(browser_context):
    # 1. 获取页面对象
    page = browser_context
    
    # 2. 加载配置数据
    config = load_config() 
    username = config['login']['username']
    password = config['login']['password']

    # 3. 创建登录页面对象并执行登录
    login_page = LoginPage(page)
    login_page.login(username, password)

    # 4. 断言
    with allure.step("验证登录成功"):
        # 断言 URL 是否包含 inventory
        assert "inventory" in page.url
        
    # 5. 添加附件证据
    allure.attach(
        "登录成功，已跳转到商品页面",  # 第一个参数是内容
        name="登录结果",                # name 参数是附件名称
        attachment_type=allure.attachment_type.TEXT  # 附件类型
    )
     # 6. 可选：添加截图证据
    allure.attach(
        page.screenshot(),
        name="登录后页面截图",
        attachment_type=allure.attachment_type.PNG
    )