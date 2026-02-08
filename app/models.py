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
    code = Column(String(50), unique=True, index=True, nullable=False)  # HUMAN-001, HUMAN-002...
    name = Column(String(100), nullable=False)
    role = Column(String(50), default="regular")  # admin, lead, senior, regular, assistant
    default_profit_rate = Column(Float, default=10.0)  # 기본 수익률 (%)
    
    # 연락처 정보
    phone = Column(String(50), nullable=True)
    email = Column(String(100), nullable=True)
    
    # 은행 정보
    bank_name = Column(String(100), nullable=True)
    account_number = Column(String(100), nullable=True)
    
    # 첨부 파일 경로
    id_card_path = Column(String(500), nullable=True)  # 신분증 사본
    bankbook_path = Column(String(500), nullable=True)  # 통장 사본
    
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
    name = Column(String(200), nullable=False, index=True)
    client = Column(String(200), nullable=True)  # 클라이언트/발주처
    
    # 금액 정보
    total_amount = Column(Float, default=0.0)  # 총 프로젝트 금액
    cost = Column(Float, default=0.0)  # 원가
    profit = Column(Float, default=0.0)  # 순이익 (total_amount - cost)
    
    # 프로젝트 상태
    status = Column(String(50), default="planned")  # planned, in_progress, completed, settled
    
    # 프로젝트 단계별 날짜 (스크린샷 기준)
    idea_date = Column(DateTime, nullable=True)  # 아이디어
    introduction_date = Column(DateTime, nullable=True)  # 소개
    consultation_date = Column(DateTime, nullable=True)  # 상담
    quote_date = Column(DateTime, nullable=True)  # 견적
    contract_date = Column(DateTime, nullable=True)  # 계약
    development_date = Column(DateTime, nullable=True)  # 개발
    test_date = Column(DateTime, nullable=True)  # 테스트
    delivery_date = Column(DateTime, nullable=True)  # 납품
    completion_date = Column(DateTime, nullable=True)  # 완료
    maintenance_date = Column(DateTime, nullable=True)  # 유지보수
    
    # 날짜 정보 (기존)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    
    # 메모
    notes = Column(Text, nullable=True)
    
    # 진도 관리
    progress_notes = Column(Text, nullable=True)  # 진도 메모
    progress_rate = Column(Float, default=0.0)  # 진도율 (0-100%)
    current_stage = Column(String(50), nullable=True)  # 현재 단계
    
    # 타임스탬프
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    participants = relationship("Participant", secondary=project_participants, back_populates="projects")
    settlements = relationship("Settlement", back_populates="project")
    progress_logs = relationship("ProjectProgress", back_populates="project", cascade="all, delete-orphan")

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
    status = Column(String(50), default="pending")  # pending, paid, cancelled
    paid_at = Column(DateTime, nullable=True)
    
    # 메모
    notes = Column(Text, nullable=True)
    
    # 타임스탬프
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    project = relationship("Project", back_populates="settlements")
    participant = relationship("Participant", back_populates="settlements")

class ProjectProgress(Base):
    """프로젝트 진도 로그 모델"""
    __tablename__ = "project_progress"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # 외래키
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    
    # 진도 정보
    stage = Column(String(50), nullable=True)  # 단계 (아이디어, 소개, 상담, 견적, 계약, 개발, 테스트, 납품, 완료, 유지보수)
    memo = Column(Text, nullable=False)  # 진도 메모
    progress_rate = Column(Float, default=0.0)  # 진도율 (0-100%)
    
    # 작성자 (향후 추가)
    author = Column(String(100), nullable=True)
    
    # 타임스탬프
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    project = relationship("Project", back_populates="progress_logs")
