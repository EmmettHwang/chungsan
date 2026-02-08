# 📚 청산에사르리랏다 - 완벽한 가이드 모음

> **프로젝트**: 청산에사르리랏다 (Chungsan Settlement System)  
> **버전**: v1.0.0  
> **작성일**: 2026-02-08  
> **GitHub**: https://github.com/EmmettHwang/chungsan

---

## 🎯 시작하기 전에

**청산에사르리랏다**는 프로젝트 정산을 자동화하는 FastAPI 기반 시스템입니다.

### 주요 기능
- ✅ **참여자 관리**: 자동 코드 생성 (HUMAN-001, HUMAN-002...)
- ✅ **프로젝트 관리**: 수익 자동 계산
- ✅ **정산 계산**: 수익률 기반 자동 분배
- ✅ **5단계 권한**: admin, lead, senior, regular, assistant

---

## 📖 가이드 문서 목록

### 🚀 빠른 시작 (초보자)

#### 1. **QUICKSTART.md** - 5분 빠른 시작 ⚡
```
5분 안에 실행하고 첫 정산 계산하기
```

**이런 분께 추천:**
- 프로그래밍 초보자
- 빨리 실행해보고 싶은 분
- 간단한 테스트만 원하는 분

**주요 내용:**
- 5분 완성 가이드
- 한 번에 복사 가능한 명령어
- Swagger UI 테스트 방법
- 첫 정산 계산 튜토리얼

**파일 경로:** `/QUICKSTART.md`

---

### 🪟 윈도우 사용자

#### 2. **MANUAL_SETUP.md** - 수동 실행 가이드 🔧
```
CMD, PowerShell, Git Bash로 직접 실행하기
```

**이런 분께 추천:**
- 수동으로 제어하고 싶은 분
- 자동 스크립트가 안 될 때
- 단계별로 이해하며 실행하고 싶은 분

**주요 내용:**
- CMD 실행 방법
- PowerShell 실행 방법
- Git Bash 실행 방법
- 문제 해결 가이드 (상세)
- 프로젝트 구조 설명

**파일 경로:** `/MANUAL_SETUP.md`

---

#### 3. **WINDOWS_SETUP.md** - 자동 실행 가이드 🎯
```
start-windows.bat 더블클릭으로 자동 실행
```

**이런 분께 추천:**
- 가장 쉬운 방법을 원하는 분
- 명령어 입력이 어려운 분
- 한 번의 클릭으로 실행하고 싶은 분

**주요 내용:**
- 자동 실행 배치 파일 사용법
- PowerShell 스크립트 사용법
- 자동화 스크립트 설명

**파일 경로:** `/WINDOWS_SETUP.md`

---

#### 4. **WINDOWS_GIT_GUIDE.md** - Git 연동 가이드 🔗
```
GitHub Desktop, Git CMD, VS Code로 Git 사용하기
```

**이런 분께 추천:**
- GitHub와 연동하고 싶은 분
- 코드 수정 후 커밋/푸시하고 싶은 분
- Git이 처음인 분

**주요 내용:**
- GitHub Desktop 사용법 (추천)
- Git CMD/PowerShell 명령어
- VS Code Git 통합
- Personal Access Token (PAT) 설정
- 자주 발생하는 오류 해결

**파일 경로:** `/WINDOWS_GIT_GUIDE.md`

---

### 📱 API 사용법

#### 5. **USAGE_EXAMPLES.md** - API 사용 예시 📊
```
실전 시나리오와 함께하는 API 완벽 가이드
```

**이런 분께 추천:**
- API 사용법을 배우고 싶은 분
- 실전 예시가 필요한 분
- curl 명령어를 사용하는 분

**주요 내용:**
- 참여자 관리 예시
- 프로젝트 관리 예시
- 정산 계산 예시
- 실전 시나리오 (5명 팀 프로젝트)
- 수익률 계산 로직 설명

**파일 경로:** `/USAGE_EXAMPLES.md`

---

### 💻 개발자용

#### 6. **BACKEND_COMPLETE.md** - 백엔드 구현 상세 🔧
```
FastAPI 백엔드 아키텍처 및 구현 세부사항
```

**이런 분께 추천:**
- 코드를 이해하고 싶은 분
- 기능을 추가/수정하고 싶은 분
- 백엔드 개발자

**주요 내용:**
- 데이터베이스 스키마
- API 엔드포인트 상세
- 코드 구조 설명
- 테스트 결과
- 향후 개선 사항

**파일 경로:** `/BACKEND_COMPLETE.md`

---

#### 7. **LOCAL_SETUP_GUIDE.md** - 로컬 실행 가이드 🏠
```
macOS, Linux 환경에서 실행하기
```

**이런 분께 추천:**
- macOS/Linux 사용자
- 전체 설치 프로세스를 원하는 분
- Python 가상환경에 익숙한 분

**주요 내용:**
- Python 3.8+ 설치
- 가상환경 생성
- 패키지 설치
- 서버 실행
- 트러블슈팅

**파일 경로:** `/LOCAL_SETUP_GUIDE.md`

---

### 📝 프로젝트 정보

#### 8. **README.md** - 프로젝트 소개 📋
```
프로젝트 개요 및 기본 정보
```

**주요 내용:**
- 프로젝트 소개
- 주요 기능
- 기술 스택
- 빠른 시작 링크

**파일 경로:** `/README.md`

---

## 🗺️ 가이드 선택 플로우차트

```
시작
  │
  ├─ 프로그래밍 초보자?
  │   └─ YES → QUICKSTART.md (5분 빠른 시작)
  │
  ├─ 윈도우 사용자?
  │   ├─ 가장 쉬운 방법? → WINDOWS_SETUP.md (자동 실행)
  │   ├─ 수동으로 제어? → MANUAL_SETUP.md (수동 실행)
  │   └─ Git 연동 필요? → WINDOWS_GIT_GUIDE.md
  │
  ├─ API 사용법 배우기
  │   └─ USAGE_EXAMPLES.md (실전 예시)
  │
  ├─ 개발자 (코드 이해/수정)
  │   ├─ 백엔드 상세 → BACKEND_COMPLETE.md
  │   └─ 로컬 환경 → LOCAL_SETUP_GUIDE.md
  │
  └─ 프로젝트 정보
      └─ README.md
```

---

## 🎯 추천 학습 경로

### 🌱 초보자 경로

1. **README.md** - 프로젝트가 뭔지 이해하기
2. **QUICKSTART.md** - 5분 안에 실행해보기
3. **USAGE_EXAMPLES.md** - API 사용법 배우기
4. **WINDOWS_GIT_GUIDE.md** - Git 연동하기 (선택)

### 💼 실무자 경로

1. **MANUAL_SETUP.md** - 제대로 설치하기
2. **USAGE_EXAMPLES.md** - 실전 시나리오 익히기
3. **WINDOWS_GIT_GUIDE.md** - Git으로 협업하기
4. **BACKEND_COMPLETE.md** - 시스템 이해하기 (선택)

### 👨‍💻 개발자 경로

1. **BACKEND_COMPLETE.md** - 백엔드 아키텍처 이해
2. **LOCAL_SETUP_GUIDE.md** - 개발 환경 구축
3. **USAGE_EXAMPLES.md** - API 테스트
4. **WINDOWS_GIT_GUIDE.md** - Git 워크플로우

---

## 📂 전체 파일 구조

```
chungsan/
├── 📋 가이드 문서 (Guide Documents)
│   ├── README.md                    # 프로젝트 소개
│   ├── QUICKSTART.md                # ⚡ 5분 빠른 시작
│   ├── MANUAL_SETUP.md              # 🔧 수동 실행 (Windows)
│   ├── WINDOWS_SETUP.md             # 🎯 자동 실행 (Windows)
│   ├── WINDOWS_GIT_GUIDE.md         # 🔗 Git 연동 (Windows)
│   ├── USAGE_EXAMPLES.md            # 📊 API 사용 예시
│   ├── BACKEND_COMPLETE.md          # 💻 백엔드 상세
│   ├── LOCAL_SETUP_GUIDE.md         # 🏠 로컬 실행 (All OS)
│   └── GUIDE_INDEX.md               # 📚 이 문서!
│
├── 🚀 실행 스크립트 (Execution Scripts)
│   ├── start-windows.bat            # Windows 배치 파일
│   └── start-windows.ps1            # PowerShell 스크립트
│
├── ⚙️ 백엔드 소스 (Backend Source)
│   ├── main.py                      # FastAPI 앱
│   ├── requirements.txt             # Python 패키지
│   ├── chungsan.db                  # SQLite DB
│   └── app/
│       ├── database.py              # DB 연결
│       ├── models.py                # 데이터 모델
│       ├── schemas.py               # API 스키마
│       └── routers/
│           ├── participants.py      # 참여자 API
│           ├── projects.py          # 프로젝트 API
│           └── settlements.py       # 정산 API
│
├── 📁 디렉토리 (Directories)
│   ├── venv/                        # 가상환경 (자동 생성)
│   ├── uploads/                     # 업로드 파일
│   └── static/                      # 정적 파일
│
└── 🔧 설정 파일 (Configuration)
    ├── .gitignore                   # Git 제외 파일
    └── VERSION                      # 버전 정보
```

---

## 💡 자주 묻는 질문 (FAQ)

### Q1: 어떤 가이드를 먼저 봐야 하나요?

**프로그래밍 초보자:**
→ `QUICKSTART.md` (5분 빠른 시작)

**윈도우 사용자 (일반):**
→ `WINDOWS_SETUP.md` (자동 실행) 또는 `MANUAL_SETUP.md` (수동 실행)

**개발자:**
→ `BACKEND_COMPLETE.md` + `LOCAL_SETUP_GUIDE.md`

### Q2: 자동 실행 스크립트가 안 돼요!

→ `MANUAL_SETUP.md`의 문제 해결 섹션 참고
→ PowerShell 실행 정책 변경 필요할 수 있음

### Q3: API를 어떻게 사용하나요?

→ `USAGE_EXAMPLES.md`의 실전 시나리오 참고
→ Swagger UI (http://localhost:8001/docs) 사용

### Q4: Git/GitHub 연동은 어떻게 하나요?

→ `WINDOWS_GIT_GUIDE.md` 참고
→ GitHub Desktop 사용 추천 (가장 쉬움)

### Q5: 코드를 수정하고 싶어요!

→ `BACKEND_COMPLETE.md`에서 구조 파악
→ `WINDOWS_GIT_GUIDE.md`로 Git 설정
→ 수정 후 커밋/푸시

---

## 🌐 유용한 링크

### 프로젝트 링크
- **GitHub 저장소**: https://github.com/EmmettHwang/chungsan
- **Issues**: https://github.com/EmmettHwang/chungsan/issues
- **Releases**: https://github.com/EmmettHwang/chungsan/releases

### 서버 실행 후
- **API 문서 (Swagger)**: http://localhost:8001/docs
- **API 문서 (ReDoc)**: http://localhost:8001/redoc
- **Health Check**: http://localhost:8001/health

### 외부 리소스
- **Python 다운로드**: https://www.python.org/downloads/
- **Git 다운로드**: https://git-scm.com/downloads
- **GitHub Desktop**: https://desktop.github.com/
- **VS Code**: https://code.visualstudio.com/

---

## 📊 가이드 비교표

| 가이드 | 대상 | 난이도 | 소요 시간 | 추천도 |
|--------|------|--------|-----------|--------|
| **QUICKSTART.md** | 초보자 | ⭐ | 5분 | ⭐⭐⭐⭐⭐ |
| **WINDOWS_SETUP.md** | 윈도우 (자동) | ⭐ | 2분 | ⭐⭐⭐⭐⭐ |
| **MANUAL_SETUP.md** | 윈도우 (수동) | ⭐⭐ | 10분 | ⭐⭐⭐⭐ |
| **WINDOWS_GIT_GUIDE.md** | Git 사용자 | ⭐⭐ | 15분 | ⭐⭐⭐⭐ |
| **USAGE_EXAMPLES.md** | API 사용자 | ⭐⭐ | 20분 | ⭐⭐⭐⭐⭐ |
| **BACKEND_COMPLETE.md** | 개발자 | ⭐⭐⭐ | 30분 | ⭐⭐⭐⭐ |
| **LOCAL_SETUP_GUIDE.md** | Mac/Linux | ⭐⭐ | 10분 | ⭐⭐⭐⭐ |

---

## 🎓 학습 체크리스트

### 기본 사용자

- [ ] 프로젝트 소개 읽기 (README.md)
- [ ] 5분 빠른 시작 완료 (QUICKSTART.md)
- [ ] 참여자 생성해보기
- [ ] 프로젝트 생성해보기
- [ ] 정산 계산해보기
- [ ] Swagger UI 사용해보기

### 중급 사용자

- [ ] 수동 설치 완료 (MANUAL_SETUP.md)
- [ ] Git 연동 완료 (WINDOWS_GIT_GUIDE.md)
- [ ] API 사용 예시 따라하기 (USAGE_EXAMPLES.md)
- [ ] 5명 팀 프로젝트 정산해보기
- [ ] 수익률 조정해보기
- [ ] curl로 API 호출해보기

### 고급 사용자/개발자

- [ ] 백엔드 아키텍처 이해 (BACKEND_COMPLETE.md)
- [ ] 로컬 개발 환경 구축 (LOCAL_SETUP_GUIDE.md)
- [ ] 코드 리뷰 및 이해
- [ ] Git으로 코드 수정/커밋/푸시
- [ ] 새 기능 추가해보기
- [ ] Pull Request 생성해보기

---

## 🆘 도움이 필요하신가요?

### 1. 가이드 문서 확인
위의 가이드 목록에서 상황에 맞는 문서를 찾아보세요.

### 2. FAQ 확인
각 가이드 문서의 "문제 해결" 또는 "FAQ" 섹션을 참고하세요.

### 3. GitHub Issues
https://github.com/EmmettHwang/chungsan/issues

버그 리포트나 기능 요청은 이곳에 남겨주세요!

### 4. 커뮤니티
- GitHub Discussions (추후 오픈 예정)
- 프로젝트 Wiki (작성 중)

---

## 📅 버전 히스토리

### v1.0.0 (2026-02-08)
- ✅ FastAPI 백엔드 구현 완료
- ✅ 참여자/프로젝트/정산 관리 API
- ✅ 윈도우 실행 스크립트
- ✅ 완벽한 가이드 문서 세트

---

## 🎉 축하합니다!

이제 **청산에사르리랏다**를 완벽하게 활용할 수 있습니다!

### 다음 단계

1. **즉시 시작**: `QUICKSTART.md`로 5분 안에 실행
2. **API 배우기**: `USAGE_EXAMPLES.md`로 사용법 익히기
3. **Git 연동**: `WINDOWS_GIT_GUIDE.md`로 협업 시작
4. **기여하기**: GitHub에서 이슈/PR 생성

---

**청산에사르리랏다 (Chungsan Settlement System)**  
**버전**: v1.0.0  
**GitHub**: https://github.com/EmmettHwang/chungsan  
**작성일**: 2026-02-08

**Happy Coding! 🚀**
