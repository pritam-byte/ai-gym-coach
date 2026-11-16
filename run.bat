@echo off
cd /d "%~dp0"
echo ========================================================
echo    AI REAL-TIME GYM COACH (Vision & Voice AI)
echo ========================================================
echo.
echo [1/2] Opening Front Page Portal in your browser...
start "" "%~dp0REALTIME-VOICE-VISION-EXERCISE-MULTIMODAL\index.html"
echo.
echo [2/2] Booting AI Workout Engine on http://localhost:8501...
echo (Click "TRY IT LIVE" on the front page to enter your live workout!)
echo.
.\.venv311\Scripts\streamlit.exe run main.py --server.headless=true
pause
