import google.generativeai as genai
import os

# 1. 设置代理（根据你的 FlClash 端口）
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# 2. 配置 Key
genai.configure(api_key="AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E")

# 3. 呼叫模型
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("你好，我是超级个体计划的执行者，请确认连接状态。")

print(response.text)