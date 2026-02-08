# 📖 청산에사르리랏다 - 사용 예시 가이드

> **작성일**: 2026-02-08  
> **프로젝트**: 청산에사르리랏다 (Chungsan Settlement System)  
> **버전**: v1.0.0

---

## 📋 목차

1. [기본 사용 시나리오](#기본-사용-시나리오)
2. [참여자 관리](#참여자-관리)
3. [프로젝트 관리](#프로젝트-관리)
4. [정산 계산](#정산-계산)
5. [실전 예시](#실전-예시)

---

## 🎯 기본 사용 시나리오

### 전체 워크플로우

```
1. 참여자 등록
   ↓
2. 프로젝트 생성
   ↓
3. 프로젝트에 참여자 추가
   ↓
4. 정산 계산
   ↓
5. 결과 확인 및 정산
```

---

## 👥 참여자 관리

### 1️⃣ 참여자 생성

**API 엔드포인트:**
```
POST /api/participants/
```

**예시 1: 관리자 등록**

```json
{
  "name": "김동혁",
  "role": "admin",
  "default_profit_rate": 30.0,
  "phone": "010-1234-5678",
  "bank_name": "국민은행",
  "account_number": "123-456-789012",
  "email": "admin@example.com"
}
```

**응답:**
```json
{
  "id": 1,
  "code": "HUMAN-001",
  "name": "김동혁",
  "role": "admin",
  "default_profit_rate": 30.0,
  "phone": "010-1234-5678",
  "bank_name": "국민은행",
  "account_number": "123-456-789012",
  "email": "admin@example.com",
  "created_at": "2026-02-08T14:53:58.746784",
  "updated_at": "2026-02-08T14:53:58.746794"
}
```

**예시 2: 팀장 등록**

```json
{
  "name": "이수석",
  "role": "lead",
  "default_profit_rate": 25.0,
  "phone": "010-2345-6789",
  "bank_name": "신한은행",
  "account_number": "110-234-567890"
}
```

**예시 3: 선임 등록**

```json
{
  "name": "박선일",
  "role": "senior",
  "default_profit_rate": 20.0,
  "phone": "010-3456-7890",
  "bank_name": "우리은행",
  "account_number": "1002-345-678901"
}
```

**예시 4: 일반 멤버**

```json
{
  "name": "정정규",
  "role": "regular",
  "default_profit_rate": 15.0,
  "phone": "010-4567-8901",
  "bank_name": "하나은행",
  "account_number": "123-456789-01234"
}
```

**예시 5: 보조 멤버**

```json
{
  "name": "최보조",
  "role": "assistant",
  "default_profit_rate": 10.0,
  "phone": "010-5678-9012",
  "bank_name": "기업은행",
  "account_number": "123-456789-01"
}
```

### 2️⃣ 참여자 목록 조회

**API 엔드포인트:**
```
GET /api/participants/
```

**응답:**
```json
[
  {
    "id": 1,
    "code": "HUMAN-001",
    "name": "김동혁",
    "role": "admin",
    "default_profit_rate": 30.0
  },
  {
    "id": 2,
    "code": "HUMAN-002",
    "name": "이수석",
    "role": "lead",
    "default_profit_rate": 25.0
  }
]
```

### 3️⃣ 특정 참여자 조회

**API 엔드포인트:**
```
GET /api/participants/1
```

**응답:**
```json
{
  "id": 1,
  "code": "HUMAN-001",
  "name": "김동혁",
  "role": "admin",
  "default_profit_rate": 30.0,
  "phone": "010-1234-5678",
  "bank_name": "국민은행",
  "account_number": "123-456-789012"
}
```

### 4️⃣ 참여자 정보 수정

**API 엔드포인트:**
```
PUT /api/participants/1
```

**요청:**
```json
{
  "name": "김동혁",
  "role": "admin",
  "default_profit_rate": 35.0,
  "phone": "010-1234-5678",
  "bank_name": "국민은행",
  "account_number": "123-456-789012"
}
```

### 5️⃣ 참여자 삭제

**API 엔드포인트:**
```
DELETE /api/participants/1
```

**응답:**
```json
{
  "message": "참여자가 삭제되었습니다"
}
```

---

## 📁 프로젝트 관리

### 1️⃣ 프로젝트 생성

**API 엔드포인트:**
```
POST /api/projects/
```

**예시 1: 교육 시스템 프로젝트**

```json
{
  "name": "2024 교육 시스템 구축 프로젝트",
  "client": "우송대학교",
  "total_amount": 10000000,
  "cost": 3000000,
  "status": "completed",
  "start_date": "2024-01-01",
  "end_date": "2024-12-31"
}
```

**응답:**
```json
{
  "id": 1,
  "name": "2024 교육 시스템 구축 프로젝트",
  "client": "우송대학교",
  "total_amount": 10000000.0,
  "cost": 3000000.0,
  "profit": 7000000.0,
  "status": "completed",
  "start_date": "2024-01-01",
  "end_date": "2024-12-31",
  "created_at": "2026-02-08T14:54:19.861691",
  "updated_at": "2026-02-08T14:54:19.861700"
}
```

**예시 2: 웹사이트 제작 프로젝트**

```json
{
  "name": "기업 홈페이지 리뉴얼",
  "client": "ABC기업",
  "total_amount": 5000000,
  "cost": 1500000,
  "status": "in_progress",
  "start_date": "2024-02-01",
  "end_date": "2024-04-30"
}
```

**예시 3: 컨설팅 프로젝트**

```json
{
  "name": "디지털 전환 컨설팅",
  "client": "XYZ그룹",
  "total_amount": 20000000,
  "cost": 5000000,
  "status": "planning",
  "notes": "6개월 장기 프로젝트"
}
```

### 2️⃣ 프로젝트 목록 조회

**API 엔드포인트:**
```
GET /api/projects/
```

**응답:**
```json
[
  {
    "id": 1,
    "name": "2024 교육 시스템 구축 프로젝트",
    "client": "우송대학교",
    "total_amount": 10000000.0,
    "cost": 3000000.0,
    "profit": 7000000.0,
    "status": "completed"
  }
]
```

### 3️⃣ 프로젝트에 참여자 추가

**API 엔드포인트:**
```
POST /api/projects/1/participants
```

**예시 1: 기본 수익률로 추가**

```json
{
  "participant_id": 1
}
```

**응답:**
```json
{
  "message": "참여자가 추가되었습니다",
  "profit_rate": 30.0
}
```

**예시 2: 커스텀 수익률로 추가**

```json
{
  "participant_id": 2,
  "profit_rate": 20.0
}
```

**응답:**
```json
{
  "message": "참여자가 추가되었습니다",
  "profit_rate": 20.0
}
```

### 4️⃣ 프로젝트 참여자 목록 조회

**API 엔드포인트:**
```
GET /api/projects/1/participants
```

**응답:**
```json
[
  {
    "participant_id": 1,
    "participant_name": "김동혁",
    "participant_code": "HUMAN-001",
    "participant_role": "admin",
    "profit_rate": 30.0,
    "joined_at": "2026-02-08T14:54:50"
  },
  {
    "participant_id": 2,
    "participant_name": "이수석",
    "participant_code": "HUMAN-002",
    "participant_role": "lead",
    "profit_rate": 25.0,
    "joined_at": "2026-02-08T14:54:51"
  }
]
```

### 5️⃣ 참여자 수익률 수정

**API 엔드포인트:**
```
PUT /api/projects/1/participants/2
```

**요청:**
```json
{
  "profit_rate": 22.0
}
```

**응답:**
```json
{
  "message": "수익률이 업데이트되었습니다",
  "profit_rate": 22.0
}
```

### 6️⃣ 프로젝트에서 참여자 제거

**API 엔드포인트:**
```
DELETE /api/projects/1/participants/2
```

**응답:**
```json
{
  "message": "참여자가 프로젝트에서 제거되었습니다"
}
```

---

## 💰 정산 계산

### 1️⃣ 정산 계산 실행

**API 엔드포인트:**
```
POST /api/settlements/calculate
```

**요청:**
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
    },
    {
      "participant_id": 2,
      "participant_name": "이수석",
      "participant_code": "HUMAN-002",
      "profit_rate": 25.0,
      "amount": 1750000.0
    },
    {
      "participant_id": 3,
      "participant_name": "박선일",
      "participant_code": "HUMAN-003",
      "profit_rate": 20.0,
      "amount": 1400000.0
    },
    {
      "participant_id": 4,
      "participant_name": "정정규",
      "participant_code": "HUMAN-004",
      "profit_rate": 15.0,
      "amount": 1050000.0
    },
    {
      "participant_id": 5,
      "participant_name": "최보조",
      "participant_code": "HUMAN-005",
      "profit_rate": 10.0,
      "amount": 700000.0
    }
  ]
}
```

### 2️⃣ 정산 내역 저장 (향후 기능)

정산 계산 결과를 데이터베이스에 저장할 수 있습니다.

---

## 🎬 실전 예시

### 시나리오: 새 프로젝트 정산하기

#### 1단계: 팀원 등록

```bash
# 1. 프로젝트 리더 등록
curl -X POST http://localhost:8001/api/participants/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "김팀장",
    "role": "lead",
    "default_profit_rate": 35.0,
    "phone": "010-1111-2222",
    "bank_name": "국민은행",
    "account_number": "123-456-789"
  }'

# 2. 선임 개발자 등록
curl -X POST http://localhost:8001/api/participants/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "박선임",
    "role": "senior",
    "default_profit_rate": 30.0,
    "phone": "010-2222-3333",
    "bank_name": "신한은행",
    "account_number": "110-234-567"
  }'

# 3. 주니어 개발자 등록
curl -X POST http://localhost:8001/api/participants/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "이주니어",
    "role": "regular",
    "default_profit_rate": 20.0,
    "phone": "010-3333-4444",
    "bank_name": "우리은행",
    "account_number": "1002-345-678"
  }'

# 4. 디자이너 등록
curl -X POST http://localhost:8001/api/participants/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "최디자인",
    "role": "regular",
    "default_profit_rate": 15.0,
    "phone": "010-4444-5555",
    "bank_name": "하나은행",
    "account_number": "123-456-789"
  }'
```

#### 2단계: 프로젝트 생성

```bash
curl -X POST http://localhost:8001/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "쇼핑몰 웹사이트 개발",
    "client": "스타트업 A사",
    "total_amount": 30000000,
    "cost": 8000000,
    "status": "completed",
    "start_date": "2024-01-01",
    "end_date": "2024-03-31"
  }'
```

#### 3단계: 참여자 추가

```bash
# 프로젝트 ID가 1이라고 가정

# 1. 팀장 추가 (ID: 1)
curl -X POST http://localhost:8001/api/projects/1/participants \
  -H "Content-Type: application/json" \
  -d '{"participant_id": 1}'

# 2. 선임 추가 (ID: 2)
curl -X POST http://localhost:8001/api/projects/1/participants \
  -H "Content-Type: application/json" \
  -d '{"participant_id": 2}'

# 3. 주니어 추가 (ID: 3)
curl -X POST http://localhost:8001/api/projects/1/participants \
  -H "Content-Type: application/json" \
  -d '{"participant_id": 3}'

# 4. 디자이너 추가 (ID: 4)
curl -X POST http://localhost:8001/api/projects/1/participants \
  -H "Content-Type: application/json" \
  -d '{"participant_id": 4}'
```

#### 4단계: 정산 계산

```bash
curl -X POST http://localhost:8001/api/settlements/calculate \
  -H "Content-Type: application/json" \
  -d '{"project_id": 1}'
```

**예상 결과:**

```
총 수익: 30,000,000원
원가: 8,000,000원
순이익: 22,000,000원

정산 내역:
- 김팀장 (35%): 7,700,000원
- 박선임 (30%): 6,600,000원
- 이주니어 (20%): 4,400,000원
- 최디자인 (15%): 3,300,000원
합계: 22,000,000원 ✓
```

---

## 📊 응용 시나리오

### 시나리오 1: 프로젝트별 커스텀 수익률

어떤 프로젝트에서는 특정 멤버의 기여도가 높아서 수익률을 조정하고 싶을 때:

```bash
# 주니어 개발자의 이번 프로젝트 수익률을 25%로 상향
curl -X PUT http://localhost:8001/api/projects/1/participants/3 \
  -H "Content-Type: application/json" \
  -d '{"profit_rate": 25.0}'
```

### 시나리오 2: 중간에 참여자 변경

프로젝트 진행 중 팀원이 바뀔 때:

```bash
# 1. 기존 멤버 제거
curl -X DELETE http://localhost:8001/api/projects/1/participants/4

# 2. 새 멤버 추가
curl -X POST http://localhost:8001/api/projects/1/participants \
  -H "Content-Type: application/json" \
  -d '{"participant_id": 5, "profit_rate": 15.0}'
```

### 시나리오 3: 여러 프로젝트 동시 관리

```bash
# 프로젝트 A
curl -X POST http://localhost:8001/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "프로젝트 A",
    "client": "클라이언트 A",
    "total_amount": 10000000,
    "cost": 3000000
  }'

# 프로젝트 B
curl -X POST http://localhost:8001/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "프로젝트 B",
    "client": "클라이언트 B",
    "total_amount": 15000000,
    "cost": 4000000
  }'

# 각 프로젝트별로 참여자 추가 및 정산
```

---

## 🔢 수익률 계산 로직

### 기본 계산식

```
순이익 = 총액 - 원가
개인 정산 금액 = 순이익 × (개인 수익률 / 전체 수익률 합계)
```

### 예시

**프로젝트 정보:**
- 총액: 10,000,000원
- 원가: 3,000,000원
- 순이익: 7,000,000원

**참여자:**
- A (30%)
- B (25%)
- C (20%)
- D (15%)
- E (10%)
- **합계: 100%**

**계산:**
- A: 7,000,000 × 30% = 2,100,000원
- B: 7,000,000 × 25% = 1,750,000원
- C: 7,000,000 × 20% = 1,400,000원
- D: 7,000,000 × 15% = 1,050,000원
- E: 7,000,000 × 10% = 700,000원

---

## 💡 유용한 팁

### 1️⃣ 역할별 기본 수익률 가이드

```
admin     : 30% - 35% (프로젝트 총괄)
lead      : 25% - 30% (팀장급)
senior    : 20% - 25% (선임급)
regular   : 15% - 20% (일반 멤버)
assistant : 10% - 15% (보조 멤버)
```

### 2️⃣ 수익률 합계가 100%를 초과해도 됩니다!

시스템은 비율에 따라 자동으로 계산하므로:
- 합계 150%라면: A(30%) → 실제 20%, B(45%) → 실제 30%

### 3️⃣ 프로젝트 상태 관리

```
planning    : 기획 단계
in_progress : 진행 중
completed   : 완료
cancelled   : 취소
```

---

## 📚 추가 자료

- **API 문서**: http://localhost:8001/docs
- **GitHub**: https://github.com/EmmettHwang/chungsan
- **설치 가이드**: `MANUAL_SETUP.md`
- **Git 연동**: `WINDOWS_GIT_GUIDE.md`

---

**청산에사르리랏다 (Chungsan Settlement System)**  
**버전**: v1.0.0  
**작성일**: 2026-02-08
