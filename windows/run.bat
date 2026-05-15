@echo off
echo Starting the auto-retry bot...
cd ..
echo.
echo Select which image(s) to check:
echo   1. Retry Button (retrybutton.png)
echo   2. Allow in Workspace (allowinworkspace.png)
echo   all. Both images
set /p choice="Enter 1, 2, or all: "
if "%choice%"=="" set choice=all
python bot.py --check %choice%
pause
