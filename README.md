# WikiSeek - iGEM Wiki 智能分析工具

## 项目简介

WikiSeek 是一个专门为 iGEM 比赛设计的 Wiki 页面智能分析工具。它能自动抓取并分析各参赛队伍的项目描述，利用 ChatGPT 生成结构化的项目总结，帮助参赛者快速了解其他队伍的项目内容。

## 主要功能

- 🔍 自动筛选特定年份的参赛队伍 Wiki
- 📑 智能提取 Description 页面的关键内容
- 🤖 利用 ChatGPT 生成项目要点分析
- 💾 自动保存分析结果，支持断点续传
- 🛡️ 内置重试机制，提高运行稳定性
- ⚙️ 灵活的配置系统，支持自定义分析

## 快速开始

### 1. 环境配置

#### 使用 venv（推荐）
```bash
# 在 Windows 上
python -m venv igem-env
.\igem-env\Scripts\activate

# 在 macOS/Linux 上
python3 -m venv igem-env
source igem-env/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### 使用 Conda（可选）
```bash
# 创建并激活虚拟环境
conda create -n igem python=3.11
conda activate igem

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置文件设置

1. 准备 `teams.csv` 文件（包含参赛队伍 Wiki 链接）
2. 在 `config.py` 中设置：
   ```python
   # OpenAI API 配置
   OPENAI_CONFIG = {
       "api_key": "your-api-key",
       "base_url": "your-api-base-url",
       "model": "gpt-3.5-turbo",
       "temperature": 0.61
   }

   # 设置目标年份
   SCRAPING_CONFIG = {
       "target_year": "2024",  # 修改为目标年份
       ...
   }

   # 自定义分析提示词
   PROMPT_TEMPLATE = """
   您的自定义提示词...
   """
   ```

### 3. 运行程序

```bash
python main.py
```

## 配置说明

### 主要配置项

1. **OpenAI API 配置**
   - API 密钥
   - API 基础URL
   - 模型选择
   - 温度参数

2. **文件路径配置**
   - 输入文件路径
   - 输出文件路径

3. **爬取配置**
   - 目标年份
   - 请求超时时间
   - 最大文本长度
   - 请求间隔时间

4. **重试配置**
   - 最大重试次数
   - 等待时间范围

5. **提示词模板**
   - 完全自定义的分析提示词
   - 支持年份和文本变量

## 输出示例

程序会生成 `output.csv`，包含以下信息：
- Wiki URL
- 项目名称
- 问题背景
- 解决方案
- 其他关键信息

## 技术特点

- 🚀 自动化的数据获取和分析流程
- 🔄 内置指数退避重试机制
- 💡 智能文本分析和结构化输出
- ⚡ 实时保存进度，支持断点恢复
- 🔧 模块化配置系统
- 📝 自定义分析模板

## 注意事项

1. **API 使用**
   - 需要有效的 OpenAI API 密钥
   - 建议使用代理服务（如 vveai）以降低成本

2. **运行限制**
   - 请求间隔和重试次数可在配置文件中调整
   - 文本长度限制可自定义

3. **环境要求**
   - Python 3.11 或更高版本
   - 推荐使用虚拟环境

## 常见问题解决

1. OpenAI API 版本问题：
   ```bash
   pip install openai==0.28.0
   ```

2. 代理连接问题：
   ```bash
   pip install httpx[socks]
   ```

3. 配置文件问题：
   - 确保所有配置项都已正确设置
   - 检查文件路径是否正确
   - 验证 API 密钥格式

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目！

## 许可证

本项目采用 MIT 许可证。
