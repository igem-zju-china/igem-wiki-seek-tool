# OpenAI API 配置
OPENAI_CONFIG = {
    "api_key": "sk-TNiVDch5gjn5HV6W8332189f2fCf41849cA4B0880a7265A4",
    "base_url": "https://api.vveai.com/v1",
    "model": "gpt-3.5-turbo",
    "temperature": 0.61
}

# 文件路径配置
FILE_PATHS = {
    "teams_file": "./teams.csv",
    "output_file": "./output.csv"
}

# 爬取配置
SCRAPING_CONFIG = {
    "target_year": "2024",  # 目标年份
    "request_timeout": 10,  # 请求超时时间（秒）
    "max_text_length": 7000,  # 最大文本长度
    "sleep_time": 1.00,  # 请求间隔时间（秒）
}

# 重试配置
RETRY_CONFIG = {
    "max_attempts": 3,  # 最大重试次数
    "min_wait": 4,  # 最小等待时间
    "max_wait": 10  # 最大等待时间
}

# 自定义提示词模板
PROMPT_TEMPLATE = """请分析以下从{year}年iGEM参赛队伍的wiki网页中提取的文本，
分析概述出该iGEM比赛参赛队伍的主要项目内容，包括：
1. 项目名称
2. 问题背景
3. 解决方案
4. 其它重要内容

要求：
- 结合文本内容并分点给出
- 保持简洁明了
- 突出创新点

以下是需要分析的文本：

{text}
"""
