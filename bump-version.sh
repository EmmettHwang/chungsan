#!/bin/bash

# 청산에사르리랏다 버전 업데이트 자동화 스크립트
# "버전 올려" 명령어 실행 시 자동으로 수행

set -e  # 에러 발생 시 중단

echo ""
echo "🚀 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   청산에사르리랏다 버전 업데이트 시작"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 현재 브랜치 저장
CURRENT_BRANCH=$(git branch --show-current)
echo "📍 현재 브랜치: ${CURRENT_BRANCH}"

# 변경사항 확인
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  변경사항이 감지되었습니다."
    git status --short
    echo ""
else
    echo "✅ 작업 디렉토리가 깨끗합니다."
fi

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣ 버전 번호 증가
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "1️⃣  버전 번호 증가 중..."

# README.md에서 현재 버전 추출
CURRENT_VERSION=$(grep -oP "(?<=버전\*\*: v)[0-9.]+" README.md | head -1)

if [ -z "$CURRENT_VERSION" ]; then
    echo "❌ 현재 버전을 찾을 수 없습니다."
    exit 1
fi

echo "   현재 버전: v${CURRENT_VERSION}"

# 버전 분리 (v5.6.9 -> 5, 6, 9)
IFS='.' read -ra VERSION_PARTS <<< "$CURRENT_VERSION"
MAJOR=${VERSION_PARTS[0]}
MINOR=${VERSION_PARTS[1]}
PATCH=${VERSION_PARTS[2]%%.*}

# 버전 업데이트 선택
echo ""
echo "   버전 업데이트 유형을 선택하세요:"
echo "   1) Patch (v${MAJOR}.${MINOR}.${PATCH} → v${MAJOR}.${MINOR}.$((PATCH + 1)))"
echo "   2) Minor (v${MAJOR}.${MINOR}.${PATCH} → v${MAJOR}.$((MINOR + 1)).0)"
echo "   3) Major (v${MAJOR}.${MINOR}.${PATCH} → v$((MAJOR + 1)).0.0)"
echo ""
read -p "   선택 (1/2/3): " VERSION_TYPE

case $VERSION_TYPE in
    1)
        NEW_VERSION="${MAJOR}.${MINOR}.$((PATCH + 1))"
        ;;
    2)
        NEW_VERSION="${MAJOR}.$((MINOR + 1)).0"
        ;;
    3)
        NEW_VERSION="$((MAJOR + 1)).0.0"
        ;;
    *)
        echo "❌ 잘못된 선택입니다."
        exit 1
        ;;
esac

# 타임스탬프 생성 (YYYYMMDDHHMM 형식)
TIMESTAMP=$(date +"%Y%m%d%H%M")
NEW_VERSION_FULL="${NEW_VERSION}.${TIMESTAMP}"

echo "   ✅ 새 버전: v${NEW_VERSION_FULL}"

# README.md 버전 업데이트
sed -i "s/버전\*\*: v[0-9.]*/버전**: v${NEW_VERSION_FULL}/" README.md
echo "   ✅ README.md 버전 업데이트 완료"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2️⃣ README.md 정리
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "2️⃣  README.md 정리 중..."

# 변경 내역 입력
echo ""
read -p "   📝 주요 변경사항을 입력하세요: " CHANGE_SUMMARY

# README.md 상단에 변경사항 추가
CURRENT_DATE=$(date +"%Y-%m-%d")
CHANGE_ENTRY="### ✅ 최신 업데이트 (v${NEW_VERSION}, ${CURRENT_DATE})\n\n${CHANGE_SUMMARY}\n"

# 임시 파일 생성
TMP_FILE=$(mktemp)
echo -e "${CHANGE_ENTRY}\n" > "$TMP_FILE"
cat README.md >> "$TMP_FILE"
mv "$TMP_FILE" README.md

echo "   ✅ README.md 변경사항 추가 완료"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3️⃣ 캐시 버스팅 정리
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "3️⃣  캐시 버스팅 정리 중..."

# frontend/app.js의 APP_VERSION 업데이트
if [ -f "frontend/app.js" ]; then
    sed -i "s/let APP_VERSION = '[^']*'/let APP_VERSION = 'v${NEW_VERSION_FULL}'/" frontend/app.js
    echo "   ✅ frontend/app.js APP_VERSION 업데이트"
fi

# Service Worker 버전 업데이트
if [ -f "frontend/service-worker.js" ]; then
    sed -i "s/const CACHE_VERSION = '[^']*'/const CACHE_VERSION = 'v${NEW_VERSION_FULL}'/" frontend/service-worker.js
    echo "   ✅ Service Worker 캐시 버전 업데이트"
fi

echo "   ✅ 캐시 버스팅 완료"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4️⃣ Git 커밋
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "4️⃣  Git 커밋 중..."

git add .
git commit -m "chore: bump version to v${NEW_VERSION_FULL}

${CHANGE_SUMMARY}

- 버전 업데이트: v${CURRENT_VERSION} → v${NEW_VERSION_FULL}
- README.md 업데이트
- 캐시 버스팅 적용"

echo "   ✅ 커밋 완료"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5️⃣ Git Push
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "5️⃣  Git Push 중..."

git push origin "${CURRENT_BRANCH}"

echo "   ✅ ${CURRENT_BRANCH} 브랜치 푸시 완료"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 6️⃣ Main 브랜치에 병합
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "6️⃣  Main 브랜치에 병합 중..."

# main 브랜치로 체크아웃
git checkout main

# 최신 상태로 업데이트
git pull origin main

# 현재 브랜치 병합
git merge "${CURRENT_BRANCH}" --no-ff -m "Merge ${CURRENT_BRANCH} into main (v${NEW_VERSION_FULL})"

# main 브랜치 푸시
git push origin main

echo "   ✅ Main 브랜치 병합 및 푸시 완료"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 7️⃣ 작업 브랜치로 복귀
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "7️⃣  작업 브랜치로 복귀 중..."

git checkout "${CURRENT_BRANCH}"

echo "   ✅ ${CURRENT_BRANCH} 브랜치로 복귀 완료"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 완료
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 버전 업데이트 완료!"
echo ""
echo "   📦 새 버전: v${NEW_VERSION_FULL}"
echo "   📝 변경사항: ${CHANGE_SUMMARY}"
echo "   🌿 현재 브랜치: ${CURRENT_BRANCH}"
echo "   ✅ Main 브랜치 동기화 완료"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
