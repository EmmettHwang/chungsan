# ⚡ 청산에사르리랏다 - 빠른 시작 가이드 (5분 완성)

> **작성일**: 2026-02-08  
> **프로젝트**: 청산에사르리랏다 (Chungsan Settlement System)  
> **버전**: v1.0.0

---

## 🎯 5분 안에 시작하기

### Windows 사용자

#### 1️⃣ 다운로드

**GitHub에서 ZIP 다운로드:**
https://github.com/EmmettHwang/chungsan

→ **Code** 버튼 → **Download ZIP**

#### 2️⃣ 압축 해제

다운로드한 `chungsan-main.zip` 압축 해제

#### 3️⃣ 폴더 열기

압축 해제한 `chungsan-main` 폴더 열기

#### 4️⃣ 실행 (CMD)

폴더 안에서:
1. `Shift` + 우클릭 → "여기서 PowerShell 창 열기" 또는
2. 주소창에 `cmd` 입력

다음 명령 실행:

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

#### 5️⃣ 확인

브라우저에서:
```
http://localhost:8001/docs
```

**완료! 🎉**

---

## 📋 한 번에 복사하기

### CMD (명령 프롬프트)

```cmd
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### PowerShell

```powershell
python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### Git Bash

```bash
python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

---

## 🚀 첫 API 테스트 (Swagger UI)

### 1️⃣ 브라우저에서 접속

```
http://localhost:8001/docs
```

### 2️⃣ 참여자 생성

1. **POST /api/participants/** 클릭
2. **Try it out** 클릭
3. 다음 JSON 입력:

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

### 3️⃣ 프로젝트 생성

1. **POST /api/projects/** 클릭
2. **Try it out** 클릭
3. 다음 JSON 입력:

```json
{
  "name": "테스트 프로젝트",
  "client": "테스트 고객",
  "total_amount": 10000000,
  "cost": 3000000,
  "status": "completed"
}
```

4. **Execute** 클릭

### 4️⃣ 프로젝트에 참여자 추가

1. **POST /api/projects/1/participants** 클릭
2. **Try it out** 클릭
3. 다음 JSON 입력:

```json
{
  "participant_id": 1
}
```

4. **Execute** 클릭

### 5️⃣ 정산 계산

1. **POST /api/settlements/calculate** 클릭
2. **Try it out** 클릭
3. 다음 JSON 입력:

```json
{
  "project_id": 1
}
```

4. **Execute** 클릭

**결과 확인:**
```json
{
  "project_id": 1,
  "project_name": "테스트 프로젝트",
  "total_profit": 7000000.0,
  "settlements": [
    {
      "participant_id": 1,
      "participant_name": "홍길동",
      "participant_code": "HUMAN-001",
      "profit_rate": 30.0,
      "amount": 2100000.0
    }
  ]
}
```

**완료! 정산이 계산되었습니다! 🎉**

---

## 📱 curl로 테스트 (고급)

### 새 CMD/PowerShell 창 열고:

```bash
# 1. 참여자 생성
curl -X POST http://localhost:8001/api/participants/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"홍길동\",\"role\":\"admin\",\"default_profit_rate\":30.0,\"phone\":\"010-1234-5678\",\"bank_name\":\"국민은행\",\"account_number\":\"123-456-789012\"}"

# 2. 프로젝트 생성
curl -X POST http://localhost:8001/api/projects/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"테스트 프로젝트\",\"client\":\"테스트 고객\",\"total_amount\":10000000,\"cost\":3000000,\"status\":\"completed\"}"

# 3. 참여자 추가
curl -X POST http://localhost:8001/api/projects/1/participants ^
  -H "Content-Type: application/json" ^
  -d "{\"participant_id\":1}"

# 4. 정산 계산
curl -X POST http://localhost:8001/api/settlements/calculate ^
  -H "Content-Type: application/json" ^
  -d "{\"project_id\":1}"
```

---

## 🎓 튜토리얼: 실전 시나리오

### 시나리오: 5명의 팀으로 프로젝트 정산하기

#### 1단계: 팀원 5명 등록

**Swagger UI에서 POST /api/participants/ 5번 실행:**

```json
{"name":"김팀장","role":"lead","default_profit_rate":30.0,"phone":"010-1111-1111","bank_name":"국민은행","account_number":"123-456-789"}
{"name":"이선임","role":"senior","default_profit_rate":25.0,"phone":"010-2222-2222","bank_name":"신한은행","account_number":"110-234-567"}
{"name":"박주임","role":"regular","default_profit_rate":20.0,"phone":"010-3333-3333","bank_name":"우리은행","account_number":"1002-345-678"}
{"name":"최사원","role":"regular","default_profit_rate":15.0,"phone":"010-4444-4444","bank_name":"하나은행","account_number":"123-456-789"}
{"name":"정인턴","role":"assistant","default_profit_rate":10.0,"phone":"010-5555-5555","bank_name":"기업은행","account_number":"123-456-789"}
```

#### 2단계: 프로젝트 생성

```json
{
  "name": "웹사이트 리뉴얼 프로젝트",
  "client": "ABC기업",
  "total_amount": 20000000,
  "cost": 5000000,
  "status": "completed",
  "start_date": "2024-01-01",
  "end_date": "2024-03-31"
}
```

#### 3단계: 참여자 5명 추가

**POST /api/projects/1/participants 5번 실행:**

```json
{"participant_id": 1}
{"participant_id": 2}
{"participant_id": 3}
{"participant_id": 4}
{"participant_id": 5}
```

#### 4단계: 정산 계산

```json
{"project_id": 1}
```

#### 예상 결과:

```
총액: 20,000,000원
원가: 5,000,000원
순이익: 15,000,000원

정산:
- 김팀장 (30%): 4,500,000원
- 이선임 (25%): 3,750,000원
- 박주임 (20%): 3,000,000원
- 최사원 (15%): 2,250,000원
- 정인턴 (10%): 1,500,000원
합계: 15,000,000원 ✓
```

---

## 🔥 자주 묻는 질문 (FAQ)

### Q1: Python이 설치되어 있는지 확인하려면?

```cmd
python --version
```

출력 예시: `Python 3.11.5`

### Q2: 가상환경이 활성화되었는지 확인하려면?

프롬프트 앞에 `(venv)`가 표시되어야 합니다:
```
(venv) C:\Users\user\chungsan>
```

### Q3: 서버가 실행 중인지 확인하려면?

새 CMD 창에서:
```cmd
curl http://localhost:8001/health
```

응답:
```json
{"status":"healthy","service":"청산에사르리랏다"}
```

### Q4: 포트 8001이 이미 사용 중이라면?

다른 포트 사용:
```cmd
uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```

그리고 http://localhost:8002/docs 접속

### Q5: 데이터를 초기화하고 싶다면?

```cmd
# 서버 종료 (Ctrl + C)
del chungsan.db
# 서버 재실행
```

---

## 🛑 서버 종료

### 방법 1: 키보드

```
Ctrl + C
```

### 방법 2: 가상환경 비활성화

```cmd
deactivate
```

---

## 📚 다음 단계

이제 기본 사용법을 익혔다면:

1. **상세 가이드 읽기**
   - `MANUAL_SETUP.md` - 수동 설정 상세
   - `USAGE_EXAMPLES.md` - 사용 예시

2. **Git 연동하기**
   - `WINDOWS_GIT_GUIDE.md` - GitHub 연동

3. **프론트엔드 개발**
   - UI 페이지 만들기
   - 대시보드 구현

4. **배포하기**
   - 프로덕션 서버 설정
   - 도메인 연결

---

## 🆘 문제가 발생했나요?

### 1. Python이 없다면?
https://www.python.org/downloads/

### 2. 가상환경 활성화 실패?
PowerShell 실행 정책:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. pip install 실패?
```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. 포트 충돌?
```cmd
netstat -ano | findstr :8001
taskkill /PID [PID번호] /F
```

---

## 🎉 축하합니다!

이제 청산에사르리랏다를 사용할 준비가 완료되었습니다!

### 접속 URL

- **API 문서**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc
- **Health Check**: http://localhost:8001/health

### 주요 API 엔드포인트

- `GET /api/participants/` - 참여자 목록
- `POST /api/participants/` - 참여자 생성
- `GET /api/projects/` - 프로젝트 목록
- `POST /api/projects/` - 프로젝트 생성
- `POST /api/settlements/calculate` - 정산 계산

---

## 📖 추가 자료

- **GitHub**: https://github.com/EmmettHwang/chungsan
- **Issues**: https://github.com/EmmettHwang/chungsan/issues
- **문서**:
  - `README.md` - 프로젝트 소개
  - `MANUAL_SETUP.md` - 수동 설치
  - `USAGE_EXAMPLES.md` - 사용 예시
  - `WINDOWS_GIT_GUIDE.md` - Git 연동

---

**청산에사르리랏다 (Chungsan Settlement System)**  
**버전**: v1.0.0  
**작성일**: 2026-02-08

**Happy Coding! 🚀**
