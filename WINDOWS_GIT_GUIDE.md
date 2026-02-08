# 윈도우에서 GitHub 연동하기

## 🎯 목표
윈도우에서 청산에사르리랏다 프로젝트를 GitHub에서 다운로드하고, 수정한 내용을 다시 푸시하기

---

## 📋 방법 1: GitHub Desktop (가장 쉬움! 추천)

### 1️⃣ GitHub Desktop 설치
1. https://desktop.github.com/ 접속
2. "Download for Windows" 클릭
3. 설치 파일 실행

### 2️⃣ GitHub 계정 로그인
1. GitHub Desktop 실행
2. **File** → **Options** → **Accounts**
3. **Sign in** 클릭
4. 브라우저에서 GitHub 로그인
5. GitHub Desktop 승인

### 3️⃣ 저장소 클론
1. **File** → **Clone repository**
2. **URL** 탭 선택
3. Repository URL 입력:
   ```
   https://github.com/EmmettHwang/chungsan
   ```
4. Local path 선택 (예: `C:\Projects\chungsan`)
5. **Clone** 클릭

### 4️⃣ 수정 후 커밋 & 푸시
1. 파일 수정 (VS Code, 메모장 등)
2. GitHub Desktop에서 변경사항 확인
3. 왼쪽 하단에 커밋 메시지 입력:
   ```
   feat: 새로운 기능 추가
   ```
4. **Commit to main** 클릭
5. 상단 **Push origin** 클릭

✅ **끝!** GitHub에 푸시 완료!

---

## 📋 방법 2: Git 명령어 (CMD/PowerShell)

### 1️⃣ Git 설치
1. https://git-scm.com/download/win 접속
2. 설치 파일 다운로드 및 실행
3. 모든 기본 설정 그대로 **Next** (추천)

### 2️⃣ Git 설정
**CMD 또는 PowerShell 열기** (Win + R → cmd 또는 powershell)

```cmd
REM Git 사용자 정보 설정
git config --global user.name "EmmettHwang"
git config --global user.email "dhhwang@wsu.ac.kr"

REM 설정 확인
git config --list
```

### 3️⃣ 저장소 클론
```cmd
REM 프로젝트를 저장할 폴더로 이동
cd C:\Projects

REM GitHub 저장소 클론
git clone https://github.com/EmmettHwang/chungsan.git

REM 폴더 이동
cd chungsan
```

### 4️⃣ 파일 수정 후 커밋
```cmd
REM 파일 수정 (메모장, VS Code 등으로)
notepad main.py

REM 변경사항 확인
git status

REM 모든 변경사항 스테이징
git add .

REM 또는 특정 파일만
git add main.py

REM 커밋
git commit -m "feat: 새로운 기능 추가"

REM GitHub에 푸시
git push origin main
```

### 5️⃣ 최신 코드 가져오기
```cmd
REM 다른 컴퓨터에서 수정한 내용 가져오기
git pull origin main
```

---

## 📋 방법 3: VS Code에서 Git 사용

### 1️⃣ VS Code 설치
1. https://code.visualstudio.com/ 접속
2. "Download for Windows" 클릭
3. 설치

### 2️⃣ Git 설치 (위 방법 2-1 참고)

### 3️⃣ VS Code에서 저장소 클론
1. VS Code 실행
2. **Ctrl + Shift + P** (명령 팔레트)
3. "Git: Clone" 입력 및 선택
4. Repository URL 입력:
   ```
   https://github.com/EmmettHwang/chungsan
   ```
5. 저장할 폴더 선택
6. **Open** 클릭

### 4️⃣ VS Code에서 커밋 & 푸시
1. 파일 수정
2. 왼쪽 **Source Control** 아이콘 클릭 (Ctrl + Shift + G)
3. 변경사항 확인
4. 메시지 입력 후 **✓ Commit** 클릭
5. **...** → **Push** 클릭

---

## 🔐 GitHub 인증 방법

### Windows Credential Manager 사용 (추천)
Git 설치 시 자동으로 설정됨. 처음 푸시 시:

1. `git push` 실행
2. 브라우저가 열리며 GitHub 로그인 요청
3. 로그인 완료 → 자동으로 저장됨
4. 다음부터는 자동 로그인!

### Personal Access Token (PAT) 사용
비밀번호 대신 토큰 사용 (더 안전)

#### 1. GitHub에서 토큰 생성
1. GitHub 로그인 → **Settings**
2. **Developer settings** → **Personal access tokens** → **Tokens (classic)**
3. **Generate new token** → **Generate new token (classic)**
4. Note: `chungsan-windows` (이름)
5. Expiration: `No expiration` (만료 없음) 또는 원하는 기간
6. 권한 선택:
   - ✅ **repo** (전체)
7. **Generate token** 클릭
8. 🔥 **토큰 복사** (다시 볼 수 없음!)

#### 2. 토큰으로 푸시
```cmd
REM HTTPS URL에 토큰 포함
git remote set-url origin https://토큰@github.com/EmmettHwang/chungsan.git

REM 예시 (토큰이 ghp_xxxx라면)
git remote set-url origin https://ghp_abcd1234@github.com/EmmettHwang/chungsan.git

REM 확인
git remote -v

REM 푸시
git push origin main
```

---

## 🔧 일반적인 Git 명령어

### 기본 워크플로우
```cmd
REM 1. 최신 코드 가져오기
git pull origin main

REM 2. 파일 수정

REM 3. 상태 확인
git status

REM 4. 변경사항 스테이징
git add .

REM 5. 커밋
git commit -m "feat: 새 기능 추가"

REM 6. 푸시
git push origin main
```

### 유용한 명령어
```cmd
REM 변경 내역 보기
git log --oneline -5

REM 마지막 커밋 취소 (파일은 유지)
git reset --soft HEAD~1

REM 특정 파일만 되돌리기
git checkout -- main.py

REM 브랜치 목록
git branch

REM 새 브랜치 생성 및 전환
git checkout -b feature/new-feature

REM 원격 저장소 확인
git remote -v

REM 원격 저장소 변경사항 확인 (가져오지 않고)
git fetch

REM 커밋 메시지 수정 (마지막 커밋)
git commit --amend -m "새 메시지"
```

---

## 📝 커밋 메시지 규칙

### 형식
```
타입: 제목

상세 설명 (선택)
```

### 타입
- `feat:` - 새로운 기능
- `fix:` - 버그 수정
- `docs:` - 문서 수정
- `style:` - 코드 포맷팅
- `refactor:` - 리팩토링
- `test:` - 테스트 추가
- `chore:` - 기타 작업

### 예시
```cmd
git commit -m "feat: 참여자 삭제 기능 추가"

git commit -m "fix: 정산 계산 오류 수정"

git commit -m "docs: README 업데이트"
```

---

## ⚡ 빠른 시작 (Windows)

### GitHub Desktop으로 (1분!)
```
1. GitHub Desktop 설치 → 로그인
2. Clone repository → URL: https://github.com/EmmettHwang/chungsan
3. 파일 수정
4. Commit → Push
```

### Git 명령어로 (2분!)
```cmd
1. Git 설치
2. cmd 열기
3. git clone https://github.com/EmmettHwang/chungsan.git
4. cd chungsan
5. notepad main.py (수정)
6. git add .
7. git commit -m "feat: 수정"
8. git push origin main
```

---

## 🔥 자주 발생하는 오류 해결

### ❌ "Permission denied"
**원인**: 인증 실패

**해결**:
```cmd
REM 1. 자격 증명 다시 입력
git config --global credential.helper manager

REM 2. 푸시 시도
git push origin main

REM 3. 로그인 창이 뜨면 GitHub 계정으로 로그인
```

### ❌ "fatal: not a git repository"
**원인**: Git 저장소가 아닌 폴더

**해결**:
```cmd
REM 올바른 폴더로 이동
cd C:\Projects\chungsan

REM 또는 Git 저장소 초기화
git init
git remote add origin https://github.com/EmmettHwang/chungsan.git
```

### ❌ "Updates were rejected"
**원인**: 원격 저장소가 더 최신

**해결**:
```cmd
REM 1. 최신 코드 가져오기
git pull origin main --rebase

REM 2. 충돌 해결 (있다면)
REM 3. 다시 푸시
git push origin main
```

### ❌ 한글 파일명 깨짐
**해결**:
```cmd
git config --global core.quotepath false
```

---

## 🎯 청산에사르리랏다 프로젝트 클론부터 실행까지

### 전체 과정 (Windows)
```cmd
REM 1. 프로젝트 폴더로 이동
cd C:\Projects

REM 2. Git 클론
git clone https://github.com/EmmettHwang/chungsan.git

REM 3. 폴더 이동
cd chungsan

REM 4. 서버 실행
start-windows.bat

REM 또는 수동 실행
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### 수정 후 푸시
```cmd
REM 파일 수정 후...

git add .
git commit -m "feat: 새로운 기능 추가"
git push origin main
```

---

## 🌟 추천 도구

### 1. GitHub Desktop
- **장점**: GUI, 쉬움, 초보자 친화적
- **다운로드**: https://desktop.github.com/

### 2. VS Code + Git
- **장점**: 코드 편집 + Git 통합
- **다운로드**: https://code.visualstudio.com/

### 3. Git CMD/PowerShell
- **장점**: 강력함, 자동화 가능
- **다운로드**: https://git-scm.com/

---

## 📚 추가 학습 자료

### Git 기초
- https://git-scm.com/book/ko/v2
- https://learngitbranching.js.org/?locale=ko

### GitHub 사용법
- https://docs.github.com/ko

### VS Code Git 사용
- https://code.visualstudio.com/docs/sourcecontrol/overview

---

**생성 일시**: 2026-02-08  
**프로젝트**: 청산에사르리랏다  
**GitHub**: https://github.com/EmmettHwang/chungsan  
**문서**: WINDOWS_GIT_GUIDE.md
