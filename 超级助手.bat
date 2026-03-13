@echo off
:: Set to UTF-8 for proper display
chcp 65001 >nul

:menu
cls
echo ===========================================
echo    2026 Super Individual: Database Terminal
echo ===========================================
echo [1] System Check (Doctor)
echo [2] AI Chat (Chat)
echo [3] Deep Link Discovery (GraphLink)
echo [4] Exit
echo ===========================================
set /p opt=Choose option number:

:: Use full paths to prevent issues
if %opt%==1 "C:\Users\chaoy\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\doctor.py"
if %opt%==2 "C:\Users\chaoy\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\chat.py"
if %opt%==3 "C:\Users\chaoy\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\GraphLinker.py"
if %opt%==4 exit

echo.
echo Operation completed, press any key to return to menu...
pause >nul
goto menu