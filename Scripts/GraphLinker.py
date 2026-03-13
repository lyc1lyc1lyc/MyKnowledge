import os
import time
from google import genai
from google.genai import errors
import glob
import re

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

def get_recent_note(vault_path):
    """获取最近修改的笔记文件"""
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    if not md_files:
        return None
    # 排除Templates和Scripts文件夹
    md_files = [f for f in md_files if not any(x in f for x in ['999 Templates', 'Scripts'])]
    if not md_files:
        return None
    # 按修改时间排序，取最新的
    md_files.sort(key=os.path.getmtime, reverse=True)
    return md_files[0]

def get_all_titles(vault_path):
    """获取所有笔记的标题列表"""
    titles = []
    md_files = glob.glob(os.path.join(vault_path, "**", "*.md"), recursive=True)
    md_files = [f for f in md_files if not any(x in f for x in ['999 Templates', 'Scripts'])]
    for file in md_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                if first_line.startswith('# '):
                    title = first_line[2:]
                else:
                    title = os.path.basename(file).replace('.md', '')
                titles.append(title)
        except:
            pass
    return titles

def analyze_and_suggest(content, titles):
    """使用AI分析内容并建议链接"""
    prompt = f"""
    你现在是 Zettelkasten 专家。
    任务：分析以下新笔记，并从已知标题列表中找出 3 个最具【逻辑相关性】的笔记进行双链关联。
    
    新笔记内容：
    {content[:2000]}  # 限制内容长度
    
    库中已有标题列表（部分）：
    {', '.join(titles[:100])}  # 前100个标题
    
    要求：
    1. 不要摘要。
    2. 给出 2-3 条建议，格式为：- [[标题]]: [关联原因，一句话说明它们如何互补或冲突]。
    3. 如果新笔记太长（超过 500 字），请指出具体的拆分点。
    """
    try:
        response = retry_on_429(client.models.generate_content,
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"AI分析失败: {e}")
        return "AI分析失败，请检查网络和API。"

def append_suggestions_to_note(note_path, suggestions):
    """将建议追加到笔记末尾"""
    try:
        with open(note_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 检查是否已有相关探讨章节
        if "## 相关探讨" in content:
            print("笔记已有相关探讨章节，跳过追加。")
            return
        # 追加到末尾
        new_content = content + "\n\n## 相关探讨\n\n" + suggestions
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ 已将建议追加到 {note_path}")
    except Exception as e:
        print(f"写入失败: {e}")

def main():
    vault_path = r"C:\Users\chaoy\obsidian\MyKnowledge"
    print("🔍 正在扫描知识库，寻找深度关联...")

    # 获取最近笔记
    recent_note = get_recent_note(vault_path)
    if not recent_note:
        print("❌ 未找到笔记文件。")
        return

    print(f"📝 最近修改的笔记: {os.path.basename(recent_note)}")

    # 读取内容
    try:
        with open(recent_note, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取笔记失败: {e}")
        return

    # 获取所有标题
    titles = get_all_titles(vault_path)
    print(f"📚 库中有 {len(titles)} 个笔记标题。")

    # AI分析
    print("🤖 AI正在分析...")
    suggestions = analyze_and_suggest(content, titles)

    print("💡 AI建议:")
    print(suggestions)

    # 自动追加到笔记
    append_suggestions_to_note(recent_note, suggestions)

if __name__ == "__main__":
    main()