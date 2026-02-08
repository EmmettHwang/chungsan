# 청산에사르리랏다 (Chungsan Settlement System)

> 청산에 살어리랏다 청산에 살어리랏다  
> 멀위랑 다래랑 먹고 청산에 살어리랏다  
> 얄리얄리 얄랑셩 얄라리 얄라

**프로젝트 정산을 자동화하는 FastAPI 기반 시스템**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**버전**: v1.0.0  
**최종 업데이트**: 2026-02-08

---

## 🎯 주요 기능

- ✅ **참여자 관리**: 자동 코드 생성 (HUMAN-001, HUMAN-002...)
- ✅ **프로젝트 관리**: 수익 자동 계산 (총액 - 원가)
- ✅ **정산 계산**: 수익률 기반 자동 분배
- ✅ **5단계 권한**: admin, lead, senior, regular, assistant
- ✅ **API 문서**: Swagger UI / ReDoc 자동 생성
- ✅ **윈도우 지원**: 더블클릭으로 실행 가능

---

## 🚀 빠른 시작

### Windows 사용자 (가장 쉬운 방법)

1. **다운로드**
   ```
   https://github.com/EmmettHwang/chungsan
   Code → Download ZIP
   ```

2. **압축 해제 후 실행**
   ```
   start-windows.bat 더블클릭
   ```

3. **브라우저에서 확인**
   ```
   http://localhost:8001/docs
   ```

**완료! 🎉**

### 수동 실행 (CMD/PowerShell)

```cmd
# 1. 프로젝트 다운로드
git clone https://github.com/EmmettHwang/chungsan.git
cd chungsan

# 2. 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

---

## 📚 가이드 문서

| 문서 | 설명 | 대상 |
|------|------|------|
| [**QUICKSTART.md**](QUICKSTART.md) | ⚡ 5분 빠른 시작 | 초보자 |
| [**GUIDE_INDEX.md**](GUIDE_INDEX.md) | 📚 완벽한 가이드 모음 | 모든 사용자 |
| [**MANUAL_SETUP.md**](MANUAL_SETUP.md) | 🔧 윈도우 수동 실행 | 윈도우 사용자 |
| [**WINDOWS_SETUP.md**](WINDOWS_SETUP.md) | 🎯 윈도우 자동 실행 | 윈도우 사용자 |
| [**WINDOWS_GIT_GUIDE.md**](WINDOWS_GIT_GUIDE.md) | 🔗 Git 연동 가이드 | Git 사용자 |
| [**USAGE_EXAMPLES.md**](USAGE_EXAMPLES.md) | 📊 API 사용 예시 | API 사용자 |
| [**BACKEND_COMPLETE.md**](BACKEND_COMPLETE.md) | 💻 백엔드 구현 상세 | 개발자 |
| [**LOCAL_SETUP_GUIDE.md**](LOCAL_SETUP_GUIDE.md) | 🏠 로컬 실행 (Mac/Linux) | Mac/Linux 사용자 |

---

## 🔧 기술 스택

### 백엔드
- **FastAPI** - 고성능 비동기 웹 프레임워크
- **SQLAlchemy** - ORM (Object-Relational Mapping)
- **SQLite** - 내장 데이터베이스
- **Pydantic** - 데이터 검증
- **Uvicorn** - ASGI 서버

### 주요 기능
- RESTful API 설계
- 자동 API 문서 생성 (Swagger/ReDoc)
- CORS 지원
- 파일 업로드 지원

---

## 📁 프로젝트 구조

```
chungsan/
├── main.py                      # FastAPI 앱
├── requirements.txt             # Python 패키지
├── chungsan.db                  # SQLite DB
├── app/
│   ├── database.py              # DB 연결
│   ├── models.py                # 데이터 모델
│   ├── schemas.py               # API 스키마
│   └── routers/
│       ├── participants.py      # 참여자 API
│       ├── projects.py          # 프로젝트 API
│       └── settlements.py       # 정산 API
├── start-windows.bat            # Windows 실행 스크립트
├── start-windows.ps1            # PowerShell 스크립트
└── docs/                        # 가이드 문서
```

---

## 🌐 API 엔드포인트

### 참여자 관리
```
GET    /api/participants/          # 목록 조회
POST   /api/participants/          # 생성
GET    /api/participants/{id}      # 상세 조회
PUT    /api/participants/{id}      # 수정
DELETE /api/participants/{id}      # 삭제
```

### 프로젝트 관리
```
GET    /api/projects/              # 목록 조회
POST   /api/projects/              # 생성
GET    /api/projects/{id}          # 상세 조회
PUT    /api/projects/{id}          # 수정
DELETE /api/projects/{id}          # 삭제
```

### 프로젝트 참여자
```
GET    /api/projects/{id}/participants              # 참여자 목록
POST   /api/projects/{id}/participants              # 참여자 추가
PUT    /api/projects/{id}/participants/{pid}        # 수익률 수정
DELETE /api/projects/{id}/participants/{pid}        # 참여자 제거
```

### 정산
```
POST   /api/settlements/calculate  # 정산 계산
GET    /api/settlements/            # 정산 내역 조회
```

---

## 💡 사용 예시

### 1. 참여자 생성

```json
POST /api/participants/
{
  "name": "김동혁",
  "role": "admin",
  "default_profit_rate": 30.0,
  "phone": "010-1234-5678",
  "bank_name": "국민은행",
  "account_number": "123-456-789012"
}
```

### 2. 프로젝트 생성

```json
POST /api/projects/
{
  "name": "2024 교육 시스템 구축",
  "client": "우송대학교",
  "total_amount": 10000000,
  "cost": 3000000,
  "status": "completed"
}
```

### 3. 정산 계산

```json
POST /api/settlements/calculate
{
  "project_id": 1
}
```

**응답:**
```json
{
  "project_id": 1,
  "total_profit": 7000000.0,
  "settlements": [
    {
      "participant_name": "김동혁",
      "profit_rate": 30.0,
      "amount": 2100000.0
    }
  ]
}
```

---

## 🔢 정산 계산 로직

```
순이익 = 총액 - 원가
개인 정산액 = 순이익 × (개인 수익률 / 전체 수익률 합계)
```

**예시:**
- 총액: 10,000,000원
- 원가: 3,000,000원
- 순이익: 7,000,000원
- A (30%): 2,100,000원
- B (25%): 1,750,000원
- C (20%): 1,400,000원

---

## 🧪 테스트

### Swagger UI 사용
```
http://localhost:8001/docs
```

### curl 사용
```bash
# Health Check
curl http://localhost:8001/health

# 참여자 목록
curl http://localhost:8001/api/participants/

# 정산 계산
curl -X POST http://localhost:8001/api/settlements/calculate \
  -H "Content-Type: application/json" \
  -d '{"project_id": 1}'
```

---

## 🔧 문제 해결

### Python이 없다면?
https://www.python.org/downloads/ (3.8 이상)

### 가상환경 활성화 실패?
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 포트 충돌?
```cmd
uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```

자세한 문제 해결은 [MANUAL_SETUP.md](MANUAL_SETUP.md) 참고

---

## 📊 개발 로드맵

### v1.0 (완료) ✅
- [x] FastAPI 백엔드 구현
- [x] 참여자/프로젝트/정산 관리
- [x] 자동 코드 생성
- [x] 수익률 기반 정산
- [x] API 문서 자동 생성
- [x] 윈도우 실행 스크립트

### v1.1 (계획)
- [ ] 프론트엔드 UI 구현
- [ ] 대시보드 (참여자/프로젝트/정산)
- [ ] 통계 차트
- [ ] 엑셀 다운로드

### v2.0 (계획)
- [ ] 사용자 인증/권한
- [ ] 이메일 알림
- [ ] 정산 승인 워크플로우
- [ ] 다중 프로젝트 통합 정산

---

## 🤝 기여하기

### 버그 리포트
https://github.com/EmmettHwang/chungsan/issues

### Pull Request
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 라이선스

MIT License - 자유롭게 사용 가능합니다.

---

## 📞 연락처

- **GitHub**: https://github.com/EmmettHwang/chungsan
- **Issues**: https://github.com/EmmettHwang/chungsan/issues
- **Email**: (프로젝트 Issues 사용 권장)

---

## 🙏 감사의 말

이 프로젝트는 다음 기술들을 사용합니다:
- FastAPI - https://fastapi.tiangolo.com/
- SQLAlchemy - https://www.sqlalchemy.org/
- Pydantic - https://pydantic-docs.helpmanual.io/
- Uvicorn - https://www.uvicorn.org/

---

## 📅 변경 이력

| 버전 | 날짜 | 내용 |
|------|------|------|
| v1.0.0 | 2026-02-08 | FastAPI 백엔드 완전 구현 |
| v0.1.0 | 2026-02-06 | 프로젝트 초기화 |

---

**청산에사르리랏다 (Chungsan Settlement System)**  
**GitHub**: https://github.com/EmmettHwang/chungsan  
**버전**: v1.0.0  
**최종 업데이트**: 2026-02-08

**Happy Coding! 🚀**
