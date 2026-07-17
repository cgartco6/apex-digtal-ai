Write-Host "Apex Digital AI Windows Setup" -ForegroundColor Green
pip install -r requirements.txt
New-Item -ItemType Directory -Force -Path "deliverables" | Out-Null
Write-Host "Setup complete. Run: python main.py" -ForegroundColor Green
