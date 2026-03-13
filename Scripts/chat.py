from google import genai
import os
import time

# 代理设置
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

client = genai.Client(api_key="AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E")

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
    print("--- 🤖 超级个体数据库助理已上线 (输入 'quit' 退出) ---")

    while True:
        try:
            user_input = input("✨ 你想处理什么任务？: ")
        except KeyboardInterrupt:
            # 输入阶段被中断
            print("\n操作被用户中断，返回菜单。")
            break
        if user_input.lower() in ['quit', 'exit', '退出']:
            break
        
        # 这里的 stream=True 就是实现“可视化逐字弹出”的关键
        response = retry_on_429(client.models.generate_content,
            model="gemini-2.0-flash",
            contents=user_input,
        )
        print(f"\n💎 Gemini: \n{response.text}\n")

if __name__ == "__main__":
    import sys
    try:
        main()
    except KeyboardInterrupt:
        print("\n操作被用户中断，返回菜单。")
        sys.exit(0)