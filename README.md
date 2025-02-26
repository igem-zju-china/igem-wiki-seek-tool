# WikiSeek -- iGEM Wiki 爬虫与批量分析程序

## 〇、概述

本项目实现了一个基于 Anaconda 环境的 Jupyter Notebook 的 Python 分析程序，主要功能包括：

- 从 iGEM 官方提供的参赛队伍 CSV 表格中读取各个队伍的 wiki 链接；
- 筛选出包含特定年份（如 "2024"）的 description 页面链接；
- 爬取每个修改后的页面内容，并利用 BeautifulSoup 提取页面纯文本；
- 调用 OpenAI ChatGPT 接口（本示例中使用的是 GPT-3.5-turbo）根据预设的 prompt 对提取的文本进行分析，生成关于项目名称、问题背景、解决方案等主要内容及关键信息的解析结果，并分点展示；
- 将每个链接及其对应的分析结果保存到新的 CSV 文件中。

### 缺点：
- 爬取方式较为简单，未使用异步优化，效率较低；
- 依赖 OpenAI API，需要外部 API 支持（但调用次数一般不受限）；
- 缺乏数据清洗和后处理，ChatGPT 生成的内容仍需要进一步人工筛选。

---

## 一、依赖库

本程序依赖以下 Python 库：

- [pandas](https://pandas.pydata.org/)
- [requests](https://docs.python-requests.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [openai](https://github.com/openai/openai-python)  
- time（Python 内置模块）

### 安装依赖库：
```bash
pip install pandas requests beautifulsoup4 openai
```
> **注意**：如果在使用 `openai` 库时遇到版本过高的问题，根据错误提示可安装特定版本（一般需要降级至 1.0 以下）。例如：
> ```bash
> pip install openai==0.28
> ```

---

## 二、使用说明

### 0. 前置安装
安装所有依赖库，并打开 Jupyter Notebook，在其中打开 `main.ipynb`。

### 1. 获取完整的参赛队伍列表
从文件夹中下载 `teams.csv` 并保存至本地，并将文件路径在代码中正确设置（推荐使用绝对路径）：
```python
df = pd.read_csv("your_file_path\\teams.csv")
```

### 2. 筛选目标链接
程序默认筛选 `wiki` 列中包含 `"2024"` 的链接，如需处理其他年份，可直接修改筛选条件。

### 3. 设置 API 密钥及端点
替换代码中的 `openai.api_key` 为你自己的 API 密钥（本示例使用的是在 [vveai](https://api.vveai.com) 获得的免费额度）。
确保 `openai.api_base` 正确设置到所使用的 API 服务端点。

### 4. 运行程序
在 Jupyter Notebook 中运行代码，程序会依次爬取每个目标链接，调用 ChatGPT 接口进行内容解析，并将结果写入指定的输出 CSV 文件：
```python
result_df.to_csv("your_file_path\\output.csv", index=False)
```

### 5. 查看结果
程序执行完毕后，可在指定路径找到 `output.csv` 文件，其中包含每个处理后的链接及其对应的 ChatGPT 分析内容。

---

## 三、注意事项

1. **请求速率控制**  
   为防止请求过快被目标网站封禁，程序中每次请求后暂停 `1.00` 秒。

2. **文本长度限制**  
   若页面文本过长，程序会截取前 `7000` 个字符进行分析，可根据需要调整该数值。

3. **API 调用**  
   调用 ChatGPT API 会消耗免费额度或产生费用，请根据自身需求合理使用。

4. **环境配置**  
   若遇到 `openai` 库版本不兼容等问题，请按照错误提示重新安装符合要求的版本。
