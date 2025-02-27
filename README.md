# WikiSeek - iGEM Wiki 智能分析工具

## 项目简介

WikiSeek 是一个专门为 iGEM 比赛设计的 Wiki 页面智能分析工具。它能自动抓取并分析各参赛队伍的项目描述，利用 ChatGPT 生成结构化的项目总结，帮助参赛者快速了解其他队伍的项目内容。

## 主要功能

- 🔍 自动筛选参赛队伍 Wiki
  - 支持年份、地区、国家等多维度筛选
  - 支持单值和多值筛选条件
  - 实时显示筛选结果统计

- 📑 智能提取 Description 页面的关键内容
  - 自动处理页面文本
  - 智能清理无关内容
  - 控制文本长度在合理范围

- 🤖 利用 ChatGPT 生成项目要点分析
  - 自动提取项目名称
  - 分析问题背景
  - 总结解决方案
  - 突出创新要点

- 💾 自动保存分析结果
  - 支持断点续传
  - CSV 格式易于处理
  - 实时保存进度

- 🛡️ 内置重试机制
  - 自动处理网络错误
  - 智能调整重试间隔
  - 提高运行稳定性

- 📊 数据统计功能
  - 显示处理进度
  - 统计筛选结果
  - 展示可用筛选选项

## 安装指南

### 1. 克隆项目

```bash
# 克隆项目
git clone https://github.com/igem-zju-china/igem-wiki-seek-tool.git
cd igem-wiki-seek-tool
```

### 2. 环境配置

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

### 3. 准备数据文件
1. 准备 `teams.csv` 文件（包含参赛队伍 Wiki 链接）
2. 将 `teams.csv` 放在项目根目录下

### 4. 配置设置

1. 在 `config.py` 中设置 API 配置：
   ```python
   OPENAI_CONFIG = {
       "api_key": "your-api-key",
       "base_url": "your-api-base-url",
       "model": "gpt-3.5-turbo",
       "temperature": 0.61
   }
   ```

3. 设置筛选条件：
   ```python
   FILTER_CONFIG = {
       "year": "2024",          # 年份筛选
       "region": ["asia", "europe"],  # 支持多个地区
       "country": ["USA", "FIN"],  # 支持多个国家
       "village": None,         # 赛道筛选
       "kind": None,           # 项目类型筛选
       "section": None,        # 部分筛选
       "is_remote": False      # 是否远程
   }
   ```

### 筛选配置说明

#### 可用的筛选值

1. **Village 类别**:
   - Measurement
   - Manufacturing
   - New Application
   - Environment
   - Diagnostics
   - Foundational Advance
   - Bioremediation
   - Oncology
   - Entrepreneurship
   - Energy
   - Therapeutics
   - Health & Medicine
   - Food & Nutrition
   - Space
   - Information Processing
   - Climate Crisis
   - Agriculture
   - Software Tools
   - Art & Design
   - 等...

2. **Region 地区**:
   - asia
   - europe
   - north-america
   - africa
   - ...

3. **Section 类别**:
   - overgrad
   - undergrad
   - collegiate

#### 基本用法
- 单一值筛选：直接指定值
  ```python
  "village": "Therapeutics"
  ```

- 多值筛选：使用列表
  ```python
  "village": ["Therapeutics", "Diagnostics"]
  ```

- 不进行筛选：使用 None
  ```python
  "village": None
  ```

#### 筛选示例

1. **按特定领域和年份筛选**
   ```python
   FILTER_CONFIG = {
       "year": "2024",
       "village": "Therapeutics",
       "country": None,
       # 其他条件设为 None
   }
   ```

2. **多个领域的非远程团队**
   ```python
   FILTER_CONFIG = {
       "year": "2024",
       "village": ["Therapeutics", "Diagnostics"],
       "is_remote": False,
       # 其他条件设为 None
   }
   ```

3. **特定地区的本科生团队**
   ```python
   FILTER_CONFIG = {
       "year": "2024",
       "region": "asia",
       "section": "undergrad",
       # 其他条件设为 None
   }
   ```

#### 注意事项
1. 筛选值需要完全匹配，注意大小写
2. 某些分类可能随年份变化
3. 建议先用较少的筛选条件测试
4. 如果没有匹配结果，程序会显示可用的选项

#### 运行结果展示
程序运行时会显示：
- 筛选条件统计
- 匹配到的队伍数量
- 处理进度
- 最终结果保存位置

示例输出：
```
✅ 成功找到 50 支符合条件的队伍（原始数据共 300 支队伍）

使用的筛选条件：
- year: 2024
- region: ['asia', 'europe']
- is_remote: False

开始处理队伍信息...
```

### 5. 运行程序

```bash
python main.py
```

## 主要功能

- 🔍 自动筛选参赛队伍 Wiki
  - 支持年份、地区、国家等多维度筛选
  - 支持单值和多值筛选条件
  - 实时显示筛选结果统计

- 📑 智能提取 Description 页面的关键内容
  - 自动处理页面文本
  - 智能清理无关内容
  - 控制文本长度在合理范围

- 🤖 利用 ChatGPT 生成项目要点分析
  - 自动提取项目名称
  - 分析问题背景
  - 总结解决方案
  - 突出创新要点

- 💾 自动保存分析结果
  - 支持断点续传
  - CSV 格式易于处理
  - 实时保存进度

- 🛡️ 内置重试机制
  - 自动处理网络错误
  - 智能调整重试间隔
  - 提高运行稳定性

- 📊 数据统计功能
  - 显示处理进度
  - 统计筛选结果
  - 展示可用筛选选项

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

1. 代理连接问题：
   ```bash
   pip install socksio
   ```

2. 配置文件问题：
   - 确保所有配置项都已正确设置
   - 检查文件路径是否正确
   - 验证 API 密钥格式

3. Excel 打开乱码问题
   - 在 Excel 中打开 `output.csv` 时，可能会遇到乱码问题。可以尝试使用其他文本编辑器（如 Notepad++）打开查看。
   - 或者使用 `Excel`，选择数据来源->从文本/CSV，选择 `output.csv` 文件，选择 `UTF-8` 编码，即可正常显示。
   
## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目！

## 许可证

本项目采用 MIT 许可证。
