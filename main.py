"""
청산에사르리랏다 - 메인 FastAPI 애플리케이션
소프트웨어 및 하드웨어 개발 납품 프로젝트의 정산 관리 시스템
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.database import engine, Base
from app.routers import participants, projects, settlements, progress

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# FastAPI 앱 생성
app = FastAPI(
    title="청산에사르리랏다",
    description="소프트웨어 및 하드웨어 개발 납품 프로젝트의 정산 관리 시스템",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(participants.router)
app.include_router(projects.router)
app.include_router(settlements.router)
app.include_router(progress.router)

# 정적 파일 서빙
if os.path.exists("static"):
    app.mount("/css", StaticFiles(directory="static/css"), name="css")
    app.mount("/js", StaticFiles(directory="static/js"), name="js")
    app.mount("/images", StaticFiles(directory="static/images"), name="images")

# uploads 디렉토리 서빙
if os.path.exists("uploads"):
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def read_root():
    """프론트엔드 홈페이지"""
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    else:
        return {
            "message": "청산에사르리랏다 (Chungsan Settlement System)",
            "description": "소프트웨어 및 하드웨어 개발 납품 프로젝트의 정산 관리 시스템",
            "version": "1.0.0",
            "docs": "/docs",
            "redoc": "/redoc",
            "frontend": "/static/index.html"
        }

@app.get("/api")
def api_root():
    """API 정보"""
    return {
        "message": "청산에사르리랏다 API",
        "version": "1.0.0",
        "endpoints": {
            "participants": "/api/participants/",
            "projects": "/api/projects/",
            "settlements": "/api/settlements/"
        }
    }

@app.get("/health")
def health_check():
    """헬스 체크"""
    return {
        "status": "healthy",
        "service": "청산에사르리랏다"
    }

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("🎉 청산에사르리랏다 (Chungsan Settlement System)")
    print("="*60)
    print("\n📍 접속 URL:")
    print("   - 메인 (프론트엔드): http://localhost:8001")
    print("   - API 문서 (Swagger): http://localhost:8001/docs")
    print("   - API 문서 (ReDoc): http://localhost:8001/redoc")
    print("\n⌨️  종료: Ctrl+C")
    print("="*60 + "\n")
    
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)

