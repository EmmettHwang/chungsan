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
    
    # 프로젝트 단계별 날짜
    idea_date: Optional[datetime] = None
    introduction_date: Optional[datetime] = None
    consultation_date: Optional[datetime] = None
    quote_date: Optional[datetime] = None
    contract_date: Optional[datetime] = None
    development_date: Optional[datetime] = None
    test_date: Optional[datetime] = None
    delivery_date: Optional[datetime] = None
    completion_date: Optional[datetime] = None
    maintenance_date: Optional[datetime] = None
    
    # 기존 날짜
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    
    # 진도 관리
    progress_notes: Optional[str] = None
    progress_rate: Optional[float] = 0.0
    current_stage: Optional[str] = None
    
    notes: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    client: Optional[str] = None
    total_amount: Optional[float] = None
    cost: Optional[float] = None
    status: Optional[str] = None
    
    # 프로젝트 단계별 날짜
    idea_date: Optional[datetime] = None
    introduction_date: Optional[datetime] = None
    consultation_date: Optional[datetime] = None
    quote_date: Optional[datetime] = None
    contract_date: Optional[datetime] = None
    development_date: Optional[datetime] = None
    test_date: Optional[datetime] = None
    delivery_date: Optional[datetime] = None
    completion_date: Optional[datetime] = None
    maintenance_date: Optional[datetime] = None
    
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    
    # 진도 관리
    progress_notes: Optional[str] = None
    progress_rate: Optional[float] = None
    current_stage: Optional[str] = None
    
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

# ============================================================================
# 프로젝트 진도 (Project Progress) 스키마
# ============================================================================

class ProjectProgressBase(BaseModel):
    project_id: int
    stage: Optional[str] = None
    memo: str
    progress_rate: Optional[float] = 0.0
    author: Optional[str] = None

class ProjectProgressCreate(ProjectProgressBase):
    pass

class ProjectProgressUpdate(BaseModel):
    stage: Optional[str] = None
    memo: Optional[str] = None
    progress_rate: Optional[float] = None

class ProjectProgress(ProjectProgressBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# 진도 분석 요청/응답
class ProgressAnalyzeRequest(BaseModel):
    memo: str

class ProgressAnalyzeResponse(BaseModel):
    stage: str
    progress_rate: float
    summary: str
    keywords: List[str]
