# ui_tests/conftest.py
import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_context(request):
    """
    浏览器 Fixture
    request 是 pytest 内置 fixture，自动注入
    """
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        
        # 创建上下文
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )
        
        # 创建页面
        page = context.new_page()
        
        # 返回 page 对象给测试用例
        yield page
        
        # --- 后置操作：测试结束后执行 ---
        # 检查测试是否失败
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            try:
                screenshot = page.screenshot()
                allure.attach(
                    screenshot,
                    name=f"测试失败截图：{request.node.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"截图失败：{e}")
        
        # 清理资源
        context.close()
        browser.close()


# 钩子函数：记录测试结果状态（用于失败截图）
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    这个钩子函数会在测试运行前后被调用
    用于记录测试结果，供 fixture 中的 request.node.rep_call 使用
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)