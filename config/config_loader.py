import yaml
import os

def load_config():
    """
    加载 config.yaml 配置文件
    """
    # 1. 获取当前文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 2. 拼接出 config.yaml 的完整路径
    config_path = os.path.join(current_dir, 'config.yaml')
    
    # 3. 打开并读取 YAML 文件
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    return config

# 方便调试：直接运行此文件看能否读出数据
if __name__ == '__main__':
    print(load_config())