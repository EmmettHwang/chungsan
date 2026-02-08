"""
청산에사르리랏다 - 참여자 관리 API
"""
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
from datetime import datetime

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/api/participants", tags=["participants"])

# 업로드 디렉토리
UPLOAD_DIR = "uploads/participants"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def generate_participant_code(db: Session) -> str:
    """참여자 코드 자동 생성 (HUMAN-001, HUMAN-002...)"""
    last_participant = db.query(models.Participant).order_by(models.Participant.id.desc()).first()
    if last_participant and last_participant.code.startswith("HUMAN-"):
        try:
            last_number = int(last_participant.code.split("-")[1])
            new_number = last_number + 1
        except:
            new_number = 1
    else:
        new_number = 1
    
    return f"HUMAN-{new_number:03d}"

@router.get("/", response_model=List[schemas.Participant])
def get_participants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """모든 참여자 조회"""
    participants = db.query(models.Participant).offset(skip).limit(limit).all()
    return participants

@router.get("/{participant_id}", response_model=schemas.Participant)
def get_participant(participant_id: int, db: Session = Depends(get_db)):
    """특정 참여자 조회"""
    participant = db.query(models.Participant).filter(models.Participant.id == participant_id).first()
    if not participant:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    return participant

@router.post("/", response_model=schemas.Participant, status_code=201)
def create_participant(participant: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    """새 참여자 생성"""
    # 코드 자동 생성
    code = generate_participant_code(db)
    
    # 참여자 생성
    db_participant = models.Participant(
        code=code,
        **participant.model_dump()
    )
    
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    
    return db_participant

@router.put("/{participant_id}", response_model=schemas.Participant)
def update_participant(
    participant_id: int,
    participant_update: schemas.ParticipantUpdate,
    db: Session = Depends(get_db)
):
    """참여자 정보 수정"""
    db_participant = db.query(models.Participant).filter(models.Participant.id == participant_id).first()
    if not db_participant:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    # 업데이트
    update_data = participant_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_participant, key, value)
    
    db_participant.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_participant)
    
    return db_participant

@router.delete("/{participant_id}")
def delete_participant(participant_id: int, db: Session = Depends(get_db)):
    """참여자 삭제"""
    db_participant = db.query(models.Participant).filter(models.Participant.id == participant_id).first()
    if not db_participant:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    db.delete(db_participant)
    db.commit()
    
    return {"message": "참여자가 삭제되었습니다"}

@router.post("/{participant_id}/upload/id-card")
async def upload_id_card(participant_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """신분증 사본 업로드"""
    db_participant = db.query(models.Participant).filter(models.Participant.id == participant_id).first()
    if not db_participant:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    # 파일 저장
    file_extension = os.path.splitext(file.filename)[1]
    filename = f"{db_participant.code}_id_card{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # DB 업데이트
    db_participant.id_card_path = file_path
    db.commit()
    
    return {"filename": filename, "path": file_path}

@router.post("/{participant_id}/upload/bankbook")
async def upload_bankbook(participant_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """통장 사본 업로드"""
    db_participant = db.query(models.Participant).filter(models.Participant.id == participant_id).first()
    if not db_participant:
        raise HTTPException(status_code=404, detail="참여자를 찾을 수 없습니다")
    
    # 파일 저장
    file_extension = os.path.splitext(file.filename)[1]
    filename = f"{db_participant.code}_bankbook{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # DB 업데이트
    db_participant.bankbook_path = file_path
    db.commit()
    
    return {"filename": filename, "path": file_path}
