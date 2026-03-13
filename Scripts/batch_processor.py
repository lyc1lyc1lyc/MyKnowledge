import os
import time
from google import genai
from google.genai import errors

# --- 1. 配置区 ---
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

client = genai.Client(api_key="AIzaSyAr0pnh1EvT891oHt-MZQ3uaON99SC7i0E")
VAULT_DIR = ".."  # 返回上一级，即 Obsidian 库根目录

def ai_process_content(content):
    """带 429 自动静默重试的核心函数"""
    while True:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=f"请为这篇笔记写一个50字以内的核心摘要：\n\n{content}"
            )
            return response.text
        except errors.ClientError as e:
            if "429" in str(e):
                print("  ⚠️ 服务器拥挤 (429)，静默等待 60 秒后自动继续...")
                time.sleep(60)
            else:
                print(f"  ❌ 遇到其他错误: {e}")
                return None

def run_batch():
    print("🚀 2026 超级个体：全库笔记批量摘要任务启动...")
    
    # 扫描所有 .md 文件
    for root, dirs, files in os.walk(VAULT_DIR):
        # 跳过脚本文件夹本身
        if "Scripts" in root: continue
        
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # 读取笔记
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # 如果已经有摘要了，就跳过（防止重复处理）
                if "> [!abstract] AI 摘要" in content:
                    print(f"⏩ 跳过已处理文件: {file}")
                    continue

                print(f"📝 正在处理: {file}...")
                summary = ai_process_content(content)
                
                if summary:
                    # 将摘要插入到笔记开头
                    new_content = f"> [!abstract] AI 摘要\n> {summary.strip()}\n\n" + content
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ 摘要已添加至: {file}")

if __name__ == "__main__":
    run_batch()