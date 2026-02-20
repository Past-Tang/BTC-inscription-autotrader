# BTC符文自动交易工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/Playwright-1.0+-green.svg)](https://playwright.dev/)

## 项目状态

**注意：此仓库已不再维护。**

## 项目概述

BTC符文自动交易工具是一个基于Python和Playwright的自动化程序，用于辅助比特币符文(Inscriptions)的交易操作。此工具通过自动化浏览器操作，实现与UniSat钱包和交易平台(如MagicEden)的无缝交互，支持多钱包批量管理和交易自动化。

## 技术栈

- **Python**: 核心编程语言
- **Playwright**: Web自动化测试框架
- **Chrome浏览器**: 运行环境
- **UniSat钱包**: 比特币钱包扩展(v1.3.4)
- **比特币符文(Inscriptions)**: 交易对象

## 特点

- 自动处理UniSat钱包的登录、解锁及签名操作
- 支持多钱包账户管理与切换
- 自动化符文交易流程
- 处理浏览器弹窗和扩展交互
- 支持在MagicEden等平台进行自动化操作

## 安装说明

1. 克隆仓库到本地：
   ```
   git clone https://github.com/username/btc-inscription-autotrader.git
   cd btc-inscription-autotrader
   ```

2. 安装依赖：
   ```
   pip install playwright
   playwright install chromium
   ```

3. 确保UniSat钱包扩展已就绪：
   - 项目包含UniSat Chrome扩展(v1.3.4)
   - 扩展路径配置在代码中已设置为`unisat-chrome-mv3-v1.3.4`目录

## 使用方法

1. 配置钱包信息：
   - 在`Context_Tool.py`文件中更新钱包密码

2. 运行主程序：
   ```
   python Browser_main.py
   ```

3. 程序自动执行流程：
   - 启动Chrome浏览器并加载UniSat扩展
   - 登录钱包并初始化任务列表
   - 访问交易平台(默认为MagicEden的UNCOMMON•GOODS页面)
   - 按照任务列表切换钱包并执行交易操作

## 配置选项

在`Browser_main.py`中可配置以下选项：
- `USER_DATA_DIR`: Chrome用户数据目录路径
- `EXTENSION_PATH`: UniSat钱包扩展路径

钱包密码在`Context_Tool.py`的`Login_Wallet`函数中配置。

## 项目结构

- `Browser_main.py`: 主程序入口，包含浏览器启动和主流程控制
- `Context_Tool.py`: 钱包相关工具函数，包括钱包登录、切换等
- `Page_Tool.py`: 页面交互工具函数
- `unisat-chrome-mv3-v1.3.4/`: UniSat钱包Chrome扩展
- `chrome_user_data/`: Chrome用户数据目录(运行时自动生成)

## 依赖项

- Python 3.6+
- Playwright
- Chrome浏览器
- UniSat钱包扩展(v1.3.4)

## API文档

本项目主要函数:

- `get_extension_id()`: 获取Chrome扩展ID
- `Login_Wallet()`: 登录UniSat钱包并初始化任务列表
- `Next_wallet()`: 切换到指定钱包
- `handle_popup()`: 处理钱包签名等弹窗
- `wait_for_text_to_disappear()`: 等待指定文本从页面消失

## 贡献指南

由于此仓库已不再维护，不接受新的代码贡献。

## 常见问题(FAQ)

### 如何处理钱包解锁失败？
确保在`Context_Tool.py`中设置了正确的钱包密码。

### 支持哪些交易平台？
目前代码示例主要针对MagicEden平台，可以通过修改相应URL和选择器扩展到其他平台。

### 如何添加更多的自动化操作？
可通过扩展`handle_popup`函数或增加新的页面操作函数来实现更多自动化任务。

## 安全注意事项

- 请勿在代码中硬编码敏感信息如钱包密码
- 仅在测试环境或小额交易时使用自动化功能
- 使用前请备份钱包数据

## 许可证

MIT

## 项目维护者

此项目已不再维护。若有疑问，请通过Issue区留言。