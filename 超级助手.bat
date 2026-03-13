@echo off
:: 设置编码为GBK以支持中文显示
chcp 936 >nul

:menu
cls
echo ===========================================
echo    2026 超级助手数据库工具
echo ===========================================
echo [1] 系统检查 (Doctor)
echo [2] 聊天模式 (Chat)
echo [3] GraphLinker.py (双链灵感触发器)
echo [4] 退出

echo ===========================================
set /p opt=请选择编号: 

:: 使用完整路径以避免被移动
if %opt%==1 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\doctor.py"
if %opt%==2 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\chat.py"
if %opt%==3 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\GraphLinker.py"
if %opt%==4 exit

echo.
echo 操作完成，按任意键返回菜单...
pause >nul
goto menu
