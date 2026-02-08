"""
MySQL 테이블 생성 스크립트
청산에사르리랏다 - 데이터베이스 스키마 초기화
"""
from app.database import engine, Base, SQLALCHEMY_DATABASE_URL
from app.models import Participant, Project, Settlement, ProjectProgress
import sys

def create_tables():
    """데이터베이스 테이블 생성"""
    
    print("="*60)
    print("🔧 데이터베이스 테이블 생성")
    print("="*60)
    print(f"📍 연결: {SQLALCHEMY_DATABASE_URL.split('?')[0]}")  # 비밀번호 숨김
    print()
    
    try:
        print("⏳ 테이블 생성 중...")
        
        # 모든 테이블 생성
        Base.metadata.create_all(bind=engine)
        
        print("✅ 테이블 생성 완료!")
        print()
        
        # 생성된 테이블 목록
        print("📋 생성된 테이블:")
        tables = [
            ("participants", "참여자 정보"),
            ("projects", "프로젝트 정보 (10단계 날짜 + 진도 관리)"),
            ("project_participants", "프로젝트-참여자 연결 (개별 수익률)"),
            ("settlements", "정산 내역"),
            ("project_progress", "진도 로그 (히스토리)")
        ]
        
        for table_name, description in tables:
            print(f"  ✓ {table_name:25} - {description}")
        
        print()
        print("="*60)
        print("✨ 초기화 완료!")
        print("="*60)
        print()
        print("✅ 다음 단계:")
        print("  1. uvicorn main:app --host 0.0.0.0 --port 8001 --reload")
        print("  2. 브라우저: http://localhost:8001")
        print("  3. 참여자 추가 → 프로젝트 추가 → 정산 계산")
        print()
        
        return True
        
    except Exception as e:
        print(f"❌ 테이블 생성 실패: {e}")
        print()
        import traceback
        traceback.print_exc()
        
        print()
        print("💡 해결 방법:")
        print("  1. python test_mysql_connection.py  # 먼저 연결 테스트")
        print("  2. .env 파일 설정 확인")
        print("  3. MySQL 사용자 권한 확인 (CREATE TABLE 권한 필요)")
        print()
        
        return False

if __name__ == "__main__":
    success = create_tables()
    sys.exit(0 if success else 1)
