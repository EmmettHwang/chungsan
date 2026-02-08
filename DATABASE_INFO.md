# 💾 청산에사르리랏다 - 데이터베이스 정보

## 📊 현재 사용 중인 데이터베이스

### 기본 정보
```
데이터베이스: SQLite
버전: 3.40.1
파일명: chungsan.db
크기: 52.00 KB
경로: /home/user/webapp/chungsan.db
백업: chungsan.db.backup (52.00 KB)
```

### 연결 설정
```python
# app/database.py
SQLALCHEMY_DATABASE_URL = "sqlite:///./chungsan.db"

# 환경변수로 변경 가능
# DATABASE_URL=sqlite:///./chungsan.db
# DATABASE_URL=postgresql://user:password@localhost/dbname
```

---

## 🗄️ 데이터베이스 구조

### 테이블 목록 (5개)

#### 1. **participants** (참여자)
프로젝트 참여자 정보를 저장하는 테이블

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| id | INTEGER (PK) | 참여자 ID |
| code | VARCHAR (NOT NULL) | 참여자 코드 (예: HUMAN-001) |
| name | VARCHAR (NOT NULL) | 이름 |
| role | VARCHAR | 역할 (admin, lead, senior, regular, assistant) |
| default_profit_rate | FLOAT | 기본 수익률 (%) |
| phone | VARCHAR | 전화번호 |
| email | VARCHAR | 이메일 |
| bank_name | VARCHAR | 은행명 |
| account_number | VARCHAR | 계좌번호 |
| id_card_path | VARCHAR | 신분증 파일 경로 |
| bankbook_path | VARCHAR | 통장 사본 파일 경로 |
| notes | TEXT | 메모 |
| created_at | DATETIME | 생성일시 |
| updated_at | DATETIME | 수정일시 |

**현재 레코드 수**: 0개

---

#### 2. **projects** (프로젝트)
프로젝트 정보 및 진도 관리

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| id | INTEGER (PK) | 프로젝트 ID |
| name | VARCHAR (NOT NULL) | 프로젝트명 |
| client | VARCHAR | 클라이언트명 |
| total_amount | FLOAT | 총액 (원) |
| cost | FLOAT | 원가 (원) |
| profit | FLOAT | 순이익 (원) |
| status | VARCHAR | 상태 (planning, in_progress, completed, cancelled) |
| **10단계 날짜 필드** | | |
| idea_date | DATETIME | 1. 아이디어 날짜 |
| introduction_date | DATETIME | 2. 소개 날짜 |
| consultation_date | DATETIME | 3. 상담 날짜 |
| quote_date | DATETIME | 4. 견적 날짜 |
| contract_date | DATETIME | 5. 계약 날짜 |
| development_date | DATETIME | 6. 개발 날짜 |
| test_date | DATETIME | 7. 테스트 날짜 |
| delivery_date | DATETIME | 8. 납품 날짜 |
| completion_date | DATETIME | 9. 완료 날짜 |
| maintenance_date | DATETIME | 10. 유지보수 날짜 |
| **기타 필드** | | |
| start_date | DATETIME | 시작일 |
| end_date | DATETIME | 종료일 |
| notes | TEXT | 메모 |
| **진도 관리 필드** | | |
| progress_notes | TEXT | 진도 메모 |
| progress_rate | FLOAT | 진도율 (0-100) |
| current_stage | VARCHAR | 현재 단계 |
| created_at | DATETIME | 생성일시 |
| updated_at | DATETIME | 수정일시 |

**현재 레코드 수**: 0개

---

#### 3. **project_participants** (프로젝트-참여자 연결)
프로젝트와 참여자의 다대다(Many-to-Many) 관계 및 개별 수익률 저장

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| project_id | INTEGER (PK, FK) | 프로젝트 ID |
| participant_id | INTEGER (PK, FK) | 참여자 ID |
| profit_rate | FLOAT | 개별 수익률 (%) |
| joined_at | DATETIME | 참여 날짜 |

**현재 레코드 수**: 0개

**특징**:
- ✅ 프로젝트마다 다른 참여자 선택 가능
- ✅ 참여자별 개별 수익률 설정 가능
- ✅ 같은 참여자가 여러 프로젝트 참여 가능

---

#### 4. **settlements** (정산)
프로젝트별 참여자 정산 내역

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| id | INTEGER (PK) | 정산 ID |
| project_id | INTEGER (NOT NULL, FK) | 프로젝트 ID |
| participant_id | INTEGER (NOT NULL, FK) | 참여자 ID |
| profit_rate | FLOAT | 수익률 (%) |
| amount | FLOAT | 정산 금액 (원) |
| status | VARCHAR | 상태 (pending, paid) |
| paid_at | DATETIME | 지급일시 |
| notes | TEXT | 메모 |
| created_at | DATETIME | 생성일시 |
| updated_at | DATETIME | 수정일시 |

**현재 레코드 수**: 0개

---

#### 5. **project_progress** (프로젝트 진도 로그)
프로젝트별 진도 기록 히스토리

| 컬럼명 | 타입 | 설명 |
|--------|------|------|
| id | INTEGER (PK) | 로그 ID |
| project_id | INTEGER (NOT NULL, FK) | 프로젝트 ID |
| stage | VARCHAR | 단계 (아이디어, 개발, 테스트 등) |
| memo | TEXT (NOT NULL) | 진도 메모 |
| progress_rate | FLOAT | 진도율 (0-100) |
| author | VARCHAR | 작성자 |
| created_at | DATETIME | 생성일시 |
| updated_at | DATETIME | 수정일시 |

**현재 레코드 수**: 0개

**특징**:
- ✅ 프로젝트 진도 변경 히스토리 저장
- ✅ AI 분석 결과 자동 저장
- ✅ 타임라인 뷰 생성 가능

---

## 🔗 테이블 관계도

```
┌─────────────────┐
│  participants   │
│  (참여자)       │
└────────┬────────┘
         │
         │ Many-to-Many
         │
         ├─────────────────────────────┐
         │                             │
┌────────▼────────────────┐   ┌────────▼────────┐
│ project_participants    │   │   settlements   │
│ (프로젝트-참여자 연결)  │   │   (정산)        │
└────────┬────────────────┘   └────────┬────────┘
         │                             │
         │                             │
         │                             │
┌────────▼────────────────┐            │
│      projects           │◄───────────┘
│      (프로젝트)         │
└────────┬────────────────┘
         │
         │ One-to-Many
         │
┌────────▼────────────────┐
│  project_progress       │
│  (진도 로그)            │
└─────────────────────────┘
```

### 관계 설명

1. **participants ↔ projects** (다대다)
   - 중간 테이블: `project_participants`
   - 한 프로젝트에 여러 참여자
   - 한 참여자가 여러 프로젝트 참여

2. **projects → settlements** (일대다)
   - 한 프로젝트에 여러 정산 내역
   - 참여자별 정산 금액 저장

3. **participants → settlements** (일대다)
   - 한 참여자가 여러 정산 내역 보유

4. **projects → project_progress** (일대다)
   - 한 프로젝트에 여러 진도 로그
   - 진도 변경 히스토리 추적

---

## 🚀 SQLite 장점

### 현재 사용하는 이유

✅ **간단한 설치 및 설정**
- 별도 DB 서버 불필요
- 파일 기반으로 관리 용이
- Python 기본 내장

✅ **빠른 개발 속도**
- 즉시 사용 가능
- 마이그레이션 간단
- 테스트 환경 구축 용이

✅ **작은 프로젝트에 적합**
- 중소규모 프로젝트에 충분
- 동시 접속 수 제한적이지만 관리 시스템에는 문제없음

✅ **이식성**
- 단일 파일로 백업/이동 가능
- Windows/Mac/Linux 모두 지원

✅ **제로 설정**
- DATABASE_URL만 설정하면 즉시 작동
- 복잡한 권한 설정 불필요

---

## ⚠️ SQLite 제약사항

### 알아두어야 할 한계

❌ **동시 쓰기 제한**
- 동시에 여러 사용자가 쓰기 작업 시 성능 저하
- 읽기는 무제한, 쓰기는 순차적

❌ **대용량 데이터 처리**
- 수십만 건 이상의 데이터에서는 PostgreSQL/MySQL 권장

❌ **네트워크 접근 불가**
- 로컬 파일 기반
- 원격 DB 서버 불가 (단, NFS 마운트 가능)

❌ **복잡한 권한 관리 불가**
- 사용자별 권한 설정 불가
- 파일 시스템 권한에 의존

---

## 🔄 다른 DB로 전환하기

### PostgreSQL로 마이그레이션

#### 1. PostgreSQL 설치
```bash
# Windows
# PostgreSQL 설치 프로그램 다운로드
# https://www.postgresql.org/download/windows/

# Mac
brew install postgresql

# Linux
sudo apt install postgresql
```

#### 2. 데이터베이스 생성
```sql
CREATE DATABASE chungsan;
CREATE USER chungsan_user WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE chungsan TO chungsan_user;
```

#### 3. 환경변수 설정
```bash
# .env 파일 생성
DATABASE_URL=postgresql://chungsan_user:password123@localhost/chungsan
```

#### 4. 패키지 설치
```bash
pip install psycopg2-binary
```

#### 5. 데이터 마이그레이션
```python
# SQLite → PostgreSQL 마이그레이션 스크립트
import sqlite3
import psycopg2

# SQLite 데이터 읽기
sqlite_conn = sqlite3.connect('chungsan.db')
# PostgreSQL에 쓰기
pg_conn = psycopg2.connect(...)
```

### MySQL로 마이그레이션

#### 환경변수 설정
```bash
DATABASE_URL=mysql+pymysql://user:password@localhost/chungsan
```

#### 패키지 설치
```bash
pip install pymysql
```

---

## 📋 데이터베이스 관리 명령어

### 백업
```bash
# SQLite 백업 (단순 파일 복사)
cp chungsan.db chungsan_backup_$(date +%Y%m%d).db

# 또는 SQL 덤프
sqlite3 chungsan.db .dump > backup.sql
```

### 복원
```bash
# 파일 복사 방식
cp chungsan_backup_20260208.db chungsan.db

# SQL 덤프 방식
sqlite3 chungsan.db < backup.sql
```

### 테이블 정보 확인
```python
# Python 스크립트
import sqlite3
conn = sqlite3.connect('chungsan.db')
cursor = conn.cursor()

# 테이블 목록
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# 특정 테이블 스키마
cursor.execute("PRAGMA table_info(projects);")
print(cursor.fetchall())

conn.close()
```

### 데이터 직접 조회
```python
import sqlite3
conn = sqlite3.connect('chungsan.db')
cursor = conn.cursor()

# 모든 프로젝트 조회
cursor.execute("SELECT * FROM projects;")
for row in cursor.fetchall():
    print(row)

conn.close()
```

---

## 🎯 현재 상태 요약

```
데이터베이스: SQLite 3.40.1
파일 크기: 52 KB
테이블 수: 5개
레코드 수: 0개 (모든 테이블 비어있음)

상태: ✅ 정상 작동 중
백업: ✅ chungsan.db.backup 존재
```

### 테이블별 상태
- ✅ participants (참여자): 준비 완료
- ✅ projects (프로젝트): 준비 완료
- ✅ project_participants (연결): 준비 완료
- ✅ settlements (정산): 준비 완료
- ✅ project_progress (진도 로그): 준비 완료

---

## 💡 권장사항

### 현재 단계 (개발/테스트)
✅ **SQLite 계속 사용 권장**
- 빠른 개발 및 테스트
- 설정 간단
- 백업 용이

### 프로덕션 배포 시
🔄 **PostgreSQL 전환 검토**
- 동시 접속자 10명 이상 예상 시
- 데이터가 10만 건 이상 예상 시
- 원격 DB 서버 필요 시

### 현재 구조 유지 시
✅ **SQLite 최적화**
- 정기적인 백업 (매일 자동 백업)
- VACUUM 명령으로 DB 최적화
- WAL 모드 활성화 (동시성 개선)

---

## 🛠️ SQLite 최적화 설정

### WAL (Write-Ahead Logging) 모드 활성화

**장점**:
- 읽기-쓰기 동시성 개선
- 성능 향상

**설정 방법**:
```python
# app/database.py 수정
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,
        "timeout": 30
    }
)

# WAL 모드 활성화
from sqlalchemy import event

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA synchronous=NORMAL")
    cursor.execute("PRAGMA cache_size=10000")
    cursor.close()
```

---

## 📞 문의 및 지원

데이터베이스 관련 문제가 발생하면:
1. 백업 파일 확인: `chungsan.db.backup`
2. 로그 확인: 서버 콘솔 출력
3. 데이터 복구: 백업에서 복원

**GitHub**: https://github.com/EmmettHwang/chungsan

---

**문서 버전**: v1.0  
**작성일**: 2026-02-08  
**DB 버전**: SQLite 3.40.1
