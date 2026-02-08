# 청산에사르리랏다 - 윈도우 로컬 실행 가이드

## 💻 윈도우에서 실행하기

### 📋 필수 프로그램 설치

#### 1. Python 3.8+ 설치
- 다운로드: https://www.python.org/downloads/
- 설치 시 **"Add Python to PATH"** 체크 필수!
- 설치 확인:
```cmd
python --version
```

#### 2. Git 설치 (선택사항)
- 다운로드: https://git-scm.com/download/win
- 또는 GitHub Desktop 사용

---

## 🚀 실행 방법

### 방법 1: 명령 프롬프트(CMD) 사용

#### 1️⃣ 저장소 다운로드
```cmd
REM Git 사용
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan

REM 또는 ZIP 다운로드 후 압축 해제
REM https://github.com/EmmettHwang/chungsan/archive/refs/heads/main.zip
```

#### 2️⃣ 가상환경 생성 및 활성화
```cmd
REM 가상환경 생성
python -m venv venv

REM 가상환경 활성화
venv\Scripts\activate

REM 성공하면 프롬프트 앞에 (venv) 표시됨
```

#### 3️⃣ 패키지 설치
```cmd
pip install -r requirements.txt
```

#### 4️⃣ 서버 실행
```cmd
python main.py

REM 또는
uvicorn main:app --reload --port 8001
```

#### 5️⃣ 브라우저에서 접속
- 메인: http://localhost:8001
- API 문서: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

---

### 방법 2: PowerShell 사용

#### 1️⃣ PowerShell 열기
- `Win + X` → "Windows PowerShell" 또는 "Windows Terminal"

#### 2️⃣ 실행 정책 설정 (최초 1회)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 3️⃣ 저장소 다운로드
```powershell
# Git 사용
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan
```

#### 4️⃣ 가상환경 생성 및 활성화
```powershell
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
.\venv\Scripts\Activate.ps1

# 성공하면 (venv) 표시됨
```

#### 5️⃣ 패키지 설치 및 실행
```powershell
pip install -r requirements.txt
python main.py
```

---

### 방법 3: 배치 파일 사용 (가장 쉬움!)

#### `start-windows.bat` 파일 생성
```batch
@echo off
echo ========================================
echo 청산에사르리랏다 서버 시작
echo ========================================
echo.

REM 가상환경이 없으면 생성
if not exist venv (
    echo 가상환경 생성 중...
    python -m venv venv
)

REM 가상환경 활성화
call venv\Scripts\activate.bat

REM 패키지 설치
echo 패키지 설치 중...
pip install -r requirements.txt --quiet

REM 서버 실행
echo.
echo 서버 시작 중...
echo API 문서: http://localhost:8001/docs
echo.
python main.py

pause
```

#### 실행 방법
1. `start-windows.bat` 파일 더블클릭
2. 브라우저에서 http://localhost:8001/docs 접속

---

## 🔧 트러블슈팅

### ❌ 오류 1: "python을 찾을 수 없습니다"
**원인**: Python이 PATH에 없음

**해결**:
1. Python 재설치 시 "Add Python to PATH" 체크
2. 또는 수동으로 PATH 추가:
   - 시스템 환경 변수 편집
   - `C:\Users\사용자명\AppData\Local\Programs\Python\Python312` 추가

### ❌ 오류 2: "Activate.ps1을 로드할 수 없습니다"
**원인**: PowerShell 실행 정책

**해결**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ 오류 3: 포트 8001이 이미 사용 중
**원인**: 다른 프로그램이 포트 사용

**해결**:
```cmd
REM 다른 포트 사용
python main.py --port 8002

REM 또는 포트 사용 프로세스 종료
netstat -ano | findstr :8001
taskkill /PID [PID번호] /F
```

### ❌ 오류 4: 패키지 설치 실패
**원인**: pip 버전이 오래됨

**해결**:
```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### ❌ 오류 5: SQLite 데이터베이스 오류
**원인**: chungsan.db 파일 권한 문제

**해결**:
```cmd
REM 데이터베이스 파일 삭제 후 재생성
del chungsan.db
python main.py
```

---

## 📦 프로젝트 구조 (윈도우)

```
C:\청산에사르리랏다\
├── app\
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers\
│       ├── participants.py
│       ├── projects.py
│       └── settlements.py
├── venv\                    (가상환경)
├── main.py                  (서버 실행 파일)
├── requirements.txt         (패키지 목록)
├── chungsan.db             (SQLite DB)
├── start-windows.bat       (윈도우 실행 스크립트)
└── README.md
```

---

## 🎯 빠른 시작 (All-in-One)

### CMD 한 번에 실행
```cmd
git clone https://github.com/EmmettHwang/chungsan.git && cd chungsan && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python main.py
```

### PowerShell 한 번에 실행
```powershell
git clone https://github.com/EmmettHwang/chungsan.git; cd chungsan; python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; python main.py
```

---

## 🌐 접속 URL (윈도우 로컬)

| 서비스 | URL |
|--------|-----|
| **메인 페이지** | http://localhost:8001 |
| **API 문서 (Swagger)** | http://localhost:8001/docs |
| **API 문서 (ReDoc)** | http://localhost:8001/redoc |
| **헬스 체크** | http://localhost:8001/health |

---

## 🛑 서버 종료

### 방법 1: 키보드
```
Ctrl + C
```

### 방법 2: 작업 관리자
```
Ctrl + Shift + Esc
→ "Python" 프로세스 찾기
→ "작업 끝내기"
```

---

## 📱 윈도우에서 개발하기

### VS Code 추천 확장
1. **Python** - Microsoft
2. **Pylance** - Microsoft
3. **SQLite Viewer** - 데이터베이스 확인
4. **Thunder Client** - API 테스트

### VS Code에서 실행
```
1. VS Code 열기 (Ctrl + Shift + P)
2. "Python: Select Interpreter" 선택
3. venv\Scripts\python.exe 선택
4. Terminal → New Terminal (Ctrl + `)
5. python main.py
```

---

## 🔥 윈도우 최적화 팁

### 1. 가상환경 자동 활성화
**settings.json (VS Code)**
```json
{
    "python.terminal.activateEnvironment": true,
    "python.defaultInterpreterPath": "${workspaceFolder}\\venv\\Scripts\\python.exe"
}
```

### 2. 데이터베이스 백업 스크립트 (backup.bat)
```batch
@echo off
set TIMESTAMP=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%
copy chungsan.db backups\chungsan_%TIMESTAMP%.db
echo 백업 완료: chungsan_%TIMESTAMP%.db
```

### 3. 서버 자동 재시작 (watch.bat)
```batch
@echo off
:loop
python main.py
timeout /t 2
goto loop
```

---

## 📞 윈도우 관련 문제 해결

### 한글 깨짐 문제
```cmd
chcp 65001
python main.py
```

### 방화벽 경고
- "액세스 허용" 클릭
- 또는 방화벽 → 앱 허용 → Python 추가

### 관리자 권한 필요 시
```
프로그램 우클릭 → "관리자 권한으로 실행"
```

---

## 🎉 설치 완료!

### 다음 단계
1. ✅ http://localhost:8001/docs 접속
2. ✅ API 테스트 (Swagger UI)
3. ✅ 참여자 생성해보기
4. ✅ 프로젝트 만들고 정산 계산하기

---

**생성 일시**: 2026-02-08  
**프로젝트**: 청산에사르리랏다  
**GitHub**: https://github.com/EmmettHwang/chungsan  
**문서**: BACKEND_COMPLETE.md, LOCAL_SETUP_GUIDE.md
