import pytest
import allure

@pytest.fixture(scope="session")
def api_base_url():
    """API 基础 URL"""
    from config.config_loader import load_config
    config = load_config()
    return config['api']['base_url']