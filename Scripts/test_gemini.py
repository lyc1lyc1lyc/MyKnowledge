import google.generativeai as genai
import os
import time

# 1. 设置代理（根据你的 FlClash 端口）
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# 2. 配置 Key
genai.configure(api_key="AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E")

def retry_on_429(func, *args, **kwargs):
    while True:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "429" in str(e):
                print("⚠️ 遇到429错误，等待60秒后重试... (按Ctrl+C可中断)")
                try:
                    for i in range(60, 0, -1):
                        print(f"倒计时: {i} 秒", end='\r')
                        time.sleep(1)
                    print("继续重试...")
                except KeyboardInterrupt:
                    print("\n重试被用户中断。")
                    raise
            else:
                raise

# 3. 呼叫模型
model = genai.GenerativeModel('gemini-1.5-flash')
response = retry_on_429(model.generate_content, "你好，我是超级个体计划的执行者，请确认连接状态。")

print(response.text)