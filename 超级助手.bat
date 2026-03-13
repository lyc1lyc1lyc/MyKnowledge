@echo off
:: 取消对 Ctrl+C/Break 的增强处理，以便批处理能接收到中断事件
::（不再使用 "break off"，否则 ON BREAK 无效）
:: 当用户按 Ctrl+C/Break 时直接回到菜单
ON BREAK GOTO menu
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
echo [4] 退出

echo ===========================================
set /p opt=请选择编号: 

:: 使用 call 调用 Python，出错或中断后仍会返回批处理
if %opt%==1 call python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\doctor.py"
if %opt%==2 call python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\chat.py"
if %opt%==3 call python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\GraphLinker.py"
if %opt%==4 exit

echo.
echo 操作完成，按任意键返回菜单...
pause >nul
goto menu
