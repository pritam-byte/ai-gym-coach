@echo off
cd /d "%~dp0"
echo ========================================================
echo    AI REAL-TIME GYM COACH (Vision & Voice AI)
echo ========================================================
echo.
echo Starting AI Workout Coach at http://localhost:8501...
echo.
.\.venv311\Scripts\streamlit.exe run main.py
pause
