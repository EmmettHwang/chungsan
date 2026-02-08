"""
청산에사르리랏다 - 프로젝트 관리 API
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_, text
from typing import List
from datetime import datetime

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/api/projects", tags=["projects"])

@router.get("/", response_model=List[schemas.Project])
def get_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """모든 프로젝트 조회"""
    projects = db.query(models.Project).offset(skip).limit(limit).all()
    
    # profit 계산
    for project in projects:
        project.profit = project.total_amount - project.cost
    
    return projects

@router.get("/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    """특정 프로젝트 조회"""
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # profit 계산
    project.profit = project.total_amount - project.cost
    
    return project

@router.post("/", response_model=schemas.Project, status_code=201)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    """새 프로젝트 생성"""
    db_project = models.Project(**project.model_dump())
    db_project.profit = db_project.total_amount - db_project.cost
    
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    
    return db_project

@router.put("/{project_id}", response_model=schemas.Project)
def update_project(
    project_id: int,
    project_update: schemas.ProjectUpdate,
    db: Session = Depends(get_db)
):
    """프로젝트 정보 수정"""
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # 업데이트
    update_data = project_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_project, key, value)
    
    # profit 재계산
    db_project.profit = db_project.total_amount - db_project.cost
    db_project.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_project)
    
    return db_project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    """프로젝트 삭제"""
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    db.delete(db_project)
    db.commit()
    
    return {"message": "프로젝트가 삭제되었습니다"}

# ============================================================================
# 프로젝트 참여자 관리
# ============================================================================

@router.get("/{project_id}/participants", response_model=List[schemas.ProjectParticipantResponse])
def get_project_participants(project_id: int, db: Session = Depends(get_db)):
    """프로젝트의 참여자 목록 조회"""
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # project_participants 테이블에서 조회
    result = db.execute(
        text("""
        SELECT 
            p.id as participant_id,
            p.name as participant_name,
            p.code as participant_code,
            p.role as participant_role,
            pp.profit_rate,
            pp.joined_at
        FROM participants p
        JOIN project_participants pp ON p.id = pp.participant_id
        WHERE pp.project_id = :project_id
        """),
        {"project_id": project_id}
    ).fetchall()
    
    return [
        schemas.ProjectParticipantResponse(
            participant_id=row[0],
            participant_name=row[1],
            participant_code=row[2],
            participant_role=row[3],
            profit_rate=row[4],
            joined_at=row[5]
        )
        for row in result
    ]

@router.post("/{project_id}/participants")
def add_project_participant(
    project_id: int,
    participant_add: schemas.ProjectParticipantAdd,
    db: Session = Depends(get_db)
):
    """프로젝트에 참여자 추가"""
    # 프로젝트 확인
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # 참여자 확인
    participant = db.query(models.Participant).filter(
        models.Participant.id == participant_add.participant_id
    ).first()
    if not participant:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    # 이미 참여 중인지 확인
    existing = db.execute(
        text("""
        SELECT * FROM project_participants 
        WHERE project_id = :project_id AND participant_id = :participant_id
        """),
        {"project_id": project_id, "participant_id": participant_add.participant_id}
    ).fetchone()
    
    if existing:
        raise HTTPException(status_code=400, detail="이미 참여 중인 참여자입니다")
    
    # profit_rate 설정 (없으면 participant의 default_profit_rate 사용)
    profit_rate = participant_add.profit_rate if participant_add.profit_rate is not None else participant.default_profit_rate
    
    # 참여자 추가
    db.execute(
        text("""
        INSERT INTO project_participants (project_id, participant_id, profit_rate, joined_at)
        VALUES (:project_id, :participant_id, :profit_rate, :joined_at)
        """),
        {
            "project_id": project_id,
            "participant_id": participant_add.participant_id,
            "profit_rate": profit_rate,
            "joined_at": datetime.utcnow()
        }
    )
    db.commit()
    
    return {"message": "참여자가 추가되었습니다", "profit_rate": profit_rate}

@router.put("/{project_id}/participants/{participant_id}")
def update_project_participant(
    project_id: int,
    participant_id: int,
    participant_update: schemas.ProjectParticipantUpdate,
    db: Session = Depends(get_db)
):
    """프로젝트 참여자의 수익률 수정"""
    # 존재 확인
    existing = db.execute(
        text("""
        SELECT * FROM project_participants 
        WHERE project_id = :project_id AND participant_id = :participant_id
        """),
        {"project_id": project_id, "participant_id": participant_id}
    ).fetchone()
    
    if not existing:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    # 수익률 업데이트
    db.execute(
        text("""
        UPDATE project_participants 
        SET profit_rate = :profit_rate
        WHERE project_id = :project_id AND participant_id = :participant_id
        """),
        {
            "profit_rate": participant_update.profit_rate,
            "project_id": project_id,
            "participant_id": participant_id
        }
    )
    db.commit()
    
    return {"message": "수익률이 업데이트되었습니다", "profit_rate": participant_update.profit_rate}

@router.delete("/{project_id}/participants/{participant_id}")
def remove_project_participant(project_id: int, participant_id: int, db: Session = Depends(get_db)):
    """프로젝트에서 참여자 제거"""
    # 존재 확인
    existing = db.execute(
        text("""
        SELECT * FROM project_participants 
        WHERE project_id = :project_id AND participant_id = :participant_id
        """),
        {"project_id": project_id, "participant_id": participant_id}
    ).fetchone()
    
    if not existing:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    # 참여자 제거
    db.execute(
        text("""
        DELETE FROM project_participants 
        WHERE project_id = :project_id AND participant_id = :participant_id
        """),
        {"project_id": project_id, "participant_id": participant_id}
    )
    db.commit()
    
    return {"message": "참여자가 제거되었습니다"}
