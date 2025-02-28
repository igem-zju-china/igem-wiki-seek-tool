#依赖的库：pandas, requests, BeautifulSoup, openai（直接本地pip就行）
import pandas as pd
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import time
from tenacity import retry, stop_after_attempt, wait_exponential
from config import *

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key=OPENAI_CONFIG["api_key"],
    base_url=OPENAI_CONFIG["base_url"]
)

#iGEM官网上的teams list，这里我保存成csv格式了，下载之后修改好路径就能直接用
#########################################################1
df = pd.read_csv(FILE_PATHS["teams_file"])
#########################################################1

# 读取数据
original_count = len(df)

# 应用筛选条件
for key, value in FILTER_CONFIG.items():
    if value is not None:
        if key == "year":
            df = df[df['wiki'].astype(str).str.contains(str(value))]
        elif isinstance(value, list):
            # 对于列表值进行多值匹配
            df = df[df[key].isin(value)]
        else:
            # 对于单个值进行精确匹配
            df = df[df[key] == value]

filtered_count = len(df)

filtered_count = len(df)

# 输出筛选结果
if filtered_count == 0:
    print("⚠️ 警告：没有找到符合条件的队伍！请检查筛选条件。")
    print("\n筛选条件：")
    for key, value in FILTER_CONFIG.items():
        if value is not None:
            print(f"- {key}: {value}")
    exit()
else:
    print(f"✅ 成功找到 {filtered_count} 支符合条件的队伍（原始数据共 {original_count} 支队伍）")
    print("\n使用的筛选条件：")
    for key, value in FILTER_CONFIG.items():
        if value is not None:
            print(f"- {key}: {value}")
    print("\n开始处理队伍信息...\n")

# 获取筛选后的 wiki URLs
filtered_urls = df['wiki'].tolist()
result_df = pd.DataFrame(columns=["url", "content"])
#########################################################2
output_path = FILE_PATHS["output_file"]
#########################################################2

# 添加重试装饰器
@retry(
    stop=stop_after_attempt(RETRY_CONFIG["max_attempts"]),
    wait=wait_exponential(multiplier=1, min=RETRY_CONFIG["min_wait"], max=RETRY_CONFIG["max_wait"])
)
def get_openai_response(prompt):
    chat_response = client.chat.completions.create(
        model=OPENAI_CONFIG["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=OPENAI_CONFIG["temperature"],
    )
    return chat_response.choices[0].message.content

for url in filtered_urls:
    if url.endswith("/"):
        modified_url = url + "description"
    else:
        modified_url = url + "/description"
        
    print(f"正在处理: {modified_url}")
    try:
        response = requests.get(modified_url, timeout=SCRAPING_CONFIG["request_timeout"])
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            for tag in soup(["script", "style"]):
                tag.extract()
            text = soup.get_text(separator=" ", strip=True)
            if len(text) > SCRAPING_CONFIG["max_text_length"]:
                text = text[:SCRAPING_CONFIG["max_text_length"]]

            # 使用配置的提示词模板
            prompt = PROMPT_TEMPLATE.format(
                year=FILTER_CONFIG["year"],
                text=text
            )

            try:
                answer = get_openai_response(prompt)
                new_row = pd.DataFrame([{"url": modified_url, "content": answer}])
            except Exception as e:
                print(f"OpenAI API 调用失败: {e}")
                new_row = pd.DataFrame([{"url": modified_url, "content": f"OpenAI error: {e}"}])
        else:
            new_row = pd.DataFrame([{"url": modified_url, "content": f"请求失败: {response.status_code}"}])
    except Exception as e:
        new_row = pd.DataFrame([{"url": modified_url, "content": f"错误: {e}"}])
    
    # 保存结果
    result_df = pd.concat([result_df, new_row], ignore_index=True)
    result_df.to_csv(output_path, index=False)
    print(f"已保存结果：{modified_url}")
    
    time.sleep(SCRAPING_CONFIG["sleep_time"])

# 更新最终输出信息
print(f"\n✨ 处理完成！")
print(f"- 共处理 {filtered_count} 支队伍")
print(f"- 结果已保存至：{FILE_PATHS['output_file']}")
