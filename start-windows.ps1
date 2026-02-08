# 청산에사르리랏다 서버 시작 (PowerShell)
# Chungsan Settlement System

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "청산에사르리랏다 서버 시작" -ForegroundColor Yellow
Write-Host "Chungsan Settlement System" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 가상환경 확인 및 생성
if (!(Test-Path "venv")) {
    Write-Host "[1/3] 가상환경 생성 중..." -ForegroundColor Green
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "오류: Python이 설치되어 있지 않거나 PATH에 없습니다." -ForegroundColor Red
        Write-Host "https://www.python.org/downloads/ 에서 Python을 설치하세요." -ForegroundColor Yellow
        Read-Host "계속하려면 Enter를 누르세요"
        exit 1
    }
    Write-Host "✓ 가상환경 생성 완료" -ForegroundColor Green
    Write-Host ""
}

# 가상환경 활성화
Write-Host "[2/3] 가상환경 활성화 중..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1
if ($LASTEXITCODE -ne 0) {
    Write-Host "오류: 가상환경 활성화 실패" -ForegroundColor Red
    Write-Host "PowerShell 실행 정책을 변경해야 할 수 있습니다:" -ForegroundColor Yellow
    Write-Host "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Cyan
    Read-Host "계속하려면 Enter를 누르세요"
    exit 1
}
Write-Host "✓ 가상환경 활성화 완료" -ForegroundColor Green
Write-Host ""

# 패키지 설치
Write-Host "[3/3] 패키지 확인 및 설치 중..." -ForegroundColor Green
pip install -r requirements.txt --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "오류: 패키지 설치 실패" -ForegroundColor Red
    Read-Host "계속하려면 Enter를 누르세요"
    exit 1
}
Write-Host "✓ 패키지 설치 완료" -ForegroundColor Green
Write-Host ""

# 서버 실행
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "서버 실행 중..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "접속 URL:" -ForegroundColor White
Write-Host "  - 메인: http://localhost:8001" -ForegroundColor Cyan
Write-Host "  - API 문서: http://localhost:8001/docs" -ForegroundColor Cyan
Write-Host "  - ReDoc: http://localhost:8001/redoc" -ForegroundColor Cyan
Write-Host ""
Write-Host "종료하려면 Ctrl+C를 누르세요" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python main.py

# 서버 종료 후
Write-Host ""
Write-Host "서버가 종료되었습니다." -ForegroundColor Yellow
Read-Host "계속하려면 Enter를 누르세요"
