@echo off
cd /d "%~dp0"
echo Starting AI Real-Time Gym Coach...
.\.venv311\Scripts\streamlit.exe run main.py
pause
