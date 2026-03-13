#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检测 Gemini CLI 是否正常安装的脚本
"""

import subprocess
import sys

def check_gemini_cli():
    print("[debug] PATH=", subprocess.run(['echo', '%PATH%'], capture_output=True, text=True, shell=True).stdout)
    print("[debug] where gemini ->", subprocess.run(['where', 'gemini'], capture_output=True, text=True, shell=True).stdout)
    try:
        # 尝试运行 gemini --version 命令，使用shell=True以使用系统PATH
        result = subprocess.run(['gemini', '--version'],
                              capture_output=True,
                              text=True,
                              timeout=10,
                              shell=True)

        if result.returncode == 0:
            print("✅ Gemini CLI 已正常安装！")
            print(f"版本信息: {result.stdout.strip()}")
            return True
        else:
            print("❌ Gemini CLI 安装异常")
            print(f"错误输出: {result.stderr.strip()}")
            return False

    except FileNotFoundError:
        print("❌ Gemini CLI 未安装")
        print("请确保 Gemini CLI 已正确安装并添加到系统 PATH 中")
        return False
    except subprocess.TimeoutExpired:
        print("❌ 检查超时，Gemini CLI 可能无响应")
        return False
    except Exception as e:
        print(f"❌ 检查过程中发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    print("🔍 正在检测 Gemini CLI 安装状态...")
    success = check_gemini_cli()
    sys.exit(0 if success else 1)