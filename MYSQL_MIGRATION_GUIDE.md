# 🔄 MySQL 전환 완료 가이드

## 📅 전환 정보
- **날짜**: 2026-02-08
- **이전 DB**: SQLite 3.40.1
- **새 DB**: MySQL (Cafe24)
- **상태**: ✅ 코드 준비 완료

---

## 🎯 변경 사항 요약

### 1. 데이터베이스 변경
```
SQLite (로컬 파일)  →  MySQL (Cafe24 서버)
```

### 2. 연결 정보 (.env)
```env
DB_HOST=minilms.cafe24.com
DB_PORT=3306
DB_USER=iyrc
DB_PASSWORD=dodan1004
DB_NAME=chungsan
```

### 3. 수정된 파일
- ✅ `app/database.py` - MySQL 연결 설정
- ✅ `requirements.txt` - pymysql, cryptography 추가
- ✅ `.env` - 데이터베이스 연결 정보
- ✅ `.gitignore` - .env 파일 제외 (이미 포함됨)

---

## 🚀 Windows 환경 설정 가이드

### 1단계: 최신 코드 받기

```bash
cd "G:\내 드라이브\11. DEV_23\51. Python_mp3등\chungsan\chungsan"
git pull origin main
```

### 2단계: .env 파일 생성

프로젝트 루트 폴더에 `.env` 파일을 생성하고 다음 내용을 입력:

```env
# ==================== 데이터베이스 설정 ====================
DB_HOST=minilms.cafe24.com
DB_PORT=3306
DB_USER=iyrc
DB_PASSWORD=dodan1004
DB_NAME=chungsan

# ==================== FTP 설정 ====================
FTP_HOST=minilms.cafe24.com
FTP_PORT=21
FTP_USER=minilms_ftp
FTP_PASSWORD=dodan1004

# ==================== 관리자 계정 ====================
ROOT_USER=root
ROOT_PASSWORD=xhRl1004!@#

# ==================== Google Client ID ====================
GOOGLE_CLIENT_ID=770973091354-g59o434mblbigic50lsvl2vmgcif59er.apps.googleusercontent.com

# ==================== 애플리케이션 설정 ====================
APP_NAME=청산에사르리랏다
APP_VERSION=1.1.0
DEBUG=False
```

**중요**: `.env` 파일은 Git에 커밋되지 않습니다! (.gitignore에 포함됨)

### 3단계: 필요한 패키지 설치

```bash
# Conda 환경 활성화
conda activate BH2025_WOWU

# MySQL 드라이버 설치
pip install pymysql cryptography python-dotenv
```

### 4단계: 데이터베이스 연결 테스트

```bash
python test_mysql_connection.py
```

테스트 스크립트 내용 (`test_mysql_connection.py`):
```python
import os
from dotenv import load_dotenv
import pymysql

# .env 파일 로드
load_dotenv()

# 연결 정보
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT", 3306))
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

print("🔍 데이터베이스 연결 테스트...")
print(f"호스트: {host}:{port}")
print(f"사용자: {user}")
print(f"데이터베이스: {database}")
print()

try:
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset='utf8mb4',
        connect_timeout=10
    )
    
    print("✅ 데이터베이스 연결 성공!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION();")
    version = cursor.fetchone()[0]
    print(f"📊 MySQL 버전: {version}")
    
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print(f"\n📋 기존 테이블 목록 ({len(tables)}개):")
    for table in tables:
        print(f"  - {table[0]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"❌ 연결 실패: {e}")

print("\n✨ 연결 테스트 완료!")
```

### 5단계: 데이터베이스 테이블 생성

```bash
python create_tables.py
```

테이블 생성 스크립트 내용 (`create_tables.py`):
```python
from app.database import engine, Base
from app.models import Participant, Project, Settlement, ProjectProgress

print("🔧 데이터베이스 테이블 생성 중...")

# 모든 테이블 생성
Base.metadata.create_all(bind=engine)

print("✅ 테이블 생성 완료!")
print("\n생성된 테이블:")
print("  - participants (참여자)")
print("  - projects (프로젝트)")
print("  - project_participants (프로젝트-참여자 연결)")
print("  - settlements (정산)")
print("  - project_progress (진도 로그)")
```

### 6단계: 서버 실행

```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### 7단계: 브라우저 접속

```
http://localhost:8001
```

---

## 📊 MySQL vs SQLite 비교

| 항목 | SQLite | MySQL (Cafe24) |
|------|--------|---------------|
| **설치** | 불필요 | 서버 필요 |
| **속도** | 빠름 (로컬) | 네트워크 지연 |
| **동시성** | 제한적 | 우수 |
| **확장성** | 제한적 | 우수 |
| **백업** | 파일 복사 | mysqldump |
| **원격 접속** | 불가 | 가능 |
| **용량** | ~1GB 권장 | 무제한 |
| **현재 상황** | ❌ 로컬 전용 | ✅ 서버 공유 가능 |

---

## 🎯 MySQL 장점 (Cafe24 사용 이유)

### ✅ 서버 공유 가능
- 여러 컴퓨터에서 동일한 데이터 접근
- 팀원들과 데이터 공유
- 원격 접속 가능

### ✅ 동시성 우수
- 여러 사용자 동시 접속
- 데이터 락(Lock) 관리 우수
- 트랜잭션 안정성

### ✅ 대용량 데이터 처리
- 수십만 건 이상 데이터 처리
- 인덱스 최적화
- 쿼리 성능 우수

### ✅ 백업 및 복구
- 자동 백업 설정 가능
- Point-in-time Recovery
- 복제(Replication) 지원

### ✅ 프로덕션 배포 준비
- Cafe24 호스팅과 연동
- 안정적인 서비스 운영
- 전문적인 DB 관리

---

## ⚠️ 주의사항

### 1. .env 파일 보안
```bash
# ❌ 절대 Git에 커밋하지 마세요!
# .gitignore에 이미 포함되어 있습니다.

# ✅ 팀원들과 공유 시:
# - 암호화된 채널 사용 (카카오톡, 이메일 암호화)
# - 또는 별도 보안 저장소 (LastPass, 1Password)
```

### 2. 연결 정보 확인
```python
# app/database.py에서 연결 정보 출력
# 서버 시작 시 다음과 같이 표시됩니다:
# 🔗 데이터베이스 연결: iyrc@minilms.cafe24.com:3306/chungsan
```

### 3. 연결 실패 시 체크리스트
- [ ] .env 파일이 프로젝트 루트에 있는가?
- [ ] DB_HOST, DB_USER, DB_PASSWORD 정보가 정확한가?
- [ ] pymysql 패키지가 설치되어 있는가?
- [ ] 방화벽이 3306 포트를 막고 있지 않은가?
- [ ] Cafe24 MySQL 서버가 외부 접속을 허용하는가?

---

## 🔧 문제 해결

### 문제 1: "Can't connect to MySQL server"

**원인**: 네트워크 연결 불가 또는 방화벽 차단

**해결**:
1. Cafe24 MySQL 원격 접속 설정 확인
2. 방화벽 3306 포트 허용
3. 호스트명 정확성 확인 (minilms.cafe24.com)

### 문제 2: "Access denied for user"

**원인**: 사용자명 또는 비밀번호 오류

**해결**:
1. .env 파일의 DB_USER, DB_PASSWORD 재확인
2. Cafe24 관리 페이지에서 MySQL 사용자 확인
3. 비밀번호 특수문자 이스케이프 필요 여부 확인

### 문제 3: "Unknown database 'chungsan'"

**원인**: 데이터베이스가 존재하지 않음

**해결**:
```sql
-- Cafe24 MySQL 관리 도구 또는 phpMyAdmin에서 실행
CREATE DATABASE chungsan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 문제 4: 한글 깨짐

**원인**: 문자 인코딩 문제

**해결**:
```python
# database.py에 이미 포함됨
# ?charset=utf8mb4
# 추가 설정 불필요
```

---

## 📋 테이블 생성 확인

### 생성될 테이블 목록 (5개)

1. **participants** - 참여자 정보
2. **projects** - 프로젝트 정보 (10단계 날짜 포함)
3. **project_participants** - 프로젝트-참여자 연결 (개별 수익률)
4. **settlements** - 정산 내역
5. **project_progress** - 진도 로그

### 테이블 확인 방법

#### 방법 1: Python 스크립트
```python
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
for table in cursor.fetchall():
    print(table[0])

conn.close()
```

#### 방법 2: Cafe24 phpMyAdmin
1. Cafe24 관리 페이지 로그인
2. MySQL 관리 메뉴
3. phpMyAdmin 접속
4. `chungsan` 데이터베이스 선택
5. 테이블 목록 확인

---

## 🚀 배포 준비

### Cafe24 호스팅 배포 시

1. **FTP로 파일 업로드**
```
FTP_HOST: minilms.cafe24.com
FTP_USER: minilms_ftp
FTP_PASSWORD: dodan1004
```

2. **Python 환경 설정**
```bash
# Cafe24 서버에서
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **환경변수 설정**
```bash
# 서버에 .env 파일 생성
# 또는 환경변수로 직접 설정
export DB_HOST=minilms.cafe24.com
export DB_USER=iyrc
# ... 기타 설정
```

4. **서비스 시작**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
# 또는 Gunicorn 사용
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

---

## 📈 성능 최적화

### 연결 풀 설정 (이미 적용됨)

```python
# app/database.py
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,      # 연결 유효성 검사
    pool_recycle=3600,       # 1시간마다 재활용
    pool_size=10,            # 기본 연결 10개
    max_overflow=20,         # 최대 30개까지 확장
)
```

### 인덱스 최적화 (추후 추가 가능)

```sql
-- 자주 검색하는 컬럼에 인덱스 추가
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_client ON projects(client);
CREATE INDEX idx_participants_code ON participants(code);
```

---

## 🎉 완료 체크리스트

Windows 환경에서 다음을 확인하세요:

- [ ] Git pull로 최신 코드 받기
- [ ] .env 파일 생성 및 정보 입력
- [ ] pymysql, cryptography 패키지 설치
- [ ] test_mysql_connection.py 실행 (연결 테스트)
- [ ] create_tables.py 실행 (테이블 생성)
- [ ] uvicorn으로 서버 실행
- [ ] http://localhost:8001 접속 확인
- [ ] 참여자 추가 테스트
- [ ] 프로젝트 추가 테스트
- [ ] 정산 계산 테스트

---

## 📚 추가 자료

- **MySQL 공식 문서**: https://dev.mysql.com/doc/
- **PyMySQL 문서**: https://pymysql.readthedocs.io/
- **SQLAlchemy 문서**: https://docs.sqlalchemy.org/
- **Cafe24 호스팅 가이드**: https://www.cafe24.com/

---

## 🆘 지원

문제가 발생하면:
1. 에러 메시지 전체 복사
2. .env 파일 설정 확인 (비밀번호 제외)
3. test_mysql_connection.py 결과 공유
4. 서버 로그 확인

**GitHub**: https://github.com/EmmettHwang/chungsan

---

**전환 완료일**: 2026-02-08  
**버전**: v1.2.0  
**상태**: 🟢 MySQL 연동 준비 완료

**다음 단계**: Windows 환경에서 테스트 후 피드백 부탁드립니다! 🚀
