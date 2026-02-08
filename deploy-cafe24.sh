#!/bin/bash

# 청산에사르리랏다 Cafe24 서버 배포 스크립트

set -e  # 에러 발생 시 중단

echo ""
echo "🚀 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   청산에사르리랏다 Cafe24 서버 배포"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 서버 정보
SSH_HOST="minilms.cafe24.com"
SSH_USER="root"
SSH_PORT="22"
REMOTE_PATH="/home/hosting_users/minilms/www"  # 실제 경로로 수정 필요

echo "📍 서버 정보"
echo "   호스트: ${SSH_HOST}"
echo "   사용자: ${SSH_USER}"
echo "   경로: ${REMOTE_PATH}"
echo ""

# 로컬 Git 상태 확인
echo "🔍 로컬 Git 상태 확인..."
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  커밋되지 않은 변경사항이 있습니다."
    git status --short
    echo ""
    read -p "계속하시겠습니까? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "배포를 취소합니다."
        exit 1
    fi
else
    echo "✅ 작업 디렉토리가 깨끗합니다."
fi
echo ""

# GitHub에 최신 코드 푸시
echo "📤 GitHub에 최신 코드 푸시..."
CURRENT_BRANCH=$(git branch --show-current)
git push origin "${CURRENT_BRANCH}"
echo "✅ GitHub 푸시 완료"
echo ""

# 배포 방법 선택
echo "배포 방법을 선택하세요:"
echo "1) rsync를 통한 직접 배포 (빠름)"
echo "2) SSH로 서버에서 git pull (안전)"
echo "3) 배포 취소"
echo ""
read -p "선택 (1/2/3): " DEPLOY_METHOD

case $DEPLOY_METHOD in
    1)
        echo ""
        echo "📦 rsync로 파일 전송 중..."
        
        # rsync로 파일 동기화 (node_modules, .git 제외)
        rsync -avz --progress \
            --exclude 'node_modules' \
            --exclude '.git' \
            --exclude '*.pyc' \
            --exclude '__pycache__' \
            --exclude '.env' \
            --exclude 'venv' \
            --exclude '.vscode' \
            -e "ssh -p ${SSH_PORT}" \
            ./ ${SSH_USER}@${SSH_HOST}:${REMOTE_PATH}/
        
        echo "✅ 파일 전송 완료"
        ;;
        
    2)
        echo ""
        echo "🔄 서버에서 git pull 실행 중..."
        
        ssh -p ${SSH_PORT} ${SSH_USER}@${SSH_HOST} << 'ENDSSH'
cd /home/hosting_users/minilms/www
git pull origin main
echo "✅ git pull 완료"
ENDSSH
        ;;
        
    3)
        echo "배포를 취소합니다."
        exit 0
        ;;
        
    *)
        echo "❌ 잘못된 선택입니다."
        exit 1
        ;;
esac

echo ""
echo "🔧 서버에서 설치 및 재시작 중..."

# SSH로 서버 명령어 실행
ssh -p ${SSH_PORT} ${SSH_USER}@${SSH_HOST} << 'ENDSSH'
cd /home/hosting_users/minilms/www

echo "📦 Python 패키지 설치..."
pip3 install -r backend/requirements.txt

echo "🔄 PM2로 서비스 재시작..."
pm2 restart all || pm2 start ecosystem.config.js

echo "✅ 서비스 재시작 완료"

echo ""
echo "📊 서비스 상태:"
pm2 list
ENDSSH

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 배포 완료!"
echo ""
echo "   서버: ${SSH_HOST}"
echo "   접속: ssh ${SSH_USER}@${SSH_HOST}"
echo "   로그 확인: ssh ${SSH_USER}@${SSH_HOST} 'pm2 logs'"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
