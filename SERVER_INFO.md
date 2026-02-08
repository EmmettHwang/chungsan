# 청산에사르리랏다 - SSH 및 서버 정보

## 🌐 프로덕션 서버 (Cafe24)

### SSH 접속 정보
```bash
호스트: minilms.cafe24.com
사용자: root
비밀번호: dodan1004~!@
포트: 22
```

### 빠른 접속
```bash
ssh root@minilms.cafe24.com
# 비밀번호 입력: dodan1004~!@
```

### SSH 키 등록 (비밀번호 없이 접속)
```bash
# 로컬에서 SSH 키 생성 (없는 경우)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# 공개키를 서버에 복사
ssh-copy-id root@minilms.cafe24.com

# 이후 비밀번호 없이 접속 가능
ssh root@minilms.cafe24.com
```

---

## 📁 서버 디렉토리 구조

```
/home/hosting_users/
├── 사용자명/
│   └── www/
│       ├── backend/
│       │   ├── main.py
│       │   ├── requirements.txt
│       │   └── logs/
│       ├── frontend/
│       │   ├── index.html
│       │   ├── app.js
│       │   └── static/
│       ├── .env
│       └── ecosystem.config.js
```

**주의**: `사용자명` 부분을 실제 Cafe24 사용자명으로 확인 필요

---

## 🚀 배포 방법

### 방법 1: 자동 배포 스크립트 사용 ⭐
```bash
cd /home/user/webapp
./deploy-cafe24.sh
```

**자동 실행:**
1. 로컬 Git 상태 확인
2. GitHub에 푸시
3. rsync 또는 git pull 선택
4. 서버에 파일 전송
5. 패키지 설치
6. PM2 서비스 재시작

### 방법 2: 수동 배포
```bash
# 1. 로컬에서 커밋 및 푸시
git add .
git commit -m "배포: 설명"
git push origin main

# 2. 서버에 SSH 접속
ssh root@minilms.cafe24.com

# 3. 프로젝트 디렉토리로 이동
cd /home/hosting_users/사용자명/www

# 4. 최신 코드 가져오기
git pull origin main

# 5. 패키지 설치 (필요시)
pip3 install -r backend/requirements.txt

# 6. 서비스 재시작
pm2 restart all
```

### 방법 3: rsync 직접 사용
```bash
# 로컬에서 실행
rsync -avz --progress \
    --exclude 'node_modules' \
    --exclude '.git' \
    --exclude '*.pyc' \
    --exclude '__pycache__' \
    --exclude '.env' \
    -e "ssh -p 22" \
    ./ root@minilms.cafe24.com:/home/hosting_users/사용자명/www/
```

---

## 🔧 서버 관리 명령어

### PM2 서비스 관리
```bash
# SSH 접속
ssh root@minilms.cafe24.com

# 서비스 목록 확인
pm2 list

# 모든 서비스 재시작
pm2 restart all

# 특정 서비스 재시작
pm2 restart backend

# 로그 확인
pm2 logs

# 실시간 로그 보기
pm2 logs --lines 100

# 서비스 중지
pm2 stop all

# 서비스 시작
pm2 start ecosystem.config.js
```

### 데이터베이스 관리
```bash
# MySQL 접속
mysql -u root -p

# 데이터베이스 선택
USE minilms;

# 테이블 목록 확인
SHOW TABLES;

# 백업
mysqldump -u root -p minilms > backup_$(date +%Y%m%d).sql

# 복원
mysql -u root -p minilms < backup_20260206.sql
```

### 로그 확인
```bash
# 백엔드 로그
tail -f /home/hosting_users/사용자명/www/backend/logs/app.log

# PM2 로그
pm2 logs --lines 100

# Nginx 로그 (있는 경우)
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

---

## 🔐 보안 설정

### .env 파일 설정
서버에 `.env` 파일을 직접 생성하세요 (Git에 포함되지 않음):

```bash
ssh root@minilms.cafe24.com
cd /home/hosting_users/사용자명/www
nano .env
```

**.env 내용:**
```bash
# 데이터베이스
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=실제_비밀번호
DB_NAME=minilms

# API Keys
GROQ_API_KEY=실제_키
OPENAI_API_KEY=실제_키

# 서버 설정
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=production
```

### 파일 권한 설정
```bash
# 프로젝트 디렉토리 권한
chmod -R 755 /home/hosting_users/사용자명/www

# .env 파일 권한 (읽기 전용)
chmod 600 /home/hosting_users/사용자명/www/.env

# 실행 스크립트 권한
chmod +x /home/hosting_users/사용자명/www/*.sh
```

---

## 🐛 트러블슈팅

### 서비스가 시작되지 않는 경우
```bash
# PM2 로그 확인
pm2 logs

# Python 패키지 재설치
pip3 install -r backend/requirements.txt --force-reinstall

# PM2 완전 재시작
pm2 delete all
pm2 start ecosystem.config.js
```

### 데이터베이스 연결 실패
```bash
# MySQL 상태 확인
systemctl status mysql

# MySQL 재시작
systemctl restart mysql

# 연결 테스트
mysql -u root -p -e "SELECT 1"
```

### 포트 충돌
```bash
# 8000번 포트 사용 프로세스 확인
lsof -i :8000

# 프로세스 종료
kill -9 프로세스ID
```

---

## 📊 모니터링

### 서버 상태 확인
```bash
# CPU, 메모리 사용량
htop

# 디스크 사용량
df -h

# 프로세스 목록
ps aux | grep python
ps aux | grep uvicorn
```

### 실시간 모니터링
```bash
# PM2 모니터링 대시보드
pm2 monit

# 시스템 리소스
watch -n 1 'free -h && df -h'
```

---

## 🔗 유용한 링크

- **서버 관리**: http://minilms.cafe24.com:8000/docs (FastAPI Swagger UI)
- **프론트엔드**: http://minilms.cafe24.com
- **Cafe24 관리자**: https://www.cafe24.com

---

## 📝 배포 체크리스트

배포 전 확인사항:
- [ ] 로컬에서 테스트 완료
- [ ] Git 커밋 및 푸시 완료
- [ ] .env 파일 서버에 설정됨
- [ ] 데이터베이스 백업 완료
- [ ] PM2 설정 파일 확인
- [ ] 배포 스크립트 실행
- [ ] 서비스 재시작 확인
- [ ] 웹사이트 동작 확인
- [ ] 로그 에러 확인

---

**마지막 업데이트**: 2026-02-06  
**관리자**: EmmettHwang
