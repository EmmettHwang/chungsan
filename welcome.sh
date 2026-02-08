#!/bin/bash

# 청산에사르리랏다 웰컴 메시지 및 시스템 상태 보고 스크립트

echo ""
echo "🎉 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 🎉"
echo "   청산에사르리랏다 (Chungsan Settlement System)"
echo "   소프트웨어 및 하드웨어 개발 납품 프로젝트의 정산 관리 시스템"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 📦 버전 정보
echo "📦 버전 정보"
if [ -f "README.md" ]; then
    VERSION=$(grep -oP "(?<=버전\*\*: v)[0-9.]+" README.md | head -1)
    if [ -z "$VERSION" ]; then
        VERSION="unknown"
    fi
    echo "   현재 버전: v${VERSION}"
else
    echo "   README.md 파일을 찾을 수 없습니다."
fi
echo ""

# 🔧 Git 상태
echo "🔧 Git 상태"
CURRENT_BRANCH=$(git branch --show-current 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "   현재 브랜치: ${CURRENT_BRANCH}"
    
    # 변경사항 확인
    CHANGES=$(git status --short 2>/dev/null | wc -l)
    if [ $CHANGES -eq 0 ]; then
        echo "   상태: ✅ Clean (변경사항 없음)"
    else
        echo "   상태: ⚠️  ${CHANGES}개의 변경사항 있음"
        git status --short | head -5
    fi
    
    # 마지막 커밋
    LAST_COMMIT=$(git log -1 --oneline 2>/dev/null)
    echo "   마지막 커밋: ${LAST_COMMIT}"
    
    # main과의 차이
    DIFF_COUNT=$(git log main..HEAD --oneline 2>/dev/null | wc -l)
    if [ $DIFF_COUNT -gt 0 ]; then
        echo "   main과의 차이: ${DIFF_COUNT}개의 커밋 앞서 있음"
    else
        echo "   main과의 차이: 동기화됨"
    fi
else
    echo "   ⚠️  Git 저장소가 아닙니다."
fi
echo ""

# 🌿 브랜치 목록
echo "🌿 브랜치 목록"
git branch 2>/dev/null | head -5 || echo "   브랜치 정보를 가져올 수 없습니다."
echo ""

# 🚀 시스템 상태
echo "🚀 시스템 상태"

# 백엔드 서버 상태
if pgrep -f "uvicorn.*main:app" > /dev/null; then
    PORT=$(pgrep -f "uvicorn.*main:app" -a | grep -oP "(?<=--port )\d+" | head -1)
    echo "   백엔드 서버: ✅ 실행 중 (포트: ${PORT:-8000})"
else
    echo "   백엔드 서버: ❌ 중지됨"
fi

# 데이터베이스 연결
if command -v mysql &> /dev/null; then
    if mysql -u root -e "SELECT 1" &> /dev/null; then
        echo "   MySQL: ✅ 연결 가능"
    else
        echo "   MySQL: ⚠️  연결 실패 (인증 필요할 수 있음)"
    fi
else
    echo "   MySQL: ⚠️  클라이언트 미설치"
fi

# 포트 사용 확인
if netstat -tuln 2>/dev/null | grep -q ":8000 "; then
    echo "   포트 8000: ✅ 사용 중"
else
    echo "   포트 8000: ❌ 사용 가능"
fi

# 디스크 공간
DISK_USAGE=$(df -h . | awk 'NR==2 {print $5}')
echo "   디스크 사용량: ${DISK_USAGE}"

echo ""

# 📝 최근 로그
echo "📝 최근 로그 (backend/logs/)"
if [ -d "backend/logs" ]; then
    LATEST_LOG=$(ls -t backend/logs/*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        echo "   최근 로그 파일: $(basename $LATEST_LOG)"
        ERROR_COUNT=$(grep -i "error\|exception" "$LATEST_LOG" 2>/dev/null | wc -l)
        echo "   에러 수: ${ERROR_COUNT}개"
    else
        echo "   로그 파일을 찾을 수 없습니다."
    fi
else
    echo "   로그 디렉토리가 없습니다."
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "💡 명령어:"
echo "   - 버전 올려: 버전 업데이트 및 배포 프로세스 실행"
echo "   - git status: 상세한 Git 상태 확인"
echo "   - ./start.sh: 시스템 시작"
echo "   - ./stop.sh: 시스템 종료"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
