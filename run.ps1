Set-Location $PSScriptRoot
Write-Host "Starting AI Real-Time Gym Coach..." -ForegroundColor Green
& ".\.venv311\Scripts\streamlit.exe" run main.py
