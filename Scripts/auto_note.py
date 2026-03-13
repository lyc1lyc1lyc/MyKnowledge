from google import genai
import os

# 1. 代理配置
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# 2. 初始化（AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E）
client = genai.Client(api_key="你的_AIza_开头_Key")

# 3. 指定你要读取的笔记名称 (请确保 MyKnowledge 文件夹里真有这个文件)
note_name = "测试笔记.md" 

def summarize_my_note():
    try:
        # 读取本地 Obsidian 笔记文件
        if not os.path.exists(note_name):
            print(f"❌ 找不到文件: {note_name}，请先在文件夹里创建一个。")
            return

        with open(note_name, "r", encoding="utf-8") as f:
            note_content = f.read()

        print(f"📖 正在阅读笔记: {note_name}...")

        # 调用 Gemini 2.0 
        # 注意：模型名称前不用加 models/，直接写名字
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"请用一句话总结下面这篇 Obsidian 笔记的核心内容：\n\n{note_content}"
        )

        print("\n--- Gemini 的总结 ---")
        print(response.text)

        # (可选) 把总结写回文件末尾
        with open(note_name, "a", encoding="utf-8") as f:
            f.write(f"\n\n> [!todo] AI 自动总结\n> {response.text.strip()}")
        print(f"\n✅ 总结已同步至 {note_name}")

    except Exception as e:
        print(f"运行失败: {e}")

if __name__ == "__main__":
    summarize_my_note()