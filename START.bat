@echo off
echo ============================================
echo  PHISHING CONTROLLER - Professional
echo ============================================
echo.
echo Starting Flask Server...
start "Flask Server" cmd /k "cd /d C:\Users\hacke\Desktop\phishing_demo && python app.py"
timeout /t 5 /nobreak >nul
echo Starting Phishing Controller...
start "Controller" cmd /k "cd /d C:\Users\hacke\Desktop\phishing_demo && python phishing_controller.py"
echo.
echo Both servers running.
echo.
echo Dashboard: http://127.0.0.1:3000/dashboard
echo.
pause