@echo off
:: 设置编码为UTF-8以支持中文显示
chcp 65001 >nul

:menu
cls
echo ===========================================
echo    2026 超级助手数据库工具
echo ===========================================
echo [1] 系统检查 (Doctor)
echo [2] 聊天模式 (Chat)
echo [3] GraphLinker.py (双链灵感触发器)
echo [4] Gemini CLI
echo [5] 退出

echo ===========================================
set /p opt=请选择编号: 

:: 使用 start /b /wait 运行 Python，避免 Ctrl+C 提示并返回菜单
if %opt%==1 start /b /wait "" python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\doctor.py"
if %opt%==2 start /b /wait "" python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\chat.py"
if %opt%==3 start /b /wait "" python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\GraphLinker.py"
if %opt%==4 start /b /wait "" python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\gemini_cli.py"
if %opt%==5 exit

echo.
echo 操作完成，按任意键返回菜单...
pause >nul
goto menu
