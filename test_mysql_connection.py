"""
MySQL 연결 테스트 스크립트
청산에사르리랏다 - Cafe24 MySQL 서버 연결 확인
"""
import os
from dotenv import load_dotenv
import pymysql
import sys

def test_mysql_connection():
    """MySQL 연결 테스트"""
    
    # .env 파일 로드
    load_dotenv()
    
    # 연결 정보
    host = os.getenv("DB_HOST")
    port = int(os.getenv("DB_PORT", 3306))
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    
    print("="*60)
    print("🔍 MySQL 데이터베이스 연결 테스트")
    print("="*60)
    print(f"호스트: {host}:{port}")
    print(f"사용자: {user}")
    print(f"데이터베이스: {database}")
    print()
    
    try:
        # MySQL 연결 시도
        print("⏳ 연결 중...")
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            connect_timeout=10
        )
        
        print("✅ 데이터베이스 연결 성공!")
        print()
        
        # 커서 생성
        cursor = conn.cursor()
        
        # MySQL 버전 확인
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()[0]
        print(f"📊 MySQL 버전: {version}")
        
        # 현재 데이터베이스 확인
        cursor.execute("SELECT DATABASE();")
        current_db = cursor.fetchone()[0]
        print(f"🗄️  현재 DB: {current_db}")
        
        # 문자 인코딩 확인
        cursor.execute("SHOW VARIABLES LIKE 'character_set%';")
        print(f"\n📝 문자 인코딩 설정:")
        for var, value in cursor.fetchall():
            print(f"  {var:30} = {value}")
        
        # 기존 테이블 확인
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print(f"\n📋 기존 테이블 목록 ({len(tables)}개):")
        if tables:
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
                count = cursor.fetchone()[0]
                print(f"  - {table[0]:30} ({count:,}개 레코드)")
        else:
            print("  (테이블 없음)")
        
        # 연결 상태 확인
        cursor.execute("SHOW STATUS LIKE 'Threads_connected';")
        threads = cursor.fetchone()
        print(f"\n🔗 현재 연결 수: {threads[1]}")
        
        # 데이터베이스 크기 확인
        cursor.execute("""
            SELECT 
                table_schema AS 'Database',
                ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)'
            FROM information_schema.tables
            WHERE table_schema = %s
            GROUP BY table_schema;
        """, (database,))
        
        db_size = cursor.fetchone()
        if db_size:
            print(f"💾 데이터베이스 크기: {db_size[1]} MB")
        
        # 정리
        cursor.close()
        conn.close()
        
        print("\n" + "="*60)
        print("✨ 연결 테스트 완료!")
        print("="*60)
        print()
        print("✅ 다음 단계:")
        print("  1. python create_tables.py  # 테이블 생성")
        print("  2. uvicorn main:app --reload  # 서버 실행")
        print()
        
        return True
        
    except pymysql.err.OperationalError as e:
        print(f"❌ 연결 실패 (OperationalError): {e}")
        print()
        print("💡 해결 방법:")
        print("  1. .env 파일이 프로젝트 루트에 있는지 확인")
        print("  2. DB_HOST, DB_USER, DB_PASSWORD가 정확한지 확인")
        print("  3. Cafe24 MySQL 원격 접속 허용 확인")
        print("  4. 방화벽에서 3306 포트 허용 확인")
        return False
        
    except pymysql.err.ProgrammingError as e:
        print(f"❌ 프로그래밍 오류: {e}")
        print()
        print("💡 해결 방법:")
        print("  1. DATABASE 이름 확인 (DB_NAME)")
        print("  2. Cafe24에서 chungsan 데이터베이스 생성")
        return False
        
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_mysql_connection()
    sys.exit(0 if success else 1)
