# 🚨 Git Pull 에러 해결 가이드 (.env 파일 충돌)

## 문제 상황

```bash
git pull origin main
```

실행 시 다음과 같은 에러 발생:
```
error: Your local changes to the following files would be overwritten by merge:
        .env
Please commit your changes or stash them before you merge.
Aborting
```

또는
```
error: The following untracked working tree files would be overwritten by merge:
        .env
Please move or remove them before you merge.
Aborting
```

---

## 🎯 원인

**.env 파일이 Git에 추적되고 있거나, pull 시 충돌 발생**

---

## ✅ 해결 방법 (3가지)

### 방법 1: .env 파일 백업 후 Pull (추천) ⭐

```bash
# 1. .env 파일 백업
copy .env .env.backup

# 2. .env 파일 삭제
del .env

# 3. Pull 실행
git pull origin main

# 4. .env 파일 복원
copy .env.backup .env

# 5. 백업 파일 삭제 (선택)
del .env.backup
```

**장점**: 기존 설정 유지, 안전함  
**단점**: 수동 작업 필요

---

### 방법 2: Stash 사용

```bash
# 1. 현재 변경사항 임시 저장
git stash

# 2. Pull 실행
git pull origin main

# 3. 임시 저장한 변경사항 복원
git stash pop
```

**장점**: Git 명령어로 간단  
**단점**: .env가 Git에 추적 중이면 충돌 가능

---

### 방법 3: .env 파일을 Git에서 제거 (권장) 🌟

**.env 파일이 Git에 추적되고 있다면, 완전히 제거해야 합니다!**

```bash
# 1. Git 추적에서 제거 (파일은 유지)
git rm --cached .env

# 2. 커밋
git commit -m "Remove .env from Git tracking"

# 3. Pull 실행
git pull origin main

# 4. .env 파일이 삭제되었다면 다시 생성
# (내용은 아래 참조)
```

**장점**: 근본적인 해결, 보안 강화  
**단점**: 팀원 모두 적용 필요

---

## 🔍 .env 파일이 Git에 추적되고 있는지 확인

```bash
# 방법 1: git status로 확인
git status

# 방법 2: git ls-files로 확인
git ls-files | findstr .env

# 출력이 있으면 → Git에 추적 중 ❌
# 출력이 없으면 → Git에 추적 안 함 ✅
```

---

## 📝 .env 파일 내용 (재생성 시)

만약 .env 파일이 삭제되었다면, 프로젝트 루트에 다시 생성하세요:

### Windows 명령 프롬프트 (CMD)
```cmd
echo # ==================== 데이터베이스 설정 ==================== > .env
echo DB_HOST=minilms.cafe24.com >> .env
echo DB_PORT=3306 >> .env
echo DB_USER=iyrc >> .env
echo DB_PASSWORD=dodan1004 >> .env
echo DB_NAME=chungsan >> .env
echo. >> .env
echo # ==================== FTP 설정 ==================== >> .env
echo FTP_HOST=minilms.cafe24.com >> .env
echo FTP_PORT=21 >> .env
echo FTP_USER=minilms_ftp >> .env
echo FTP_PASSWORD=dodan1004 >> .env
echo. >> .env
echo # ==================== 관리자 계정 ==================== >> .env
echo ROOT_USER=root >> .env
echo ROOT_PASSWORD=xhRl1004!@# >> .env
echo. >> .env
echo # ==================== Google Client ID ==================== >> .env
echo GOOGLE_CLIENT_ID=770973091354-g59o434mblbigic50lsvl2vmgcif59er.apps.googleusercontent.com >> .env
```

### 또는 메모장으로 직접 생성
1. 메모장 열기
2. 다음 내용 복사 붙여넣기:

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
APP_VERSION=1.2.0
DEBUG=False
```

3. "다른 이름으로 저장" → 파일명: `.env` (점 포함!)
4. 파일 형식: "모든 파일 (*.*)"
5. 저장 위치: 프로젝트 루트 폴더

---

## 🛡️ .gitignore 확인

`.gitignore` 파일에 `.env`가 포함되어 있는지 확인:

```bash
# .gitignore 파일 확인
type .gitignore | findstr .env
```

**예상 출력**:
```
.env
.env.local
```

만약 없다면 `.gitignore`에 추가:
```bash
echo .env >> .gitignore
echo .env.local >> .gitignore
```

---

## 🔄 완전한 해결 플로우 (권장)

### 1단계: .env 백업
```bash
copy .env .env.backup
```

### 2단계: Git에서 .env 제거
```bash
git rm --cached .env
git commit -m "Remove .env from tracking (security)"
```

### 3단계: .gitignore 확인
```bash
type .gitignore | findstr .env
```

만약 없다면:
```bash
echo .env >> .gitignore
echo .env.local >> .gitignore
git add .gitignore
git commit -m "Add .env to .gitignore"
```

### 4단계: Pull 실행
```bash
git pull origin main
```

### 5단계: .env 복원
```bash
copy .env.backup .env
```

### 6단계: 확인
```bash
# Git 추적 안 되는지 확인
git status

# .env가 표시되지 않아야 정상 ✅
```

---

## 💡 왜 .env를 Git에 올리면 안 되나요?

### 보안 문제 🔐
```env
DB_PASSWORD=dodan1004        # ❌ 비밀번호 노출!
ROOT_PASSWORD=xhRl1004!@#    # ❌ 관리자 비밀번호 노출!
FTP_PASSWORD=dodan1004       # ❌ FTP 비밀번호 노출!
```

GitHub에 올라가면:
- ❌ 전 세계에 공개됨
- ❌ 해커의 표적이 됨
- ❌ 데이터베이스 해킹 위험
- ❌ 서버 침입 위험

### 올바른 방법 ✅
```
프로젝트
├── .env            ← Git 추적 안 함 (.gitignore)
├── .env.example    ← Git에 포함 (비밀번호 제거된 예시)
└── .gitignore      ← .env 제외
```

**.env.example** 예시:
```env
# ==================== 데이터베이스 설정 ====================
DB_HOST=your_host_here
DB_PORT=3306
DB_USER=your_username_here
DB_PASSWORD=your_password_here
DB_NAME=chungsan
```

---

## 🚨 긴급 상황: .env가 GitHub에 올라갔다면?

### 1단계: 비밀번호 즉시 변경
```
1. Cafe24 MySQL 비밀번호 변경
2. FTP 비밀번호 변경
3. ROOT 비밀번호 변경
4. .env 파일의 비밀번호 업데이트
```

### 2단계: Git 히스토리에서 완전 삭제
```bash
# BFG Repo-Cleaner 사용 (권장)
# 또는 git filter-branch 사용

# 전문가의 도움이 필요할 수 있습니다!
```

### 3단계: GitHub에서 확인
```
https://github.com/EmmettHwang/chungsan
→ 커밋 히스토리 검색
→ .env 파일이 보이면 완전히 제거되지 않은 것
```

---

## ✅ 정상 작동 확인

### Git 상태 확인
```bash
git status
```

**정상 출력**:
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

**.env가 표시되지 않아야 정상** ✅

### Pull 테스트
```bash
git pull origin main
```

**정상 출력**:
```
Already up to date.
```

또는
```
Updating 1205f8b..xxxxxxx
Fast-forward
 ...
```

---

## 📞 여전히 문제가 있다면?

### 에러 메시지 확인
```bash
git pull origin main 2>&1 | clip
```

에러 메시지를 클립보드에 복사했으니 공유해주세요!

### 현재 상태 확인
```bash
git status
git log --oneline -5
git ls-files | findstr .env
```

이 명령어들의 결과를 공유하시면 정확한 해결 방법을 안내해드리겠습니다!

---

## 🎯 요약

| 상황 | 해결 방법 |
|------|----------|
| .env 파일 충돌 | `.env` 백업 → 삭제 → pull → 복원 |
| .env가 Git 추적 중 | `git rm --cached .env` → 커밋 |
| .gitignore 누락 | `.env` 추가 → 커밋 |
| GitHub에 .env 노출 | 비밀번호 즉시 변경 → Git 히스토리 삭제 |

---

**만든 날짜**: 2026-02-08  
**버전**: v1.0  
**다음 단계**: .env 백업 → pull → 복원 🚀
