# 🔧 Windows에서 MariaDB mysql 명령어 사용하기

## ❌ 문제
```
'mysql'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.
```

**원인**: MariaDB bin 폴더가 Windows PATH 환경변수에 없음

---

## ✅ 해결 방법

### 방법 1: 전체 경로로 실행 (빠른 해결)

MariaDB 설치 경로를 찾아서 전체 경로로 실행:

```bash
# MariaDB 10.6 예시
"C:\Program Files\MariaDB 10.6\bin\mysql.exe" -u root -p

# MariaDB 10.11 예시
"C:\Program Files\MariaDB 10.11\bin\mysql.exe" -u root -p

# MariaDB 11.0 예시
"C:\Program Files\MariaDB 11.0\bin\mysql.exe" -u root -p

# 32비트 버전
"C:\Program Files (x86)\MariaDB 10.6\bin\mysql.exe" -u root -p
```

#### 설치 경로 찾기

**PowerShell에서**:
```powershell
Get-ChildItem "C:\Program Files" -Recurse -Filter mysql.exe -ErrorAction SilentlyContinue | Select-Object FullName
```

**CMD에서**:
```bash
dir "C:\Program Files\MariaDB*" /s /b | findstr mysql.exe
dir "C:\Program Files (x86)\MariaDB*" /s /b | findstr mysql.exe
```

---

### 방법 2: HeidiSQL 사용 (가장 쉬움! 👍 추천)

MariaDB 설치 시 HeidiSQL이 함께 설치됩니다.

#### ① HeidiSQL 실행

**방법 A**: Windows 시작 메뉴
- Windows 키 누르기
- "HeidiSQL" 입력
- 클릭하여 실행

**방법 B**: 직접 실행
```
C:\Program Files\HeidiSQL\heidisql.exe
```

#### ② 연결 설정

1. 좌측 하단 **새로 만들기** 버튼 클릭

2. **세션 설정**:
   - **세션 이름**: `로컬 MariaDB` (원하는 이름)
   - **네트워크 유형**: `MySQL (TCP/IP)`
   - **라이브러리**: `libmariadb.dll`

3. **연결 정보**:
   - **호스트명/IP**: `localhost` 또는 `127.0.0.1`
   - **사용자**: `root`
   - **포트**: `3306`
   - **암호**: MariaDB 설치 시 설정한 root 비밀번호

4. **저장** 및 **열기** 클릭

#### ③ 데이터베이스 생성

**GUI 방법**:
1. 좌측 데이터베이스 목록에서 빈 공간 **우클릭**
2. **데이터베이스 생성** 선택
3. 설정:
   - **이름**: `chungsan`
   - **문자 집합**: `utf8mb4`
   - **정렬**: `utf8mb4_unicode_ci`
4. **확인** 클릭

**SQL 방법**:
1. 상단 메뉴 → **쿼리** → **새 쿼리 탭**
2. 다음 SQL 입력:

```sql
CREATE DATABASE IF NOT EXISTS chungsan 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

3. **F9** 또는 **▶ 실행** 버튼 클릭

#### ④ 데이터베이스 확인

좌측 패널에서 `chungsan` 데이터베이스가 생성된 것을 확인!

---

### 방법 3: PATH 환경변수 추가 (영구 해결)

mysql 명령어를 어디서나 사용하려면 PATH에 추가:

#### ① MariaDB bin 경로 확인

일반적인 경로:
```
C:\Program Files\MariaDB 10.6\bin
C:\Program Files\MariaDB 10.11\bin
C:\Program Files\MariaDB 11.0\bin
```

#### ② PATH 환경변수 추가

**Windows 10/11**:

1. **시작 메뉴** → "환경 변수" 검색 → **시스템 환경 변수 편집** 클릭

2. **환경 변수** 버튼 클릭

3. **시스템 변수** 섹션에서 **Path** 선택 → **편집** 클릭

4. **새로 만들기** 클릭

5. MariaDB bin 경로 입력:
   ```
   C:\Program Files\MariaDB 10.6\bin
   ```
   (실제 설치된 버전에 맞게 수정)

6. **확인** → **확인** → **확인**

#### ③ CMD/PowerShell 재시작

새 명령 프롬프트 창을 열어야 PATH 변경이 적용됩니다.

#### ④ 테스트

```bash
mysql --version
```

**예상 출력**:
```
mysql  Ver 15.1 Distrib 10.x.x-MariaDB, for Win64 (AMD64)
```

---

### 방법 4: MySQL Workbench 사용

HeidiSQL 대신 MySQL Workbench 사용 가능:

#### ① 다운로드 및 설치
https://dev.mysql.com/downloads/workbench/

#### ② 연결 설정
- **Connection Name**: 로컬 MariaDB
- **Hostname**: `127.0.0.1`
- **Port**: `3306`
- **Username**: `root`
- **Password**: Store in Keychain 클릭 → 비밀번호 입력

#### ③ 데이터베이스 생성

**쿼리 탭**에서:
```sql
CREATE DATABASE IF NOT EXISTS chungsan 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

---

## 🎯 권장 순서

### 🥇 1순위: HeidiSQL (가장 쉽고 직관적!)
- GUI 기반
- MariaDB와 함께 설치됨
- 한글 지원
- 초보자 친화적

### 🥈 2순위: 전체 경로로 실행 (빠른 해결)
- 설치 불필요
- 터미널 선호 시

### 🥉 3순위: PATH 추가 (영구 해결)
- 한 번만 설정
- 이후 편리하게 사용

---

## 🚀 지금 바로 실행

### HeidiSQL로 데이터베이스 생성 (추천!)

1. **HeidiSQL 실행**
   - Windows 시작 메뉴 → "HeidiSQL" 검색

2. **연결 생성**
   - 새로 만들기
   - Host: `localhost`
   - User: `root`
   - Port: `3306`
   - Password: root 비밀번호

3. **chungsan 데이터베이스 생성**
   - 우클릭 → 데이터베이스 생성
   - 이름: `chungsan`
   - 문자 집합: `utf8mb4`

4. **Python 테스트**
   ```bash
   cd "G:\내 드라이브\11. DEV_23\51. Python_mp3등\chungsan\chungsan"
   conda activate BH2025_WOWU
   python test_mysql_connection.py
   ```

---

## 📊 도구 비교

| 도구 | 장점 | 단점 | 추천 |
|------|------|------|------|
| **HeidiSQL** | GUI, 쉬움, 무료 | - | ✅✅✅ 최고 추천 |
| **MySQL CLI** | 빠름, 스크립트 가능 | PATH 설정 필요 | ✅✅ 추천 |
| **MySQL Workbench** | 강력한 기능 | 무거움 | ✅ 고급 사용자 |
| **phpMyAdmin** | 웹 기반 | 설치 복잡 | ⚠️ 필요시 |

---

## ✅ 체크리스트

데이터베이스 생성 확인:

- [ ] HeidiSQL 실행 성공
- [ ] localhost:3306 연결 성공
- [ ] `chungsan` 데이터베이스 생성
- [ ] utf8mb4 문자 집합 설정
- [ ] `.env` 파일 수정 완료:
  ```env
  DB_HOST=localhost
  DB_PORT=3306
  DB_USER=root
  DB_PASSWORD=실제비밀번호
  DB_NAME=chungsan
  ```
- [ ] `python test_mysql_connection.py` 성공
- [ ] `python create_tables.py` 실행
- [ ] 5개 테이블 생성 확인

---

## 🎯 다음 단계

1. ✅ 로컬 MariaDB 설치
2. ⏳ **현재**: HeidiSQL로 데이터베이스 생성
3. ⏭️ Python 연결 테스트
4. ⏭️ 테이블 생성
5. ⏭️ 서버 실행
6. ⏭️ 브라우저 테스트

---

지금 바로 HeidiSQL을 실행해서 `chungsan` 데이터베이스를 생성해보세요! 🚀
