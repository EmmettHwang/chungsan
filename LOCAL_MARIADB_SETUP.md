# 🏠 로컬 MariaDB 설정 가이드 (Windows)

## ✅ 완료된 작업
- [x] MariaDB 설치 완료

---

## 🔧 1단계: .env 파일 수정

프로젝트 폴더에서 `.env` 파일을 열고 다음과 같이 수정:

```env
# ==================== 데이터베이스 설정 ====================
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mariadb_root_password
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
APP_VERSION=1.2.0
DEBUG=True
```

**⚠️ 중요**: `your_mariadb_root_password`를 실제 MariaDB root 비밀번호로 변경!

---

## 🗄️ 2단계: MariaDB 접속 확인

### 방법 1: MySQL CLI (명령 프롬프트)

```bash
mysql -u root -p
```

비밀번호 입력 후:

```sql
-- MariaDB 버전 확인
SELECT VERSION();

-- 데이터베이스 목록
SHOW DATABASES;

-- 종료
EXIT;
```

### 방법 2: HeidiSQL (GUI 도구)

MariaDB 설치 시 함께 설치되었을 수 있습니다.

**연결 설정**:
- **네트워크 유형**: MySQL (TCP/IP)
- **호스트명**: `localhost` 또는 `127.0.0.1`
- **사용자**: `root`
- **포트**: `3306`
- **암호**: MariaDB root 비밀번호

---

## 🎯 3단계: chungsan 데이터베이스 생성

### 옵션 A: MySQL CLI에서

```bash
mysql -u root -p
```

SQL 실행:

```sql
-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS chungsan 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 확인
SHOW DATABASES;
USE chungsan;

-- 종료
EXIT;
```

### 옵션 B: HeidiSQL에서

1. 좌측 데이터베이스 목록에서 우클릭
2. **데이터베이스 생성** 선택
3. 이름: `chungsan`
4. 문자 집합: `utf8mb4`
5. 정렬: `utf8mb4_unicode_ci`
6. **확인** 클릭

---

## 🧪 4단계: Python 연결 테스트

### ① 가상환경 활성화

```bash
cd "G:\내 드라이브\11. DEV_23\51. Python_mp3등\chungsan\chungsan"
conda activate BH2025_WOWU
```

### ② 연결 테스트 실행

```bash
python test_mysql_connection.py
```

**예상 성공 출력**:
```
============================================================
🔍 MySQL 데이터베이스 연결 테스트
============================================================
호스트: localhost:3306
사용자: root
데이터베이스: chungsan

✅ 연결 성공!
🔗 MySQL 버전: 10.x.x-MariaDB
📊 현재 데이터베이스: chungsan

📊 기존 테이블 목록:
(테이블 없음 또는 기존 테이블 표시)
============================================================
```

---

## 🏗️ 5단계: 테이블 생성

```bash
python create_tables.py
```

**예상 출력**:
```
============================================================
🗄️  데이터베이스 테이블 생성
============================================================
데이터베이스: chungsan
호스트: localhost:3306

✅ 테이블 생성 완료!

생성된 테이블:
  1. participants (참여자)
  2. projects (프로젝트)
  3. project_participants (프로젝트 참여자)
  4. settlements (정산)
  5. project_progress (진도 관리)
============================================================
```

### 테이블 확인

**MySQL CLI**:
```bash
mysql -u root -p chungsan
```

```sql
SHOW TABLES;

-- 테이블 구조 확인
DESCRIBE participants;
DESCRIBE projects;
DESCRIBE project_participants;
DESCRIBE settlements;
DESCRIBE project_progress;

EXIT;
```

---

## 🚀 6단계: FastAPI 서버 실행

```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

**예상 출력**:
```
INFO:     Will watch for changes in these directories: ['G:\\...\\chungsan']
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using WatchFiles
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
🔗 데이터베이스 연결: root@localhost:3306/chungsan
INFO:     Application startup complete.
```

---

## 🌐 7단계: 브라우저 접속

```
http://localhost:8001
```

### 테스트 시나리오

#### ① 참여자 추가
1. 좌측 메뉴 → **참여자 관리**
2. **참여자 추가** 버튼 클릭
3. 정보 입력:
   - 이름: 홍길동
   - 역할: 리더 (lead)
   - 기본 수익률: 25%
   - 연락처: 010-1234-5678
4. **저장** 클릭

#### ② 프로젝트 생성
1. 좌측 메뉴 → **프로젝트 관리**
2. **프로젝트 추가** 버튼 클릭
3. **기본 정보** 탭:
   - 프로젝트명: 테스트 프로젝트
   - 클라이언트: ABC 회사
   - 총 계약금: 10,000,000원
   - 원가: 6,000,000원
   - 상태: 진행중
4. **단계 관리** 탭:
   - 아이디어 날짜: 자동 입력 (오늘)
   - 계약일: 원하는 날짜 선택
5. **참여자 관리** 탭:
   - 참여자 체크박스 선택
   - 수익률 확인/수정
6. **진도 관리** 탭:
   - 진도 메모 입력: "프로젝트 킥오프 완료, 요구사항 분석 중"
   - **자동 분석** 클릭
7. **저장** 클릭

#### ③ 정산 계산
1. 좌측 메뉴 → **정산 계산**
2. 프로젝트 선택: "테스트 프로젝트"
3. **정산 계산** 버튼 클릭
4. 각 참여자별 수익 확인

---

## 🔍 8단계: 데이터 확인

### MySQL CLI로 확인

```bash
mysql -u root -p chungsan
```

```sql
-- 참여자 목록
SELECT code, name, role, default_profit_rate FROM participants;

-- 프로젝트 목록
SELECT name, client, total_amount, profit, status FROM projects;

-- 프로젝트 참여자
SELECT 
    p.name AS project_name,
    pt.name AS participant_name,
    pp.profit_rate
FROM project_participants pp
JOIN projects p ON pp.project_id = p.id
JOIN participants pt ON pp.participant_id = pt.id;

-- 정산 내역
SELECT 
    p.name AS project_name,
    pt.name AS participant_name,
    s.profit_rate,
    s.amount
FROM settlements s
JOIN projects p ON s.project_id = p.id
JOIN participants pt ON s.participant_id = pt.id;

EXIT;
```

---

## 🎨 9단계: 샘플 데이터 입력 (선택)

빠른 테스트를 위한 샘플 데이터:

```bash
mysql -u root -p chungsan
```

```sql
-- 참여자 5명 추가
INSERT INTO participants (code, name, role, default_profit_rate, phone, email, created_at, updated_at) VALUES
('P001', '김철수', 'admin', 30.0, '010-1111-1111', 'kim@example.com', NOW(), NOW()),
('P002', '이영희', 'lead', 25.0, '010-2222-2222', 'lee@example.com', NOW(), NOW()),
('P003', '박민수', 'senior', 20.0, '010-3333-3333', 'park@example.com', NOW(), NOW()),
('P004', '최지영', 'regular', 15.0, '010-4444-4444', 'choi@example.com', NOW(), NOW()),
('P005', '정수진', 'assistant', 10.0, '010-5555-5555', 'jung@example.com', NOW(), NOW());

-- 프로젝트 1개 추가
INSERT INTO projects (
    name, client, total_amount, cost, profit, status,
    idea_date, contract_date, start_date, end_date,
    progress_notes, progress_rate, current_stage,
    created_at, updated_at
) VALUES (
    '웹사이트 리뉴얼 프로젝트', 
    'ABC 주식회사', 
    15000000.0, 
    9000000.0, 
    6000000.0, 
    'in_progress',
    NOW(), 
    DATE_ADD(NOW(), INTERVAL 7 DAY),
    NOW(),
    DATE_ADD(NOW(), INTERVAL 60 DAY),
    '프로젝트 시작, 요구사항 분석 단계',
    30.0,
    'consultation',
    NOW(), 
    NOW()
);

-- 프로젝트 참여자 연결 (5명 모두 참여)
INSERT INTO project_participants (project_id, participant_id, profit_rate, joined_at) VALUES
(1, 1, 30.0, NOW()),
(1, 2, 25.0, NOW()),
(1, 3, 20.0, NOW()),
(1, 4, 15.0, NOW()),
(1, 5, 10.0, NOW());

-- 확인
SELECT * FROM participants;
SELECT name, client, total_amount, profit, status FROM projects;
SELECT * FROM project_participants;

EXIT;
```

---

## 🔧 문제 해결

### 1. "Access denied for user 'root'@'localhost'"

**원인**: 비밀번호가 틀렸거나 root 계정이 비활성화됨

**해결**:
```bash
# MariaDB 재설정 (관리자 권한 CMD)
cd "C:\Program Files\MariaDB 10.x\bin"
mysql -u root
```

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
EXIT;
```

### 2. "Can't connect to MySQL server on 'localhost'"

**원인**: MariaDB 서비스가 실행되지 않음

**해결**:
```bash
# 서비스 확인 (관리자 권한 CMD)
sc query MariaDB

# 서비스 시작
net start MariaDB
```

또는:
- **Windows 서비스** (services.msc) 열기
- **MariaDB** 찾기
- 우클릭 → **시작**

### 3. "Unknown database 'chungsan'"

**원인**: 데이터베이스가 생성되지 않음

**해결**:
```bash
mysql -u root -p
```

```sql
CREATE DATABASE chungsan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 4. pymysql 설치 오류

```bash
pip install --upgrade pymysql cryptography
```

---

## 📊 로컬 vs 원격 비교

| 항목 | 로컬 MariaDB | Synology NAS | Cafe24 MySQL |
|------|--------------|--------------|--------------|
| 호스트 | localhost | bitnmeta2.synology.me | minilms.cafe24.com |
| 포트 | 3306 | 3307 | 3306 |
| 접속 속도 | ⚡ 매우 빠름 | 🚀 빠름 (로컬 네트워크) | 🐢 느림 (인터넷) |
| 설정 난이도 | ⭐ 쉬움 | ⭐⭐⭐ 어려움 | ⭐⭐⭐⭐ 매우 어려움 |
| 백업 | 수동 | 자동 가능 | Cafe24 관리 |
| 개발 환경 | ✅ 최적 | ✅ 좋음 | ❌ 접속 제한 |
| 프로덕션 | ❌ 부적합 | ✅ 적합 | ✅ 적합 |

**권장 사용**:
- **개발/테스트**: 로컬 MariaDB (가장 빠르고 쉬움)
- **팀 협업**: Synology NAS
- **실제 배포**: Cafe24 또는 AWS/GCP

---

## ✅ 완료 체크리스트

- [ ] MariaDB 설치 완료
- [ ] .env 파일 수정 (localhost, root, 비밀번호)
- [ ] MySQL CLI로 접속 확인
- [ ] chungsan 데이터베이스 생성
- [ ] `python test_mysql_connection.py` 성공
- [ ] `python create_tables.py` 실행
- [ ] 5개 테이블 생성 확인
- [ ] `uvicorn main:app --reload` 서버 실행
- [ ] http://localhost:8001 브라우저 접속
- [ ] 참여자 추가 테스트
- [ ] 프로젝트 생성 테스트
- [ ] 정산 계산 테스트

---

## 🎯 다음 단계

1. ✅ 로컬 MariaDB 설치 완료
2. ⏳ **현재**: .env 수정 및 연결 테스트
3. ⏭️ 테이블 생성
4. ⏭️ 서버 실행
5. ⏭️ 프론트엔드 테스트
6. ⏭️ 샘플 데이터 입력
7. ⏭️ 전체 기능 테스트

---

## 📚 참고 문서

- **MYSQL_MIGRATION_GUIDE.md** - MySQL 전환 가이드
- **SYNOLOGY_NAS_SETUP.md** - Synology 설정
- **find_phpmyadmin_port.md** - phpMyAdmin 포트 찾기
- **DATABASE_INFO.md** - 데이터베이스 구조
- **FRONTEND_UPGRADE_COMPLETE.md** - 프론트엔드 가이드

---

## 🚀 빠른 시작 요약

```bash
# 1. .env 파일 수정 (localhost, root, 비밀번호)

# 2. 가상환경 활성화
conda activate BH2025_WOWU

# 3. 데이터베이스 생성
mysql -u root -p
CREATE DATABASE chungsan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;

# 4. 연결 테스트
python test_mysql_connection.py

# 5. 테이블 생성
python create_tables.py

# 6. 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8001 --reload

# 7. 브라우저
http://localhost:8001
```

---

지금 바로 `.env` 파일을 수정하고 `python test_mysql_connection.py`를 실행해보세요! 🎉
