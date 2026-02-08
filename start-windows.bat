@echo off
chcp 65001 >nul
cls
echo ========================================
echo 청산에사르리랏다 서버 시작
echo Chungsan Settlement System
echo ========================================
echo.

REM 가상환경이 없으면 생성
if not exist venv (
    echo [1/3] 가상환경 생성 중...
    python -m venv venv
    if errorlevel 1 (
        echo 오류: Python이 설치되어 있지 않거나 PATH에 없습니다.
        echo https://www.python.org/downloads/ 에서 Python을 설치하세요.
        pause
        exit /b 1
    )
    echo ✓ 가상환경 생성 완료
    echo.
)

REM 가상환경 활성화
echo [2/3] 가상환경 활성화 중...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo 오류: 가상환경 활성화 실패
    pause
    exit /b 1
)
echo ✓ 가상환경 활성화 완료
echo.

REM 패키지 설치 확인 및 설치
echo [3/3] 패키지 확인 및 설치 중...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo 오류: 패키지 설치 실패
    pause
    exit /b 1
)
echo ✓ 패키지 설치 완료
echo.

REM 서버 실행
echo ========================================
echo 서버 실행 중...
echo ========================================
echo.
echo 접속 URL:
echo   - 메인: http://localhost:8001
echo   - API 문서: http://localhost:8001/docs
echo   - ReDoc: http://localhost:8001/redoc
echo.
echo 종료하려면 Ctrl+C를 누르세요
echo ========================================
echo.

python main.py

REM 서버 종료 후
echo.
echo 서버가 종료되었습니다.
pause
