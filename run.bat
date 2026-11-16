@echo off
cd /d "%~dp0"
echo ========================================================
echo    AI REAL-TIME GYM COACH (Vision & Voice AI)
echo ========================================================
echo.
echo Launching Streamlit Workout Coach on http://localhost:8501...
echo (Tip: You can also open launch_website.bat for the Showcase Landing Page)
echo.
.\.venv311\Scripts\streamlit.exe run main.py
pause
