"""
청산에사르리랏다 - 데이터베이스 모델
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# 프로젝트-참여자 중간 테이블 (다대다 관계)
project_participants = Table(
    'project_participants',
    Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('participant_id', Integer, ForeignKey('participants.id'), primary_key=True),
    Column('profit_rate', Float, default=0.0),  # 해당 프로젝트에서의 수익률
    Column('joined_at', DateTime, default=datetime.utcnow)
)

class Participant(Base):
    """참여자 모델"""
    __tablename__ = "participants"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)  # HUMAN-001, HUMAN-002...
    name = Column(String, nullable=False)
    role = Column(String, default="regular")  # admin, lead, senior, regular, assistant
    default_profit_rate = Column(Float, default=10.0)  # 기본 수익률 (%)
    
    # 연락처 정보
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    
    # 은행 정보
    bank_name = Column(String, nullable=True)
    account_number = Column(String, nullable=True)
    
    # 첨부 파일 경로
    id_card_path = Column(String, nullable=True)  # 신분증 사본
    bankbook_path = Column(String, nullable=True)  # 통장 사본
    
    # 메모
    notes = Column(Text, nullable=True)
    
    # 타임스탬프
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    projects = relationship("Project", secondary=project_participants, back_populates="participants")
    settlements = relationship("Settlement", back_populates="participant")

class Project(Base):
    """프로젝트 모델"""
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    client = Column(String, nullable=True)  # 클라이언트/발주처
    
    # 금액 정보
    total_amount = Column(Float, default=0.0)  # 총 프로젝트 금액
    cost = Column(Float, default=0.0)  # 원가
    profit = Column(Float, default=0.0)  # 순이익 (total_amount - cost)
    
    # 프로젝트 상태
    status = Column(String, default="planned")  # planned, in_progress, completed, settled
    
    # 날짜 정보
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    
    # 메모
    notes = Column(Text, nullable=True)
    
    # 타임스탬프
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    participants = relationship("Participant", secondary=project_participants, back_populates="projects")
    settlements = relationship("Settlement", back_populates="project")

class Settlement(Base):
    """정산 모델"""
    __tablename__ = "settlements"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # 외래키
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    participant_id = Column(Integer, ForeignKey('participants.id'), nullable=False)
    
    # 정산 정보
    profit_rate = Column(Float, default=0.0)  # 수익률 (%)
    amount = Column(Float, default=0.0)  # 정산 금액
    
    # 지급 정보
    status = Column(String, default="pending")  # pending, paid, cancelled
    paid_at = Column(DateTime, nullable=True)
    
    # 메모
    notes = Column(Text, nullable=True)
    
    # 타임스탬프
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    project = relationship("Project", back_populates="settlements")
    participant = relationship("Participant", back_populates="settlements")
