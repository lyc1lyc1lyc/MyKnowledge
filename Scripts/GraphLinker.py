import os
import re
import time
from google import genai
import glob

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

def suggest_links(new_note_content, existing_titles):
    prompt = f"""
    你现在是 Zettelkasten 专家。
    任务：分析以下新笔记，并从已知标题列表中找出 3 个最具【逻辑相关性】的笔记进行双链关联。
    
    新笔记内容：
    {new_note_content}
    
    库中已有标题列表（部分）：
    {existing_titles[:200]}  # 传入前200个字符的标题列表
    
    要求：
    1. 不要摘要。
    2. 给出 2-3 条建议，格式为：- [[标题]]: [关联原因，一句话说明它们如何互补或冲突]。
    3. 如果新笔记太长（超过 500 字），请指出具体的拆分点。
    4. 提取 3-5 个核心语义特征（不仅是关键词，而是底层逻辑）。
    """
    response = retry_on_429(client.models.generate_content,
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

def get_recent_note(vault_path):
    # 获取最近修改的.md文件
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    if not md_files:
        return None
    # 按修改时间排序，取最新的
    recent_file = max(md_files, key=os.path.getmtime)
    return recent_file

def get_all_titles(vault_path):
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    titles = []
    for file in md_files:
        # 提取文件名作为标题（去掉.md）
        title = os.path.splitext(os.path.basename(file))[0]
        titles.append(title)
    return titles

def main():
    vault_path = r"C:\Users\chaoy\obsidian\MyKnowledge"
    print("🔍 正在扫描知识库，寻找深度关联...")

    # 1. 获取最近修改的一篇笔记
    recent_note_path = get_recent_note(vault_path)
    if not recent_note_path:
        print("❌ 未找到任何.md文件。")
        return

    print(f"📖 分析最近笔记: {os.path.basename(recent_note_path)}")

    # 2. 读取内容
    try:
        with open(recent_note_path, "r", encoding="utf-8") as f:
            note_content = f.read()
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return

    # 3. 获取所有文件名作为索引
    existing_titles = get_all_titles(vault_path)
    titles_str = "\n".join(existing_titles)

    # 4. 运行 AI 建议
    suggestions = suggest_links(note_content, titles_str)

    print("\n--- AI 深度关联建议 ---")
    print(suggestions)

    # 5. 自动写入到笔记末尾
    with open(recent_note_path, "a", encoding="utf-8") as f:
        f.write(f"\n\n## 相关探讨\n\n{suggestions}")
    print(f"\n✅ 建议已自动写入到 {os.path.basename(recent_note_path)}")

if __name__ == "__main__":
    main()