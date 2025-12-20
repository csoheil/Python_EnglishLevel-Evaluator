# backend/app/models/exam.py

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func

from app.models.base import Base


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    score = Column(Integer)
    cefr_level = Column(String(2))

    started_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True))
