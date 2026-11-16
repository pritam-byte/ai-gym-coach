@echo off
cd /d "%~dp0"
echo ========================================================
echo    AI REAL-TIME GYM COACH (Vision & Voice Multimodal AI)
echo ========================================================
echo.
echo [1/2] Opening Front Page in your browser...
start "" "%~dp0REALTIME-VOICE-VISION-EXERCISE-MULTIMODAL\index.html"
echo.
echo [2/2] Starting AI Workout Engine at http://localhost:8501...
echo.
.\.venv311\Scripts\streamlit.exe run main.py
pause
