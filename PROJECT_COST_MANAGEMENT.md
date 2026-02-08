# 🎯 프로젝트 관리 개선 완료 보고서

## 📋 개선 내용

### 1. 원가 항목 상세 관리 기능 추가

#### 데이터베이스 모델
새로운 `ProjectCost` 모델 추가:
- **카테고리**: 
  - `server`: 서버 비용
  - `domain`: 도메인 비용
  - `ai_token`: AI 토큰 비용
  - `hardware`: 하드웨어 비용
  - `materials`: 잡자재 비용
  - `labor`: 인건비 (참여자 연결)
  - `other`: 기타

#### API 엔드포인트
- `GET /api/costs/project/{project_id}` - 프로젝트 원가 목록
- `GET /api/costs/{cost_id}` - 원가 항목 상세
- `POST /api/costs/` - 원가 항목 생성
- `PUT /api/costs/{cost_id}` - 원가 항목 수정
- `DELETE /api/costs/{cost_id}` - 원가 항목 삭제
- `GET /api/costs/project/{project_id}/total` - 총 원가 계산
- `GET /api/costs/project/{project_id}/category/{category}` - 카테고리별 조회

### 2. 프로젝트 모달 개선

#### 새로운 탭 추가 예정
- **원가 관리 탭**: 원가 항목 추가/수정/삭제

#### 기존 탭 구조
1. **기본 정보**: 프로젝트명, 클라이언트, 총액, 원가, 상태
2. **프로젝트 단계**: 10단계 날짜 입력
3. **참여자 선택**: 체크박스 + 수익률 설정
4. **진도 관리**: 진도 메모 + 자동 분석
5. **원가 관리** (신규): 원가 항목 관리

### 3. 참여자 자동 선택 기능

#### 계약일 기반 자동 선택
- 계약일(`contract_date`) 입력 시 자동으로 참여자 선택
- 참여자의 기본 수익률 자동 적용
- 수동으로 수정 가능

---

## 📊 데이터베이스 스키마

### project_costs 테이블

```sql
CREATE TABLE project_costs (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    project_id INTEGER NOT NULL,
    category VARCHAR(50) NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    amount FLOAT DEFAULT 0.0,
    participant_id INTEGER,  -- 인건비인 경우
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (participant_id) REFERENCES participants(id)
);
```

---

## 🔧 사용 예시

### 원가 항목 추가

#### 1. 서버 비용
```json
{
  "project_id": 1,
  "category": "server",
  "name": "AWS EC2 서버",
  "description": "t3.medium 인스턴스 3개월",
  "amount": 300000
}
```

#### 2. 도메인 비용
```json
{
  "project_id": 1,
  "category": "domain",
  "name": "example.com 도메인",
  "description": "1년 등록비",
  "amount": 15000
}
```

#### 3. AI 토큰 비용
```json
{
  "project_id": 1,
  "category": "ai_token",
  "name": "OpenAI GPT-4 API",
  "description": "개발 기간 사용량",
  "amount": 250000
}
```

#### 4. 하드웨어 비용
```json
{
  "project_id": 1,
  "category": "hardware",
  "name": "Raspberry Pi 4B 8GB",
  "description": "IoT 디바이스 5대",
  "amount": 500000
}
```

#### 5. 잡자재 비용
```json
{
  "project_id": 1,
  "category": "materials",
  "name": "케이블 및 부품",
  "description": "USB 케이블, 점퍼 와이어 등",
  "amount": 80000
}
```

#### 6. 인건비 (참여자 연결)
```json
{
  "project_id": 1,
  "category": "labor",
  "name": "홍길동 개발비",
  "description": "풀스택 개발 2개월",
  "amount": 8000000,
  "participant_id": 1
}
```

#### 7. 기타 비용
```json
{
  "project_id": 1,
  "category": "other",
  "name": "디자인 외주",
  "description": "UI/UX 디자인 작업",
  "amount": 1500000
}
```

---

## 🎨 프론트엔드 UI 개선 계획

### 원가 관리 탭 UI

```
┌─────────────────────────────────────────────────────────┐
│  원가 항목 관리                          [+ 항목 추가]  │
├─────────────────────────────────────────────────────────┤
│  카테고리별 원가 요약:                                  │
│  ├─ 서버 비용: 300,000원                               │
│  ├─ 도메인 비용: 15,000원                              │
│  ├─ AI 토큰 비용: 250,000원                            │
│  ├─ 하드웨어 비용: 500,000원                           │
│  ├─ 잡자재 비용: 80,000원                              │
│  ├─ 인건비: 16,000,000원                               │
│  └─ 기타: 1,500,000원                                  │
│                                                         │
│  총 원가: 18,645,000원                                 │
├─────────────────────────────────────────────────────────┤
│  상세 항목 목록:                                        │
│                                                         │
│  1. [서버] AWS EC2 서버 - 300,000원      [편집][삭제] │
│     설명: t3.medium 인스턴스 3개월                     │
│                                                         │
│  2. [도메인] example.com - 15,000원      [편집][삭제] │
│     설명: 1년 등록비                                   │
│                                                         │
│  3. [인건비] 홍길동 개발비 - 8,000,000원 [편집][삭제] │
│     담당자: 홍길동 (HUMAN-001)                        │
│     설명: 풀스택 개발 2개월                           │
│                                                         │
│  ... (더 많은 항목)                                    │
└─────────────────────────────────────────────────────────┘
```

### 원가 항목 추가 모달

```
┌─────────────────────────────────────────┐
│  원가 항목 추가                    [X]  │
├─────────────────────────────────────────┤
│  카테고리 *                             │
│  [서버 비용 ▼]                          │
│                                         │
│  항목명 *                               │
│  [_____________________________]        │
│                                         │
│  금액 (원) *                            │
│  [_____________________________]        │
│                                         │
│  담당자 (인건비인 경우)                  │
│  [참여자 선택 ▼]                        │
│                                         │
│  상세 설명                              │
│  [                             ]        │
│  [                             ]        │
│  [                             ]        │
│                                         │
│        [취소]          [저장]           │
└─────────────────────────────────────────┘
```

---

## 🚀 다음 단계

### Windows에서 실행

```bash
# 1. 최신 코드 받기
cd "G:\내 드라이브\11. DEV_23\51. Python_mp3등\chungsan\chungsan"
git pull origin main

# 2. 데이터베이스 업데이트 (새 테이블 생성)
python create_tables.py

# 3. 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8001 --reload

# 4. 브라우저 접속
# http://localhost:8001
```

### API 테스트

#### 원가 항목 추가 예시 (cURL)

```bash
# 서버 비용 추가
curl -X POST "http://localhost:8001/api/costs/" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": 1,
    "category": "server",
    "name": "AWS EC2 서버",
    "description": "t3.medium 3개월",
    "amount": 300000
  }'

# 인건비 추가 (참여자 연결)
curl -X POST "http://localhost:8001/api/costs/" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": 1,
    "category": "labor",
    "name": "홍길동 개발비",
    "description": "풀스택 개발 2개월",
    "amount": 8000000,
    "participant_id": 1
  }'

# 프로젝트 총 원가 조회
curl "http://localhost:8001/api/costs/project/1/total"
```

---

## ✅ 완료 체크리스트

### 백엔드
- [x] `ProjectCost` 모델 추가
- [x] `ProjectCostBase`, `ProjectCostCreate`, `ProjectCostUpdate` 스키마 추가
- [x] `crud_costs.py` CRUD 함수 구현
- [x] `routers/costs.py` API 라우터 추가
- [x] `main.py`에 라우터 등록
- [x] 데이터베이스 마이그레이션 준비

### 프론트엔드 (예정)
- [ ] 원가 관리 탭 UI 추가
- [ ] 원가 항목 추가/수정/삭제 기능
- [ ] 카테고리별 원가 요약 표시
- [ ] 인건비 참여자 자동 선택
- [ ] 총 원가 실시간 계산
- [ ] 계약일 기반 참여자 자동 선택

---

## 📚 파일 변경 내역

### 신규 파일
- `app/crud_costs.py` - 원가 CRUD 함수
- `app/routers/costs.py` - 원가 API 라우터
- `PROJECT_COST_MANAGEMENT.md` - 이 문서

### 수정 파일
- `app/models.py` - ProjectCost 모델 추가, Project.costs 관계 추가
- `app/schemas.py` - ProjectCost 스키마 추가
- `main.py` - costs 라우터 추가

---

## 🎯 주요 기능

### 1. 원가 카테고리별 관리
- 7가지 원가 카테고리 분류
- 카테고리별 합계 자동 계산
- 카테고리별 필터링 조회

### 2. 인건비 참여자 연결
- 인건비 항목은 참여자와 연결
- 참여자별 인건비 집계 가능
- 참여자 삭제 시 참조 관리

### 3. 프로젝트 원가 자동 계산
- 모든 원가 항목 자동 합산
- `projects.cost` 필드 자동 업데이트
- 순이익 자동 계산 (total_amount - cost)

### 4. 상세 설명 및 메모
- 각 원가 항목마다 상세 설명 추가
- 구매 날짜, 수량 등 상세 정보 기록

---

## 💡 활용 시나리오

### 시나리오 1: 웹 개발 프로젝트

**프로젝트**: "ABC 회사 홈페이지 제작"  
**총 계약금**: 15,000,000원

**원가 항목**:
1. AWS 서버 (3개월): 300,000원
2. 도메인 (1년): 15,000원
3. SSL 인증서: 50,000원
4. 디자인 외주: 1,500,000원
5. 홍길동 개발비: 6,000,000원
6. 이영희 기획비: 2,000,000원

**총 원가**: 9,865,000원  
**순이익**: 5,135,000원

### 시나리오 2: IoT 하드웨어 프로젝트

**프로젝트**: "스마트 홈 시스템 구축"  
**총 계약금**: 30,000,000원

**원가 항목**:
1. Raspberry Pi (10대): 1,000,000원
2. 센서 모듈 (50개): 2,500,000원
3. 케이블 및 부품: 500,000원
4. AWS IoT Core (6개월): 600,000원
5. OpenAI API (음성 인식): 300,000원
6. 박민수 하드웨어 개발: 8,000,000원
7. 최지영 소프트웨어 개발: 7,000,000원
8. 조립 인건비: 2,000,000원

**총 원가**: 21,900,000원  
**순이익**: 8,100,000원

---

## 🔗 관련 문서

- `DATABASE_INFO.md` - 데이터베이스 구조
- `FRONTEND_UPGRADE_COMPLETE.md` - 프론트엔드 가이드
- `LOCAL_MARIADB_SETUP.md` - 로컬 DB 설정
- `MYSQL_MIGRATION_GUIDE.md` - MySQL 전환 가이드

---

## 📞 API 사용 예시 (Python)

```python
import requests

BASE_URL = "http://localhost:8001"

# 1. 원가 항목 추가
cost_data = {
    "project_id": 1,
    "category": "server",
    "name": "AWS EC2",
    "amount": 300000,
    "description": "t3.medium 3개월"
}
response = requests.post(f"{BASE_URL}/api/costs/", json=cost_data)
print(response.json())

# 2. 프로젝트 원가 목록 조회
response = requests.get(f"{BASE_URL}/api/costs/project/1")
costs = response.json()
for cost in costs:
    print(f"{cost['category']}: {cost['name']} - {cost['amount']}원")

# 3. 총 원가 조회
response = requests.get(f"{BASE_URL}/api/costs/project/1/total")
total = response.json()
print(f"총 원가: {total['total_cost']}원")

# 4. 카테고리별 조회
response = requests.get(f"{BASE_URL}/api/costs/project/1/category/labor")
labor_costs = response.json()
print(f"인건비 항목: {len(labor_costs)}개")
```

---

## 🎉 완료!

프로젝트 원가 관리 시스템이 백엔드에 추가되었습니다!

**다음 단계**: 
1. Windows에서 `git pull` 및 `python create_tables.py` 실행
2. API 테스트
3. 프론트엔드 UI 추가 (다음 작업)

---

**버전**: v1.3.0  
**최종 업데이트**: 2026-02-08  
**작성자**: Claude (AI Assistant)
