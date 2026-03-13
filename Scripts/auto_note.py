from google import genai
import os

# --- 1. 配置区 ---
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

client = genai.Client(api_key="AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E")

# 【关键点】定义根目录。因为脚本在 Scripts 里，笔记在外面，所以用 ..
CORE_DIR = ".." 
note_name = "测试笔记.md" 

def summarize_my_note():
    try:
        # 使用 os.path.join 把路径和文件名拼起来
        # 结果就是：../测试笔记.md
        full_path = os.path.join(CORE_DIR, note_name)

        if not os.path.exists(full_path):
            print(f"❌ 找不到文件: {full_path}")
            print(f"ℹ️ 当前脚本运行位置: {os.getcwd()}")
            return

        with open(full_path, "r", encoding="utf-8") as f:
            note_content = f.read()

        print(f"📖 正在阅读上一级目录的笔记: {note_name}...")

        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"请用一句话总结下面这篇 Obsidian 笔记的核心内容：\n\n{note_content}"
        )

        print("\n--- Gemini 的总结 ---")
        print(response.text)

        # 写回时也使用拼接后的完整路径
        with open(full_path, "a", encoding="utf-8") as f:
            f.write(f"\n\n> [!todo] AI 自动总结\n> {response.text.strip()}")
        print(f"\n✅ 总结已同步至 {note_name}")

    except Exception as e:
        print(f"运行失败: {e}")

if __name__ == "__main__":
    summarize_my_note()