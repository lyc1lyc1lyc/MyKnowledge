from google import genai
import os

# 代理设置
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

client = genai.Client(api_key="AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E")

print("--- 🤖 超级个体数据库助理已上线 (输入 'quit' 退出) ---")

while True:
    user_input = input("✨ 你想处理什么任务？: ")
    if user_input.lower() in ['quit', 'exit', '退出']:
        break
    
    # 这里的 stream=True 就是实现“可视化逐字弹出”的关键
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input,
    )
    print(f"\n💎 Gemini: \n{response.text}\n")