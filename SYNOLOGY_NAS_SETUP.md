# 🏠 Synology NAS MySQL 설정 가이드

## 📍 현재 상황

- **NAS 주소**: bitnmeta2.synology.me
- **MySQL 포트**: 3307
- **데이터베이스**: chungsan
- **사용자**: iyrc
- **문제**: Access denied (권한 없음)

---

## 🔧 1단계: DSM 웹 인터페이스 접속

### 방법 1: HTTP (기본)
```
http://bitnmeta2.synology.me:5000
```

### 방법 2: HTTPS (보안)
```
https://bitnmeta2.synology.me:5001
```

**로그인 계정**: Synology NAS 관리자 계정

---

## 🗄️ 2단계: MariaDB 패키지 확인

1. **패키지 센터** 클릭
2. **설치됨** 탭에서 **MariaDB** 또는 **MariaDB 10** 확인
3. 없다면:
   - **모두** 탭 → **MariaDB 10** 검색
   - **설치** 클릭
   - root 비밀번호 설정

---

## 🌐 3단계: phpMyAdmin 설치 (권장)

### 설치 방법
1. **패키지 센터** → **모두**
2. **phpMyAdmin** 검색 → **설치**
3. 설치 완료 후 **열기** 클릭

### 접속 URL
```
http://bitnmeta2.synology.me:<phpMyAdmin포트>/phpMyAdmin
```

**일반적인 포트**: 8080, 8081, 또는 DSM이 자동 할당

### 로그인
- **사용자**: root
- **비밀번호**: MariaDB 설치 시 설정한 비밀번호

---

## 👤 4단계: 데이터베이스 및 사용자 생성

### phpMyAdmin에서 실행

#### ① 데이터베이스 생성
```sql
CREATE DATABASE IF NOT EXISTS chungsan 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

#### ② 사용자 생성
```sql
-- 모든 IP에서 접속 가능
CREATE USER IF NOT EXISTS 'iyrc'@'%' 
IDENTIFIED BY 'dodan1004';

-- localhost에서만 접속
CREATE USER IF NOT EXISTS 'iyrc'@'localhost' 
IDENTIFIED BY 'dodan1004';
```

#### ③ 권한 부여
```sql
-- chungsan 데이터베이스의 모든 권한 부여
GRANT ALL PRIVILEGES ON chungsan.* TO 'iyrc'@'%';
GRANT ALL PRIVILEGES ON chungsan.* TO 'iyrc'@'localhost';

-- 권한 적용
FLUSH PRIVILEGES;
```

#### ④ 확인
```sql
-- 사용자 목록
SELECT user, host FROM mysql.user WHERE user='iyrc';

-- 권한 확인
SHOW GRANTS FOR 'iyrc'@'%';
SHOW GRANTS FOR 'iyrc'@'localhost';
```

**예상 출력**:
```
+------+-----------+
| user | host      |
+------+-----------+
| iyrc | %         |
| iyrc | localhost |
+------+-----------+

Grants for iyrc@%:
GRANT ALL PRIVILEGES ON `chungsan`.* TO `iyrc`@`%`
```

---

## 🔐 5단계: 방화벽 설정 (필요시)

### DSM 방화벽 규칙 추가

1. **제어판** → **보안** → **방화벽**
2. **편집** 클릭 (프로필 선택)
3. **포트** 탭 → **사용자 지정** 선택
4. **생성** 클릭

**규칙 설정**:
- **포트**: 3307
- **프로토콜**: TCP
- **소스 IP**: 
  - 모든 IP 허용: `0.0.0.0/0` (보안 주의)
  - 특정 IP만: `192.168.x.x` 또는 공인 IP
- **동작**: 허용

---

## 🧪 6단계: Windows에서 연결 테스트

### ① .env 파일 확인
```env
DB_HOST=bitnmeta2.synology.me
DB_PORT=3307
DB_USER=iyrc
DB_PASSWORD=dodan1004
DB_NAME=chungsan
```

### ② 연결 테스트
```bash
cd "G:\내 드라이브\11. DEV_23\51. Python_mp3등\chungsan\chungsan"
conda activate BH2025_WOWU
python test_mysql_connection.py
```

**예상 성공 출력**:
```
============================================================
🔍 MySQL 데이터베이스 연결 테스트
============================================================
호스트: bitnmeta2.synology.me:3307
사용자: iyrc
데이터베이스: chungsan

✅ 연결 성공!
🔗 MySQL 버전: 10.x.x-MariaDB
📊 현재 데이터베이스: chungsan
```

### ③ 테이블 생성
```bash
python create_tables.py
```

### ④ 서버 실행
```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### ⑤ 브라우저 접속
```
http://localhost:8001
```

---

## 🛠️ 대안: SSH로 직접 설정 (고급)

### SSH 접속
```bash
ssh admin@bitnmeta2.synology.me
```

### root로 전환
```bash
sudo -i
```

### MySQL 접속
```bash
mysql -u root -p
```

### SQL 실행
```sql
CREATE DATABASE IF NOT EXISTS chungsan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'iyrc'@'%' IDENTIFIED BY 'dodan1004';
GRANT ALL PRIVILEGES ON chungsan.* TO 'iyrc'@'%';
FLUSH PRIVILEGES;
EXIT;
```

---

## 🔍 문제 해결

### 1. "Access denied" 오류
```sql
-- 사용자 재생성
DROP USER IF EXISTS 'iyrc'@'%';
CREATE USER 'iyrc'@'%' IDENTIFIED BY 'dodan1004';
GRANT ALL PRIVILEGES ON chungsan.* TO 'iyrc'@'%';
FLUSH PRIVILEGES;
```

### 2. "Unknown database" 오류
```sql
-- 데이터베이스 생성
CREATE DATABASE chungsan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. "Can't connect" 오류
- Synology NAS 전원 확인
- 네트워크 연결 확인
- 방화벽 설정 확인
- MariaDB 서비스 실행 확인: DSM → **패키지 센터** → MariaDB → **실행**

### 4. 포트 연결 불가
```bash
# Windows PowerShell에서 포트 확인
Test-NetConnection -ComputerName bitnmeta2.synology.me -Port 3307
```

**성공 시**:
```
TcpTestSucceeded : True
```

---

## 📊 포트 정리

| 포트 | 용도 | 위치 |
|------|------|------|
| **3307** | MySQL 데이터베이스 | Synology NAS |
| **8001** | FastAPI 웹 서버 | 로컬 PC (Windows) |
| **5000** | DSM HTTP | Synology 웹 관리 |
| **5001** | DSM HTTPS | Synology 웹 관리 (보안) |
| **8080** | phpMyAdmin (예시) | Synology 웹 관리 |

---

## ✅ 완료 체크리스트

- [ ] DSM 접속 성공
- [ ] MariaDB 패키지 설치 확인
- [ ] phpMyAdmin 설치 및 접속
- [ ] root로 phpMyAdmin 로그인
- [ ] `chungsan` 데이터베이스 생성
- [ ] `iyrc` 사용자 생성
- [ ] 권한 부여 및 FLUSH
- [ ] 사용자/권한 확인
- [ ] Windows에서 `test_mysql_connection.py` 성공
- [ ] `create_tables.py` 실행 성공
- [ ] 테이블 5개 생성 확인
- [ ] `uvicorn` 서버 실행 성공
- [ ] 브라우저에서 http://localhost:8001 접속

---

## 🎯 다음 단계

1. **현재 위치**: Synology NAS MySQL 설정
2. **다음**: Windows에서 연결 테스트
3. **이후**: 테이블 생성 및 샘플 데이터 입력
4. **최종**: 프론트엔드 테스트 및 정산 계산

---

## 📞 도움이 필요하면

위 단계를 진행하면서 막히는 부분이 있으면:
1. 에러 메시지 전체 복사
2. 현재 어느 단계인지 알려주기
3. 스크린샷 (선택)

함께 해결해 드리겠습니다! 🚀
