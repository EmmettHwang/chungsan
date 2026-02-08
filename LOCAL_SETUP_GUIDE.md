# 청산에사르리랏다 - 로컬 실행 가이드

## 📥 다운로드 방법

### 방법 1: Git Clone (권장)
```bash
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan
```

### 방법 2: ZIP 다운로드
1. GitHub 페이지 방문: https://github.com/EmmettHwang/chungsan
2. **Code** 버튼 클릭
3. **Download ZIP** 선택
4. 압축 해제 후 폴더로 이동

---

## 🛠 필수 설치 프로그램

- **Python 3.8+** → https://www.python.org/
- **MySQL** → https://dev.mysql.com/downloads/
- **Git** → https://git-scm.com/

---

## 🚀 로컬 실행 순서

### 1️⃣ Python 가상환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 2️⃣ 백엔드 패키지 설치

```bash
cd backend
pip install -r requirements.txt
```

### 3️⃣ 환경 변수 설정

`backend/.env` 파일을 생성하고 아래 내용을 입력하세요:

```env
# 데이터베이스 설정
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=minilms

# AI API 키 (선택사항)
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

# 서버 설정
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=development

# RAG 설정
VECTOR_DB_PATH=./vector_db
DOCUMENTS_PATH=./documents
UPLOADS_PATH=./uploads
```

> 💡 `.env.example` 파일을 복사해서 사용할 수도 있습니다:
> ```bash
> cp .env.example .env
> ```

### 4️⃣ 데이터베이스 생성

MySQL에 접속해서 데이터베이스를 생성하세요:

```sql
CREATE DATABASE minilms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

또는 MySQL 명령줄에서:

```bash
mysql -u root -p -e "CREATE DATABASE minilms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

### 5️⃣ 백엔드 서버 실행

```bash
cd backend
uvicorn main:app --reload --port 8000
```

✅ **백엔드 서버**: http://localhost:8000  
📖 **API 문서**: http://localhost:8000/docs  
📊 **대체 API 문서**: http://localhost:8000/redoc

### 6️⃣ 프론트엔드 실행 (새 터미널)

```bash
cd frontend

# Python HTTP 서버 사용
python -m http.server 3000

# 또는 Node.js http-server 사용
npx http-server -p 3000
```

✅ **프론트엔드**: http://localhost:3000

---

## ⚡ 빠른 시작 (All-in-One)

### Windows
```cmd
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan
python -m venv venv
venv\Scripts\activate
cd backend
pip install -r requirements.txt
copy .env.example .env
notepad .env
REM .env 파일 수정 후 저장
uvicorn main:app --reload --port 8000
```

### macOS/Linux
```bash
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan
python -m venv venv
source venv/bin/activate
cd backend
pip install -r requirements.txt
cp .env.example .env
nano .env
# .env 파일 수정 후 저장 (Ctrl+X, Y, Enter)
uvicorn main:app --reload --port 8000
```

---

## 🔧 트러블슈팅

### ❌ MySQL 연결 실패
```
Error: Can't connect to MySQL server
```

**해결방법:**
1. MySQL 서비스가 실행 중인지 확인
   ```bash
   # Windows
   net start MySQL80
   
   # macOS
   brew services start mysql
   
   # Linux
   sudo systemctl start mysql
   ```

2. `.env` 파일의 데이터베이스 정보 확인
3. 데이터베이스가 생성되었는지 확인
   ```bash
   mysql -u root -p -e "SHOW DATABASES;"
   ```

### ❌ 패키지 설치 실패
```
Error: Could not install packages
```

**해결방법:**
```bash
# Python 버전 확인 (3.8 이상 필요)
python --version

# pip 업그레이드
pip install --upgrade pip

# 패키지 재설치
pip install -r requirements.txt
```

### ❌ 포트 충돌
```
Error: Address already in use
```

**해결방법:**
```bash
# 다른 포트로 실행
uvicorn main:app --port 8001

# 또는 사용 중인 프로세스 종료 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID번호> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### ❌ 가상환경 활성화 안됨 (Windows PowerShell)
```
Error: Execution Policy
```

**해결방법:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📦 프로젝트 구조

```
chungsan/
├── backend/              # FastAPI 백엔드
│   ├── main.py          # 메인 API 서버 (455KB)
│   ├── extended_api.py  # 확장 API
│   ├── requirements.txt # Python 패키지 목록
│   ├── .env            # 환경 변수 (생성 필요)
│   ├── .env.example    # 환경 변수 템플릿
│   ├── rag/            # RAG 시스템
│   │   ├── vector_store.py
│   │   ├── document_loader.py
│   │   └── rag_chain.py
│   ├── documents/      # RAG 문서 저장
│   ├── uploads/        # 업로드 파일
│   └── backups/        # 백업 파일
│
├── frontend/            # Vanilla JS 프론트엔드
│   ├── index.html      # 관리자 메인 페이지
│   ├── app.js          # 메인 JavaScript (1.4MB)
│   ├── login.html      # 로그인 페이지
│   ├── register.html   # 회원가입 페이지
│   ├── student.html    # 학생 페이지
│   ├── course-intro.html
│   ├── education-support.html
│   └── aesong-chatbot.js
│
├── public/             # 정적 리소스
│   ├── images/
│   ├── fonts/
│   └── 3d-models/
│
├── migrations/         # 데이터베이스 마이그레이션
├── documents/          # 문서
├── seed.sql           # 초기 데이터
│
├── .claude            # 프로젝트 설정
├── welcome.sh         # 시스템 상태 확인 스크립트
├── bump-version.sh    # 버전 업데이트 스크립트
├── deploy-cafe24.sh   # Cafe24 배포 스크립트
│
├── README.md          # 프로젝트 소개
├── SERVER_INFO.md     # 서버 정보
├── SETUP_COMPLETE.md  # 설정 완료 보고서
└── PERMISSION_SYSTEM_IMPROVEMENT.md  # 권한 시스템 개선 문서
```

---

## 🎯 개발 모드 주요 기능

### 1. 시스템 상태 확인
```bash
./welcome.sh
```

출력 예시:
```
🎉 청산에사르리랏다 (Chungsan Settlement System) 🎉
현재 버전: v5.6.9.202602061800

📊 Git 상태:
   브랜치: main
   상태: Clean
   마지막 커밋: da81b1e - feat: Cafe24 서버 배포 스크립트 추가

🖥️  시스템 상태:
   ✅ 백엔드 서버: 실행 중 (포트 8000)
   ✅ 디스크 사용량: 24%
```

### 2. 버전 업데이트
```bash
./bump-version.sh
```

자동으로 수행:
- 버전 번호 증가 (v5.6.9 → v5.6.10)
- README.md 업데이트
- 캐시 버스팅 (app.js, service-worker.js)
- Git 커밋 및 푸시
- main 브랜치 병합
- 작업 브랜치로 복귀

### 3. API 문서 확인
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 4. 데이터베이스 초기화
```bash
cd backend
mysql -u root -p minilms < ../seed.sql
```

---

## 🌐 접속 URL 정리

| 서비스 | URL | 설명 |
|--------|-----|------|
| **백엔드 API** | http://localhost:8000 | FastAPI 서버 |
| **API 문서** | http://localhost:8000/docs | Swagger UI |
| **대체 API 문서** | http://localhost:8000/redoc | ReDoc |
| **프론트엔드** | http://localhost:3000 | 관리자 페이지 |
| **로그인** | http://localhost:3000/login.html | 로그인 페이지 |
| **학생 페이지** | http://localhost:3000/student.html | 학생용 페이지 |

---

## 🔑 기본 로그인 정보

```
관리자 계정:
ID: admin
Password: (서버 설정 확인)

강사 계정:
ID: instructor
Password: (서버 설정 확인)
```

---

## 📝 개발 가이드

### Git 커밋 규칙
```bash
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
style: 코드 포맷팅
refactor: 코드 리팩토링
test: 테스트 코드
chore: 빌드 및 설정
```

### 브랜치 전략
- `main`: 프로덕션 브랜치
- `develop`: 개발 브랜치
- `feature/*`: 기능 개발 브랜치
- `hotfix/*`: 긴급 수정 브랜치

### 유용한 명령어
```bash
# Git 상태 확인
git status

# 최신 코드 가져오기
git pull origin main

# 변경사항 커밋
git add .
git commit -m "feat: 새 기능 추가"
git push origin main

# 브랜치 목록
git branch -a

# 백엔드 로그 확인
tail -f backend/logs/app.log

# MySQL 접속
mysql -u root -p minilms
```

---

## 🚀 프로덕션 배포

Cafe24 서버 배포는 **SERVER_INFO.md** 파일을 참고하세요.

```bash
./deploy-cafe24.sh
```

---

## 📞 지원 및 문의

- **GitHub**: https://github.com/EmmettHwang/chungsan
- **Issues**: https://github.com/EmmettHwang/chungsan/issues
- **Wiki**: https://github.com/EmmettHwang/chungsan/wiki

---

## 📄 관련 문서

- [README.md](README.md) - 프로젝트 개요
- [SERVER_INFO.md](SERVER_INFO.md) - 서버 정보 및 배포
- [SETUP_COMPLETE.md](SETUP_COMPLETE.md) - 설정 완료 보고서
- [PERMISSION_SYSTEM_IMPROVEMENT.md](PERMISSION_SYSTEM_IMPROVEMENT.md) - 권한 시스템 개선
- [.claude](.claude) - 프로젝트 워크플로우

---

**🎉 로컬 개발 환경 설정 완료!**

문제가 발생하면 위 **트러블슈팅** 섹션을 참고하거나 GitHub Issues에 문의하세요.
