"""
청산에사르리랏다 - 프로젝트 원가 CRUD
"""
from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas

def get_project_costs(db: Session, project_id: int) -> List[models.ProjectCost]:
    """프로젝트의 모든 원가 항목 조회"""
    return db.query(models.ProjectCost).filter(
        models.ProjectCost.project_id == project_id
    ).all()

def get_cost_by_id(db: Session, cost_id: int) -> Optional[models.ProjectCost]:
    """원가 항목 ID로 조회"""
    return db.query(models.ProjectCost).filter(
        models.ProjectCost.id == cost_id
    ).first()

def create_project_cost(db: Session, cost: schemas.ProjectCostCreate) -> models.ProjectCost:
    """새 원가 항목 생성"""
    db_cost = models.ProjectCost(**cost.model_dump())
    db.add(db_cost)
    db.commit()
    db.refresh(db_cost)
    return db_cost

def update_project_cost(
    db: Session, 
    cost_id: int, 
    cost_update: schemas.ProjectCostUpdate
) -> Optional[models.ProjectCost]:
    """원가 항목 수정"""
    db_cost = get_cost_by_id(db, cost_id)
    if not db_cost:
        return None
    
    update_data = cost_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_cost, field, value)
    
    db.commit()
    db.refresh(db_cost)
    return db_cost

def delete_project_cost(db: Session, cost_id: int) -> bool:
    """원가 항목 삭제"""
    db_cost = get_cost_by_id(db, cost_id)
    if not db_cost:
        return False
    
    db.delete(db_cost)
    db.commit()
    return True

def get_project_total_cost(db: Session, project_id: int) -> float:
    """프로젝트의 총 원가 계산"""
    costs = get_project_costs(db, project_id)
    return sum(cost.amount for cost in costs)

def get_costs_by_category(db: Session, project_id: int, category: str) -> List[models.ProjectCost]:
    """카테고리별 원가 항목 조회"""
    return db.query(models.ProjectCost).filter(
        models.ProjectCost.project_id == project_id,
        models.ProjectCost.category == category
    ).all()
