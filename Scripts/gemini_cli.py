import os
import sys
from google import genai
import time

# --- 配置区 ---
API_KEY = "AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E"
PROXY_URL = "http://127.0.0.1:7890"

os.environ["HTTP_PROXY"] = PROXY_URL
os.environ["HTTPS_PROXY"] = PROXY_URL

client = genai.Client(api_key=API_KEY)

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

def main():
    if len(sys.argv) > 1:
        # 如果有命令行参数，直接处理
        user_input = ' '.join(sys.argv[1:])
    else:
        # 否则进入交互模式
        print("🤖 Gemini CLI - 输入 'quit' 退出")
        while True:
            try:
                user_input = input("你: ")
                if user_input.lower() in ['quit', 'exit', '退出']:
                    break
            except KeyboardInterrupt:
                print("\n退出。")
                break

    if user_input:
        try:
            response = retry_on_429(client.models.generate_content,
                model="gemini-2.0-flash",
                contents=user_input
            )
            print(f"Gemini: {response.text}")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()