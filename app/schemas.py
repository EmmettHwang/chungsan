"""
청산에사르리랏다 - Pydantic 스키마
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# ============================================================================
# 참여자 (Participant) 스키마
# ============================================================================

class ParticipantBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    role: Optional[str] = "regular"
    default_profit_rate: Optional[float] = 10.0
    phone: Optional[str] = None
    email: Optional[str] = None
    bank_name: Optional[str] = None
    account_number: Optional[str] = None
    notes: Optional[str] = None

class ParticipantCreate(ParticipantBase):
    pass

class ParticipantUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    default_profit_rate: Optional[float] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    bank_name: Optional[str] = None
    account_number: Optional[str] = None
    notes: Optional[str] = None

class Participant(ParticipantBase):
    id: int
    code: str
    id_card_path: Optional[str] = None
    bankbook_path: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ============================================================================
# 프로젝트 (Project) 스키마
# ============================================================================

class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    client: Optional[str] = None
    total_amount: Optional[float] = 0.0
    cost: Optional[float] = 0.0
    status: Optional[str] = "planned"
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    client: Optional[str] = None
    total_amount: Optional[float] = None
    cost: Optional[float] = None
    status: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    notes: Optional[str] = None

class Project(ProjectBase):
    id: int
    profit: float
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ============================================================================
# 프로젝트 참여자 (Project Participant) 스키마
# ============================================================================

class ProjectParticipantAdd(BaseModel):
    participant_id: int
    profit_rate: Optional[float] = None  # None이면 participant의 default_profit_rate 사용

class ProjectParticipantUpdate(BaseModel):
    profit_rate: float

class ProjectParticipantResponse(BaseModel):
    participant_id: int
    participant_name: str
    participant_code: str
    participant_role: str
    profit_rate: float
    joined_at: datetime
    
    class Config:
        from_attributes = True

# ============================================================================
# 정산 (Settlement) 스키마
# ============================================================================

class SettlementBase(BaseModel):
    project_id: int
    participant_id: int
    profit_rate: float
    amount: float
    status: Optional[str] = "pending"
    notes: Optional[str] = None

class SettlementCreate(SettlementBase):
    pass

class SettlementUpdate(BaseModel):
    status: Optional[str] = None
    paid_at: Optional[datetime] = None
    notes: Optional[str] = None

class Settlement(SettlementBase):
    id: int
    paid_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ============================================================================
# 정산 계산 요청/응답 스키마
# ============================================================================

class SettlementCalculateRequest(BaseModel):
    project_id: int

class SettlementCalculateResponse(BaseModel):
    project_id: int
    project_name: str
    total_profit: float
    settlements: List[dict]  # [{participant_id, participant_name, profit_rate, amount}, ...]
    
    class Config:
        from_attributes = True
