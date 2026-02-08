"""
청산에사르리랏다 - 프로젝트 진도 관리 API
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from datetime import datetime
import re

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/api/progress", tags=["progress"])

# ============================================================================
# 진도 로그 CRUD
# ============================================================================

@router.post("/", response_model=schemas.ProjectProgress)
def create_progress_log(
    progress: schemas.ProjectProgressCreate,
    db: Session = Depends(get_db)
):
    """진도 로그 생성"""
    # 프로젝트 존재 확인
    project = db.query(models.Project).filter(models.Project.id == progress.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # 진도 분석
    analyzed = analyze_progress_memo(progress.memo)
    
    # 진도 로그 생성
    db_progress = models.ProjectProgress(
        project_id=progress.project_id,
        stage=progress.stage or analyzed["stage"],
        memo=progress.memo,
        progress_rate=progress.progress_rate or analyzed["progress_rate"],
        author=progress.author
    )
    
    db.add(db_progress)
    
    # 프로젝트 진도 업데이트
    project.progress_rate = db_progress.progress_rate
    project.current_stage = db_progress.stage
    project.progress_notes = progress.memo
    
    db.commit()
    db.refresh(db_progress)
    
    return db_progress

@router.get("/{project_id}", response_model=List[schemas.ProjectProgress])
def get_progress_logs(
    project_id: int,
    db: Session = Depends(get_db)
):
    """특정 프로젝트의 진도 로그 조회"""
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    logs = db.query(models.ProjectProgress)\
        .filter(models.ProjectProgress.project_id == project_id)\
        .order_by(models.ProjectProgress.created_at.desc())\
        .all()
    
    return logs

@router.delete("/{progress_id}")
def delete_progress_log(
    progress_id: int,
    db: Session = Depends(get_db)
):
    """진도 로그 삭제"""
    progress = db.query(models.ProjectProgress)\
        .filter(models.ProjectProgress.id == progress_id)\
        .first()
    
    if not progress:
        raise HTTPException(status_code=404, detail="진도 로그를 찾을 수 없습니다")
    
    db.delete(progress)
    db.commit()
    
    return {"message": "진도 로그가 삭제되었습니다"}

# ============================================================================
# 진도 분석
# ============================================================================

@router.post("/analyze", response_model=schemas.ProgressAnalyzeResponse)
def analyze_progress(
    request: schemas.ProgressAnalyzeRequest
):
    """진도 메모 분석"""
    result = analyze_progress_memo(request.memo)
    
    return schemas.ProgressAnalyzeResponse(
        stage=result["stage"],
        progress_rate=result["progress_rate"],
        summary=result["summary"],
        keywords=result["keywords"]
    )

def analyze_progress_memo(memo: str) -> dict:
    """
    진도 메모를 분석하여 단계와 진도율을 추출
    
    단계 키워드:
    - 아이디어: 아이디어, 기획, 제안
    - 소개: 소개, 미팅, 발표
    - 상담: 상담, 협의, 논의
    - 견적: 견적, 산정, 비용
    - 계약: 계약, 서명, 체결
    - 개발: 개발, 구현, 코딩
    - 테스트: 테스트, 검증, QA
    - 납품: 납품, 배포, 출시
    - 완료: 완료, 종료, 마감
    - 유지보수: 유지보수, 지원, 패치
    """
    memo_lower = memo.lower()
    
    # 단계 키워드 매핑
    stage_keywords = {
        "아이디어": ["아이디어", "기획", "제안", "구상"],
        "소개": ["소개", "미팅", "발표", "프리젠테이션"],
        "상담": ["상담", "협의", "논의", "검토"],
        "견적": ["견적", "산정", "비용", "예산"],
        "계약": ["계약", "서명", "체결", "합의"],
        "개발": ["개발", "구현", "코딩", "프로그래밍", "작업"],
        "테스트": ["테스트", "검증", "qa", "버그"],
        "납품": ["납품", "배포", "출시", "릴리즈"],
        "완료": ["완료", "종료", "마감", "끝"],
        "유지보수": ["유지보수", "지원", "패치", "수정"]
    }
    
    # 단계 판단
    detected_stage = "개발"  # 기본값
    for stage, keywords in stage_keywords.items():
        if any(keyword in memo for keyword in keywords):
            detected_stage = stage
            break
    
    # 진도율 추출 (숫자 + %)
    progress_match = re.search(r'(\d+)\s*%', memo)
    if progress_match:
        progress_rate = float(progress_match.group(1))
    else:
        # 단계별 기본 진도율
        stage_progress = {
            "아이디어": 5,
            "소개": 10,
            "상담": 20,
            "견적": 30,
            "계약": 40,
            "개발": 60,
            "테스트": 80,
            "납품": 90,
            "완료": 100,
            "유지보수": 100
        }
        progress_rate = stage_progress.get(detected_stage, 50)
    
    # 키워드 추출 (빈도수 높은 명사)
    keywords = []
    for stage, words in stage_keywords.items():
        for word in words:
            if word in memo:
                keywords.append(word)
    
    # 중복 제거
    keywords = list(set(keywords))[:5]
    
    # 요약 생성
    summary = f"{detected_stage} 단계 진행 중 (진도율: {progress_rate}%)"
    
    return {
        "stage": detected_stage,
        "progress_rate": progress_rate,
        "summary": summary,
        "keywords": keywords
    }

# ============================================================================
# 프로젝트 진도 현황
# ============================================================================

@router.get("/project/{project_id}/summary")
def get_project_progress_summary(
    project_id: int,
    db: Session = Depends(get_db)
):
    """프로젝트 진도 현황 요약"""
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # 최근 진도 로그
    recent_logs = db.query(models.ProjectProgress)\
        .filter(models.ProjectProgress.project_id == project_id)\
        .order_by(models.ProjectProgress.created_at.desc())\
        .limit(5)\
        .all()
    
    # 단계별 완료 여부
    stages_status = {
        "아이디어": bool(project.idea_date),
        "소개": bool(project.introduction_date),
        "상담": bool(project.consultation_date),
        "견적": bool(project.quote_date),
        "계약": bool(project.contract_date),
        "개발": bool(project.development_date),
        "테스트": bool(project.test_date),
        "납품": bool(project.delivery_date),
        "완료": bool(project.completion_date),
        "유지보수": bool(project.maintenance_date)
    }
    
    return {
        "project_id": project.id,
        "project_name": project.name,
        "current_stage": project.current_stage or "아이디어",
        "progress_rate": project.progress_rate or 0.0,
        "stages_status": stages_status,
        "recent_logs": [
            {
                "id": log.id,
                "stage": log.stage,
                "memo": log.memo,
                "progress_rate": log.progress_rate,
                "created_at": log.created_at
            }
            for log in recent_logs
        ]
    }
