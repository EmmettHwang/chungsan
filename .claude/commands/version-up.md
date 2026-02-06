# 버전 올려 자동화

다음 단계를 순서대로 실행하세요:

## 1. 버전 증가
- `package.json`이 있으면 버전 증가 (patch 버전 +1)
- 없으면 `VERSION` 파일 생성/업데이트

## 2. README 정리
- README.md의 버전 정보 업데이트
- 변경 이력 섹션에 오늘 날짜와 버전 추가

## 3. 캐시 버스팅
- CSS/JS 파일에 버전 쿼리스트링 추가 (예: `?v=1.0.1`)
- HTML 파일 내 정적 자원 참조 업데이트

## 4. Git 작업
```bash
# 변경사항 스테이징
git add -A

# 커밋 (버전 번호 포함)
git commit -m "chore: bump version to {새버전}"

# 현재 브랜치 푸시
git push origin HEAD

# main 브랜치로 머지 (PR 또는 직접 머지)
git checkout main
git merge {현재브랜치} --no-edit
git push origin main

# 원래 브랜치로 복귀
git checkout {현재브랜치}
```

## 5. 완료 보고
- 이전 버전 → 새 버전 출력
- 수행된 작업 요약
