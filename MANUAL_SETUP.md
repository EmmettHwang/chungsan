# 🪟 청산에사르리랏다 - 수동 실행 가이드 (Windows)

> **작성일**: 2026-02-08  
> **프로젝트**: 청산에사르리랏다 (Chungsan Settlement System)  
> **버전**: v1.0.0

---

## 📋 목차

1. [사전 준비](#사전-준비)
2. [다운로드 방법](#다운로드-방법)
3. [수동 실행 방법](#수동-실행-방법)
4. [실행 확인](#실행-확인)
5. [문제 해결](#문제-해결)

---

## 🎯 사전 준비

### 1️⃣ Python 설치 확인

**방법 1: 명령 프롬프트(CMD)**
```cmd
python --version
```

**방법 2: PowerShell**
```powershell
python --version
```

**출력 예시:**
```
Python 3.11.5
```

> ⚠️ **Python이 설치되어 있지 않다면?**  
> https://www.python.org/downloads/ 에서 다운로드 (3.8 이상 필요)

### 2️⃣ Git 설치 확인 (선택사항)

```cmd
git --version
```

> Git이 없어도 ZIP 다운로드로 실행 가능합니다!

---

## 📥 다운로드 방법

### 방법 1: Git Clone (추천)

```cmd
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan
```

### 방법 2: ZIP 다운로드

1. 브라우저에서 https://github.com/EmmettHwang/chungsan 접속
2. **Code** 버튼 클릭
3. **Download ZIP** 선택
4. 다운로드한 ZIP 파일 압축 해제
5. 압축 해제한 폴더로 이동

---

## 🚀 수동 실행 방법

### 📌 방법 1: 명령 프롬프트 (CMD)

#### 1단계: 프로젝트 폴더로 이동

```cmd
cd C:\Users\사용자이름\Downloads\chungsan
```

> 💡 팁: 탐색기에서 폴더 열고 주소창에 `cmd` 입력하면 바로 CMD가 열립니다!

#### 2단계: 가상환경 생성

```cmd
python -m venv venv
```

#### 3단계: 가상환경 활성화

```cmd
venv\Scripts\activate
```

**활성화 확인:**
프롬프트 앞에 `(venv)`가 표시됩니다.
```cmd
(venv) C:\Users\사용자이름\Downloads\chungsan>
```

#### 4단계: 필요한 패키지 설치

```cmd
pip install -r requirements.txt
```

> ⏱️ 설치 시간: 약 1~2분 소요

#### 5단계: 서버 실행

```cmd
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

**실행 성공 메시지:**
```
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

### 📌 방법 2: PowerShell

#### 1단계: PowerShell 실행 정책 변경 (최초 1회만)

**관리자 권한으로 PowerShell 실행:**
1. 시작 메뉴에서 "PowerShell" 검색
2. 우클릭 → "관리자 권한으로 실행"
3. 다음 명령 실행:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 2단계: 프로젝트 폴더로 이동

```powershell
cd C:\Users\사용자이름\Downloads\chungsan
```

#### 3단계: 가상환경 생성

```powershell
python -m venv venv
```

#### 4단계: 가상환경 활성화

```powershell
.\venv\Scripts\Activate.ps1
```

**활성화 확인:**
```powershell
(venv) PS C:\Users\사용자이름\Downloads\chungsan>
```

#### 5단계: 필요한 패키지 설치

```powershell
pip install -r requirements.txt
```

#### 6단계: 서버 실행

```powershell
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

---

### 📌 방법 3: Git Bash (Git 설치된 경우)

#### 1단계: Git Bash 실행

탐색기에서 프로젝트 폴더 열고:
- 빈 공간에서 우클릭 → **Git Bash Here**

#### 2단계: 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/Scripts/activate
```

#### 3단계: 패키지 설치 및 실행

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

---

## ✅ 실행 확인

### 1️⃣ 브라우저에서 확인

#### API 문서 (Swagger UI)
```
http://localhost:8001/docs
```

#### API 문서 (ReDoc)
```
http://localhost:8001/redoc
```

#### Health Check
```
http://localhost:8001/health
```

### 2️⃣ 명령어로 확인

**새 CMD/PowerShell 창 열고:**

```cmd
curl http://localhost:8001/health
```

**응답:**
```json
{
  "status": "healthy",
  "service": "청산에사르리랏다"
}
```

---

## 🧪 테스트 API 호출

### 참여자 목록 조회

```cmd
curl http://localhost:8001/api/participants/
```

### 프로젝트 목록 조회

```cmd
curl http://localhost:8001/api/projects/
```

---

## 🛑 서버 종료

### CMD/PowerShell에서

```
Ctrl + C
```

### 가상환경 비활성화

```cmd
deactivate
```

---

## 🔧 문제 해결

### ❌ 문제 1: "python을 찾을 수 없습니다"

**해결 방법:**
1. Python 설치 확인: https://www.python.org/
2. 설치 시 **"Add Python to PATH"** 체크 필수!
3. 설치 후 CMD/PowerShell 재시작

### ❌ 문제 2: "venv\Scripts\activate를 실행할 수 없습니다"

**PowerShell 실행 정책 문제:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**또는 CMD 사용:**
```cmd
venv\Scripts\activate.bat
```

### ❌ 문제 3: "pip install이 실패합니다"

**해결 방법:**

```cmd
# pip 업그레이드
python -m pip install --upgrade pip

# 재시도
pip install -r requirements.txt
```

### ❌ 문제 4: "Port 8001 is already in use"

**포트가 이미 사용 중입니다.**

**방법 1: 다른 포트 사용**
```cmd
uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```

**방법 2: 사용 중인 프로세스 종료**
```cmd
# 포트 사용 프로세스 확인
netstat -ano | findstr :8001

# PID 확인 후 종료
taskkill /PID [PID번호] /F
```

### ❌ 문제 5: "ModuleNotFoundError: No module named 'fastapi'"

**가상환경이 활성화되지 않았습니다.**

```cmd
# 가상환경 활성화 확인
# 프롬프트 앞에 (venv)가 있어야 합니다
venv\Scripts\activate

# 패키지 재설치
pip install -r requirements.txt
```

---

## 📂 프로젝트 구조

```
chungsan/
├── 📄 main.py                    # FastAPI 앱
├── 📄 requirements.txt           # Python 패키지
├── 📄 chungsan.db               # SQLite 데이터베이스
├── 📁 app/
│   ├── 📄 __init__.py
│   ├── 📄 database.py           # DB 연결
│   ├── 📄 models.py             # 데이터 모델
│   ├── 📄 schemas.py            # API 스키마
│   └── 📁 routers/
│       ├── 📄 __init__.py
│       ├── 📄 participants.py   # 참여자 API
│       ├── 📄 projects.py       # 프로젝트 API
│       └── 📄 settlements.py    # 정산 API
├── 📁 venv/                     # 가상환경 (자동 생성)
├── 📁 uploads/                  # 업로드 파일
└── 📁 static/                   # 정적 파일
```

---

## 📊 실행 후 사용 방법

### 1️⃣ Swagger UI 사용

1. 브라우저에서 http://localhost:8001/docs 접속
2. API 엔드포인트 선택
3. **Try it out** 클릭
4. 파라미터 입력
5. **Execute** 클릭

### 2️⃣ 참여자 생성 예시

**Swagger UI에서:**
1. `POST /api/participants/` 선택
2. **Try it out** 클릭
3. Request body 입력:

```json
{
  "name": "홍길동",
  "role": "admin",
  "default_profit_rate": 30.0,
  "phone": "010-1234-5678",
  "bank_name": "국민은행",
  "account_number": "123-456-789012"
}
```

4. **Execute** 클릭

### 3️⃣ 정산 계산 예시

```json
{
  "project_id": 1
}
```

**응답:**
```json
{
  "project_id": 1,
  "project_name": "2024 교육 시스템 구축 프로젝트",
  "total_profit": 7000000.0,
  "settlements": [
    {
      "participant_id": 1,
      "participant_name": "김동혁",
      "participant_code": "HUMAN-001",
      "profit_rate": 30.0,
      "amount": 2100000.0
    }
  ]
}
```

---

## 🎯 빠른 시작 요약

### CMD (명령 프롬프트)

```cmd
# 1. 프로젝트 다운로드 및 이동
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan

# 2. 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8001 --reload

# 5. 브라우저에서 확인
# http://localhost:8001/docs
```

### PowerShell

```powershell
# 1. 실행 정책 변경 (최초 1회)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 2. 프로젝트 다운로드 및 이동
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan

# 3. 가상환경 생성 및 활성화
python -m venv venv
.\venv\Scripts\Activate.ps1

# 4. 패키지 설치
pip install -r requirements.txt

# 5. 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8001 --reload

# 6. 브라우저에서 확인
# http://localhost:8001/docs
```

---

## 📚 추가 자료

- **GitHub 저장소**: https://github.com/EmmettHwang/chungsan
- **API 문서**: http://localhost:8001/docs (서버 실행 후)
- **프로젝트 문서**:
  - `WINDOWS_SETUP.md` - 자동 실행 가이드
  - `WINDOWS_GIT_GUIDE.md` - Git 연동 가이드
  - `BACKEND_COMPLETE.md` - 백엔드 구현 상세
  - `LOCAL_SETUP_GUIDE.md` - 전체 설치 가이드

---

## 💡 유용한 팁

### 1️⃣ 자동 실행 스크립트 사용

**더 쉬운 방법이 있습니다!**

- **CMD**: `start-windows.bat` 더블클릭
- **PowerShell**: `start-windows.ps1` 우클릭 → PowerShell에서 실행

> 자세한 내용은 `WINDOWS_SETUP.md` 참고

### 2️⃣ 개발 모드

코드 수정 시 자동으로 서버가 재시작됩니다!

```cmd
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### 3️⃣ 로그 확인

서버 실행 중에 모든 API 요청이 콘솔에 표시됩니다.

```
INFO:     127.0.0.1:54321 - "GET /api/participants/ HTTP/1.1" 200 OK
```

### 4️⃣ 데이터베이스 초기화

데이터베이스를 처음부터 다시 만들고 싶다면:

```cmd
# 서버 종료 (Ctrl + C)
del chungsan.db
# 서버 재실행
```

---

## 🆘 도움이 필요하신가요?

### GitHub Issues
https://github.com/EmmettHwang/chungsan/issues

### 문의 사항
- 프로젝트 관련 문의는 GitHub Issues에 남겨주세요
- 버그 리포트도 환영합니다!

---

## 📅 변경 이력

- **2026-02-08**: 초기 버전 작성
  - CMD 실행 가이드
  - PowerShell 실행 가이드
  - Git Bash 실행 가이드
  - 문제 해결 가이드

---

**청산에사르리랏다 (Chungsan Settlement System)**  
**버전**: v1.0.0  
**GitHub**: https://github.com/EmmettHwang/chungsan  
**작성일**: 2026-02-08
