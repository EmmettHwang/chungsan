# 🔍 Synology phpMyAdmin 포트 찾기 가이드

## 🎯 가장 쉬운 방법 (추천!)

### DSM에서 자동으로 열기

1. 브라우저에서 접속:
```
http://bitnmeta2.synology.me:5000
```

2. Synology 계정으로 로그인

3. 좌측 상단 메뉴(9개 점) 클릭 → **패키지 센터**

4. **설치됨** 탭 클릭

5. **phpMyAdmin** 찾기

6. **열기** 버튼 클릭

→ **자동으로 올바른 포트와 URL로 이동합니다!**

---

## 🔍 방법 2: Web Station 설정 확인

DSM 접속 후:

### ① Web Station 열기
1. 메인 메뉴 → **Web Station** 클릭
2. 설치되지 않았다면 **패키지 센터**에서 설치

### ② 포트 확인
1. 좌측 메뉴 → **일반 설정**
2. **HTTP 포트** 및 **HTTPS 포트** 확인

**일반적인 포트**:
- HTTP: 80, 8080, 8081
- HTTPS: 443, 8443

### ③ 포털 설정 확인
1. 좌측 메뉴 → **포털**
2. phpMyAdmin이 등록되어 있는지 확인
3. 포트 및 경로 확인

---

## 🧪 방법 3: 일반적인 URL 직접 시도

다음 URL들을 브라우저에서 순서대로 시도:

```bash
# 1. 기본 포트 (80)
http://bitnmeta2.synology.me/phpMyAdmin

# 2. 포트 80 명시
http://bitnmeta2.synology.me:80/phpMyAdmin

# 3. 포트 8080 (가장 흔함)
http://bitnmeta2.synology.me:8080/phpMyAdmin

# 4. 포트 8081
http://bitnmeta2.synology.me:8081/phpMyAdmin

# 5. HTTPS 기본 포트
https://bitnmeta2.synology.me/phpMyAdmin

# 6. HTTPS 포트 443
https://bitnmeta2.synology.me:443/phpMyAdmin

# 7. HTTPS 포트 8443
https://bitnmeta2.synology.me:8443/phpMyAdmin
```

---

## 💻 방법 4: SSH로 포트 확인 (고급)

### ① SSH 접속
```bash
ssh admin@bitnmeta2.synology.me
```

### ② 관리자 권한 획득
```bash
sudo -i
```

### ③ 웹 서버 포트 확인

**Apache 사용 시**:
```bash
cat /etc/httpd/conf/httpd.conf | grep "Listen"
```

**Nginx 사용 시**:
```bash
cat /etc/nginx/nginx.conf | grep "listen"
```

### ④ 실행 중인 웹 서버 확인
```bash
netstat -tuln | grep LISTEN | grep -E ':(80|443|8080|8081|8443)'
```

**예상 출력**:
```
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN
```

→ 여기서 포트 번호 확인!

### ⑤ phpMyAdmin 설치 경로 확인
```bash
find /volume*/ -name phpMyAdmin -type d 2>/dev/null
```

**일반적인 경로**:
```
/volume1/web/phpMyAdmin
/volume1/@appstore/phpMyAdmin
```

---

## 🔧 방법 5: MySQL Workbench로 직접 연결

phpMyAdmin 대신 MySQL Workbench를 사용하는 방법:

### ① MySQL Workbench 다운로드
https://dev.mysql.com/downloads/workbench/

### ② 새 연결 생성
- **Connection Name**: Synology NAS
- **Hostname**: `bitnmeta2.synology.me`
- **Port**: `3307`
- **Username**: `root` (또는 `iyrc`)
- **Password**: 저장 클릭 → 비밀번호 입력

### ③ Test Connection
→ 성공하면 **OK** 클릭

### ④ SQL 직접 실행
```sql
CREATE DATABASE IF NOT EXISTS chungsan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'iyrc'@'%' IDENTIFIED BY 'dodan1004';
GRANT ALL PRIVILEGES ON chungsan.* TO 'iyrc'@'%';
FLUSH PRIVILEGES;
```

---

## 🎯 방법 6: HeidiSQL (Windows 전용)

MySQL Workbench보다 가벼운 대안:

### ① HeidiSQL 다운로드
https://www.heidisql.com/download.php

### ② 새 세션 생성
- **네트워크 유형**: MySQL (TCP/IP)
- **호스트명/IP**: `bitnmeta2.synology.me`
- **포트**: `3307`
- **사용자**: `root` (또는 `iyrc`)
- **암호**: 비밀번호 입력

### ③ 연결 후 쿼리 실행
```sql
CREATE DATABASE IF NOT EXISTS chungsan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'iyrc'@'%' IDENTIFIED BY 'dodan1004';
GRANT ALL PRIVILEGES ON chungsan.* TO 'iyrc'@'%';
FLUSH PRIVILEGES;
```

---

## 📊 포트 찾기 비교표

| 방법 | 난이도 | 소요 시간 | 권장 여부 |
|------|--------|----------|-----------|
| DSM "열기" 버튼 | ⭐ (쉬움) | 30초 | ✅ 최고 추천 |
| Web Station 확인 | ⭐⭐ (보통) | 2분 | ✅ 추천 |
| URL 직접 시도 | ⭐⭐ (보통) | 5분 | ✅ 추천 |
| SSH로 확인 | ⭐⭐⭐⭐ (어려움) | 5분 | 고급 사용자 |
| MySQL Workbench | ⭐⭐⭐ (보통) | 10분 | ✅ phpMyAdmin 대체 |
| HeidiSQL | ⭐⭐ (보통) | 10분 | ✅ Windows 사용자 |

---

## 🚀 빠른 해결 순서 (추천!)

### 1단계: DSM 접속 → 자동 열기 (30초)
```
http://bitnmeta2.synology.me:5000
→ 패키지 센터 → phpMyAdmin → 열기
```

### 2단계: 안 되면 일반 포트 시도 (3분)
```bash
http://bitnmeta2.synology.me/phpMyAdmin
http://bitnmeta2.synology.me:8080/phpMyAdmin
```

### 3단계: 그래도 안 되면 MySQL Workbench 사용 (10분)
```
다운로드 → 설치 → bitnmeta2.synology.me:3307 연결
```

---

## ❓ 여전히 포트를 못 찾겠다면?

### 대안 1: SSH로 직접 MySQL 사용

```bash
# SSH 접속
ssh admin@bitnmeta2.synology.me

# MySQL 접속
mysql -u root -p -h localhost

# SQL 실행
CREATE DATABASE chungsan;
CREATE USER 'iyrc'@'%' IDENTIFIED BY 'dodan1004';
GRANT ALL PRIVILEGES ON chungsan.* TO 'iyrc'@'%';
FLUSH PRIVILEGES;
EXIT;
```

### 대안 2: 그냥 Windows에서 연결 시도

포트를 찾지 못해도, **iyrc 사용자를 생성하면** 연결됩니다!

```bash
# Windows에서 실행
python test_mysql_connection.py
```

---

## 🎓 용어 정리

### DSM (DiskStation Manager)
- Synology NAS 관리 웹 인터페이스
- 포트: 5000 (HTTP), 5001 (HTTPS)
- URL: `http://bitnmeta2.synology.me:5000`

### phpMyAdmin
- MySQL/MariaDB 웹 관리 도구
- 포트: 가변 (80, 8080, 8081 등)
- DSM 패키지 센터에서 설치

### Web Station
- Synology 웹 서버 패키지
- phpMyAdmin을 실행하는 서버
- 포트 설정 확인 가능

### MySQL 포트 (3307)
- 데이터베이스 직접 연결 포트
- 웹 브라우저 접속 불가
- Python/MySQL Workbench로 연결

---

## ✅ 체크리스트

포트를 찾기 위해 순서대로 시도:

1. [ ] `http://bitnmeta2.synology.me:5000` DSM 접속
2. [ ] 패키지 센터 → phpMyAdmin → **열기** 버튼
3. [ ] Web Station → 일반 설정 → 포트 확인
4. [ ] `http://bitnmeta2.synology.me/phpMyAdmin` 시도
5. [ ] `http://bitnmeta2.synology.me:8080/phpMyAdmin` 시도
6. [ ] `http://bitnmeta2.synology.me:8081/phpMyAdmin` 시도
7. [ ] MySQL Workbench 다운로드 및 설치
8. [ ] Workbench로 `bitnmeta2.synology.me:3307` 연결
9. [ ] SSH 접속 → MySQL 직접 사용

---

## 🎯 결론

**가장 빠른 방법**:
1. DSM 접속 (`:5000`)
2. 패키지 센터에서 phpMyAdmin **열기** 버튼 클릭
3. 자동으로 올바른 포트로 이동!

**그래도 안 되면**:
- MySQL Workbench 또는 HeidiSQL 사용
- SSH로 직접 MySQL 접속

**포트를 꼭 알아야 하나요?**
- 아니요! DSM "열기" 버튼이 자동으로 찾아줍니다 😊

---

어떤 방법을 시도해볼까요? 결과를 알려주시면 다음 단계로 안내해드리겠습니다! 🚀
