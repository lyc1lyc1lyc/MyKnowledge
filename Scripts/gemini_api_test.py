#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test script to verify Gemini API access via google-generativeai library."""

import os
import sys

try:
    import google.generativeai as genai
except ImportError as e:
    print("❌ google-generativeai 未安装，请运行: pip install -U google-generativeai")
    sys.exit(1)

API_KEY = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("❌ 未检测到 API Key。请先设置环境变量 GOOGLE_API_KEY 或 GEMINI_API_KEY")
    sys.exit(1)

print("🔑 使用 API Key 进行验证（不会输出密钥）...")
genai.configure(api_key=API_KEY)

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate("请用中文简短介绍一下 Gemini CLI 主要用途，并给出一个小例子。")
    print("\n✅ 调用成功，返回内容：\n")
    print(resp.text)
except Exception as e:
    print("❌ 调用失败：", str(e))
    sys.exit(1)
