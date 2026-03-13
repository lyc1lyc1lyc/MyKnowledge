@echo off
:: 设置编码为GBK以支持中文显示
chcp 936 >nul

:menu
cls
echo ===========================================
echo    2026 �������壺���ݿ�����ն�
echo ===========================================
echo [1] ϵͳ�Լ� (Doctor)
echo [2] ���� AI ���� (Chat)
echo [3] GraphLinker.py (˫�����ȼ�����)
echo [4] �˳�
echo ===========================================
set /p opt=��ѡ��������: 

:: ����ʹ�þ���·������ֹ��Ϊλ���ƶ������Ҳ����ļ�
if %opt%==1 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\doctor.py"
if %opt%==2 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\chat.py"
if %opt%==3 python "C:\Users\chaoy\obsidian\MyKnowledge\Scripts\GraphLinker.py"
if %opt%==4 exit

echo.
echo ������ɣ�����������ز˵�...
pause >nul
goto menu