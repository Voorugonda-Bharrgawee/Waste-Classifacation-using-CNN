@echo off
echo ========================================
echo Waste Classification Model Training
echo ========================================
echo.
echo This will train the model and may take 30-60 minutes.
echo Press Ctrl+C to cancel if needed.
echo.
pause
cd /d "%~dp0"
python train_model.py
pause







