import os
import sys

# 【关键步】强制指定代理，解决截图中的 SSL EOF 错误
# 确保端口 7890 与你的代理软件（FlClash）一致
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

try:
    import google.generativeai as genai
    from PIL import Image
    print("✅ 基础环境：Python SDK 已安装")
except ImportError:
    print("❌ 错误：未检测到 google-generativeai，请运行: pip install -q -U google-generativeai")
    sys.exit()

# 配置你的 API KEY
# 建议：实际使用时将其放入系统环境变量
API_KEY = "AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E" 

def test_connection():
    print(f"📡 正在尝试连接 Gemini (代理: 127.0.0.1:7890)...")
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 极简请求测试
        response = model.generate_content("你好，如果你收到这条信息，请回复'连接正常'")
        
        if response.text:
            print(f"🚀 测试成功！Gemini 回复: {response.text}")
            print("\n--- 结论：你的 Gemini CLI 环境已完全打通 ---")
    except Exception as e:
        print(f"\n❌ 连接失败！错误详情：\n{str(e)}")
        print("\n💡 针对性建议：")
        if "EOF occurred" in str(e):
            print("   -> 这依然是 SSL 握手失败。请检查：1. 代理软件是否开启 2. 是否开启了 TUN 模式 3. 端口是否真的是 7890")
        elif "429" in str(e):
            print("   -> API 频率超限。请等待 60 秒或检查 API Key 额度。")
        elif "API_KEY_INVALID" in str(e):
            print("   -> API Key 填写错误，请重新检查。")

if __name__ == "__main__":
    test_connection()