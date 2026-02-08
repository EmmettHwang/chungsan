"""
청산에사르리랏다 - 프로젝트 원가 관리 API
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud_costs
from app.database import get_db

router = APIRouter(prefix="/api/costs", tags=["원가 관리"])

@router.get("/project/{project_id}", response_model=List[schemas.ProjectCost])
def get_project_costs(project_id: int, db: Session = Depends(get_db)):
    """프로젝트의 모든 원가 항목 조회"""
    costs = crud_costs.get_project_costs(db, project_id)
    return costs

@router.get("/{cost_id}", response_model=schemas.ProjectCost)
def get_cost(cost_id: int, db: Session = Depends(get_db)):
    """원가 항목 상세 조회"""
    cost = crud_costs.get_cost_by_id(db, cost_id)
    if not cost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="원가 항목을 찾을 수 없습니다"
        )
    return cost

@router.post("/", response_model=schemas.ProjectCost, status_code=status.HTTP_201_CREATED)
def create_cost(cost: schemas.ProjectCostCreate, db: Session = Depends(get_db)):
    """새 원가 항목 생성"""
    return crud_costs.create_project_cost(db, cost)

@router.put("/{cost_id}", response_model=schemas.ProjectCost)
def update_cost(
    cost_id: int,
    cost_update: schemas.ProjectCostUpdate,
    db: Session = Depends(get_db)
):
    """원가 항목 수정"""
    updated_cost = crud_costs.update_project_cost(db, cost_id, cost_update)
    if not updated_cost:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="원가 항목을 찾을 수 없습니다"
        )
    return updated_cost

@router.delete("/{cost_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cost(cost_id: int, db: Session = Depends(get_db)):
    """원가 항목 삭제"""
    success = crud_costs.delete_project_cost(db, cost_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="원가 항목을 찾을 수 없습니다"
        )
    return None

@router.get("/project/{project_id}/total")
def get_total_cost(project_id: int, db: Session = Depends(get_db)):
    """프로젝트의 총 원가 조회"""
    total = crud_costs.get_project_total_cost(db, project_id)
    return {"project_id": project_id, "total_cost": total}

@router.get("/project/{project_id}/category/{category}", response_model=List[schemas.ProjectCost])
def get_costs_by_category(
    project_id: int,
    category: str,
    db: Session = Depends(get_db)
):
    """카테고리별 원가 항목 조회"""
    costs = crud_costs.get_costs_by_category(db, project_id, category)
    return costs
