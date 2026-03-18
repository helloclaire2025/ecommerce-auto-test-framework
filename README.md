# 🛒 E-Commerce Hybrid Automation Framework

> 基于 Playwright + Pytest 的电商混合自动化测试框架

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-green.svg)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-red.svg)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-2.24+-orange.svg)](https://allurereport.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 项目简介

本项目是一个**电商混合自动化测试框架**，集成了 **UI 自动化** 和 **API 自动化** 测试能力。采用 **POM（Page Object Model）设计模式**，支持 **Allure 测试报告**、**失败自动截图**、**CI/CD 流水线** 等企业级功能。

### 🎯 核心特性

- ✅ **POM 设计模式**：页面对象封装，代码易维护
- ✅ **UI + API 混合测试**：覆盖前端和后端测试场景
- ✅ **Allure 报告**：可视化测试报告，支持截图附件
- ✅ **失败自动截图**：测试失败自动留存证据
- ✅ **数据驱动**：配置文件与代码分离，支持多环境
- ✅ **CI/CD 集成**：GitHub Actions 自动运行测试

---

## 🛠️ 技术栈

| 类别 | 技术 | 版本 |
|-----|------|------|
| **编程语言** | Python | 3.9+ |
| **测试框架** | Pytest | 7.0+ |
| **UI 自动化** | Playwright | 1.40+ |
| **API 测试** | Requests | 2.31+ |
| **测试报告** | Allure | 2.24+ |
| **配置管理** | PyYAML | 6.0+ |
| **CI/CD** | GitHub Actions | - |

---


---

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/your-username/ecommerce-auto-test-framework.git
cd ecommerce-auto-test-framework

# 创建虚拟环境 (推荐)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 安装依赖
pip install -r requirements.txt

# 安装 Playwright 浏览器
playwright install
```

### 运行测试

```bash

# 运行所有 UI 测试
pytest ui_tests/ -v --alluredir=./reports

# 运行特定测试
pytest ui_tests/test_login.py -v

# 运行 API 测试
pytest api_tests/ -v

# 生成并查看报告
allure serve ./reports
```

### 生成静态报告

```bash
# 生成静态 HTML 报告
allure generate ./reports -o ./html-report --clean

# 打开报告 (需要 HTTP 服务器)
# 方法 1: 使用 Python 内置服务器
cd html-report && python -m http.server 8080
# 浏览器访问 http://localhost:8080
```
