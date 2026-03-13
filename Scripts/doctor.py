from google import genai
from google.genai import errors
import os
import requests
import time

# --- 配置区 ---
API_KEY = "AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E"
PROXY_URL = "http://127.0.0.1:7890"

os.environ["HTTP_PROXY"] = PROXY_URL
os.environ["HTTPS_PROXY"] = PROXY_URL

def retry_on_429(func, *args, **kwargs):
    while True:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "429" in str(e):
                print("  ⚠️ 遇到429错误，等待60秒后重试... (按Ctrl+C可中断)")
                try:
                    for i in range(60, 0, -1):
                        print(f"  倒计时: {i} 秒", end='\r')
                        time.sleep(1)
                    print("  继续重试...")
                except KeyboardInterrupt:
                    print("\n  重试被用户中断。")
                    raise
            else:
                raise

def check_system():
    print("🔍 [1/3] 正在检查网络连接 (代理测试)...")
    try:
        # 尝试连接 Google 首页，超时设为 5 秒
        resp = requests.get("https://www.google.com", timeout=5)
        if resp.status_code == 200:
            print("  ✅ 网络畅通：FlClash 代理正常工作。")
    except Exception:
        print("  ❌ 网络失败：请检查 FlClash 是否开启，端口 7890 是否正确。")
        return

    print("\n🔍 [2/3] 正在验证 API Key 状态...")
    client = genai.Client(api_key=API_KEY)
    try:
        # 发送一个超短请求测试额度
        response = retry_on_429(client.models.generate_content,
            model="gemini-2.0-flash", contents="pong"
        )
        print("  ✅ API 正常：额度充足，可以继续建设数据库。")
    except errors.ClientError as e:
        # 识别具体的 API 错误码
        if "429" in str(e):
            print("  ⚠️ 额度枯竭：API 没问题，但你用得太快了，请休息 1-5 分钟。")
        elif "403" in str(e):
            print("  ❌ 权限错误：可能是 API Key 抄错了，或该 Key 被封禁。")
        else:
            print(f"  ❓ 其他 API 错误: {e}")
        return

    print("\n🔍 [3/3] 数据库文件环境检查...")
    # 检查 MyKnowledge 是否有 .md 文件
    md_files = [f for f in os.listdir('.') if f.endswith('.md')]
    print(f"  📂 当前文件夹共有 {len(md_files)} 个笔记文件。")
    
    print("\n🚀 [系统准备就绪] 你可以运行 chat.py 或其他自动化脚本了。")

if __name__ == "__main__":
    check_system()