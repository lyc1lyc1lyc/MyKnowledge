@echo off
chcp 65001 >nul
cd /d "%~dp0"

:menu
cls
echo --- 🤖 超级个体数据库助理菜单 ---
echo [1] 系统检查
echo [2] 聊天模式
echo [3] 自动笔记
echo [4] 深度链接发现 (GraphLink)
echo [0] 退出
set /p choice="请选择: "
if "%choice%"=="1" goto check
if "%choice%"=="2" goto chat
if "%choice%"=="3" goto auto
if "%choice%"=="4" goto graph
if "%choice%"=="0" goto exit
echo 无效选择，请重试。
pause
goto menu

:check
python Scripts\doctor.py
pause
goto menu

:chat
python Scripts\chat.py
pause
goto menu

:auto
python Scripts\auto_note.py
pause
goto menu

:graph
python Scripts\GraphLinker.py
pause
goto menu

:exit
echo 退出。
pause
