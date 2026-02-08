"""
청산에사르리랏다 - 정산 관리 API
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from datetime import datetime

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/api/settlements", tags=["settlements"])

@router.post("/calculate", response_model=schemas.SettlementCalculateResponse)
def calculate_settlement(request: schemas.SettlementCalculateRequest, db: Session = Depends(get_db)):
    """프로젝트 정산 계산"""
    # 프로젝트 조회
    project = db.query(models.Project).filter(models.Project.id == request.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # 순이익 계산
    total_profit = project.total_amount - project.cost
    
    # 프로젝트 참여자 조회
    participants = db.execute(
        text("""
        SELECT 
            p.id,
            p.name,
            p.code,
            pp.profit_rate
        FROM participants p
        JOIN project_participants pp ON p.id = pp.participant_id
        WHERE pp.project_id = :project_id
        """),
        {"project_id": request.project_id}
    ).fetchall()
    
    if not participants:
        raise HTTPException(status_code=400, detail="프로젝트에 참여자가 없습니다")
    
    # 각 참여자의 정산 금액 계산
    settlements = []
    total_rate = sum([row[3] for row in participants])
    
    for row in participants:
        participant_id, participant_name, participant_code, profit_rate = row
        
        # 정산 금액 = 순이익 * (참여자 수익률 / 전체 수익률)
        if total_rate > 0:
            amount = total_profit * (profit_rate / total_rate)
        else:
            amount = 0.0
        
        settlements.append({
            "participant_id": participant_id,
            "participant_name": participant_name,
            "participant_code": participant_code,
            "profit_rate": profit_rate,
            "amount": round(amount, 2)
        })
    
    return schemas.SettlementCalculateResponse(
        project_id=project.id,
        project_name=project.name,
        total_profit=round(total_profit, 2),
        settlements=settlements
    )

@router.post("/", response_model=schemas.Settlement, status_code=201)
def create_settlement(settlement: schemas.SettlementCreate, db: Session = Depends(get_db)):
    """정산 기록 생성"""
    # 프로젝트 확인
    project = db.query(models.Project).filter(models.Project.id == settlement.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="프로젝트를 찾을 수 없습니다")
    
    # 참여자 확인
    participant = db.query(models.Participant).filter(models.Participant.id == settlement.participant_id).first()
    if not participant:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    # 정산 기록 생성
    db_settlement = models.Settlement(**settlement.model_dump())
    
    db.add(db_settlement)
    db.commit()
    db.refresh(db_settlement)
    
    return db_settlement

@router.get("/", response_model=List[schemas.Settlement])
def get_settlements(
    project_id: int = None,
    participant_id: int = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """정산 기록 조회"""
    query = db.query(models.Settlement)
    
    if project_id:
        query = query.filter(models.Settlement.project_id == project_id)
    
    if participant_id:
        query = query.filter(models.Settlement.participant_id == participant_id)
    
    settlements = query.offset(skip).limit(limit).all()
    return settlements

@router.get("/{settlement_id}", response_model=schemas.Settlement)
def get_settlement(settlement_id: int, db: Session = Depends(get_db)):
    """특정 정산 기록 조회"""
    settlement = db.query(models.Settlement).filter(models.Settlement.id == settlement_id).first()
    if not settlement:
        raise HTTPException(status_code=404, detail="정산 기록을 찾을 수 없습니다")
    return settlement

@router.put("/{settlement_id}", response_model=schemas.Settlement)
def update_settlement(
    settlement_id: int,
    settlement_update: schemas.SettlementUpdate,
    db: Session = Depends(get_db)
):
    """정산 기록 수정 (상태 업데이트)"""
    db_settlement = db.query(models.Settlement).filter(models.Settlement.id == settlement_id).first()
    if not db_settlement:
        raise HTTPException(status_code=404, detail="정산 기록을 찾을 수 없습니다")
    
    # 업데이트
    update_data = settlement_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_settlement, key, value)
    
    db_settlement.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_settlement)
    
    return db_settlement

@router.delete("/{settlement_id}")
def delete_settlement(settlement_id: int, db: Session = Depends(get_db)):
    """정산 기록 삭제"""
    db_settlement = db.query(models.Settlement).filter(models.Settlement.id == settlement_id).first()
    if not db_settlement:
        raise HTTPException(status_code=404, detail="정산 기록을 찾을 수 없습니다")
    
    db.delete(db_settlement)
    db.commit()
    
    return {"message": "정산 기록이 삭제되었습니다"}

@router.post("/{settlement_id}/mark-paid")
def mark_settlement_paid(settlement_id: int, db: Session = Depends(get_db)):
    """정산을 지급 완료로 표시"""
    db_settlement = db.query(models.Settlement).filter(models.Settlement.id == settlement_id).first()
    if not db_settlement:
        raise HTTPException(status_code=404, detail="정산 기록을 찾을 수 없습니다")
    
    db_settlement.status = "paid"
    db_settlement.paid_at = datetime.utcnow()
    db.commit()
    
    return {"message": "정산이 지급 완료로 표시되었습니다"}
