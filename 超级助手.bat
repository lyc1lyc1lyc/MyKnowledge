@echo off
:: 设置中文显示
chcp 936 >nul

:menu
cls
echo ===========================================
echo    2026 超级个体：数据库管理终端
echo ===========================================
echo [1] 系统自检 (Doctor)
echo [2] 开启 AI 聊天 (Chat)
echo [3] 退出
echo ===========================================
set /p opt=请选择操作序号: 

:: 这里使用绝对路径，防止因为位置移动导致找不到文件
if %opt%==1 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\doctor.py"
if %opt%==2 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\chat.py"
if %opt%==3 exit

echo.
echo 操作完成，按任意键返回菜单...
pause >nul
goto menu