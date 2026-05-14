@echo off
setlocal

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python.
    exit /b 1
)

echo Python is installed.
echo Checking for requirements.txt...

if not exist "..\requirements.txt" (
    echo requirements.txt not found. Creating one...
    echo pyautogui > "..\requirements.txt"
    echo opencv-python >> "..\requirements.txt"
)

echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r "..\requirements.txt"

echo.
echo You're good! Everything is set up and done.
pause
