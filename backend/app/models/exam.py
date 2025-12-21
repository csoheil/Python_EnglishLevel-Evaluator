# backend/app/models/exam.py

from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    score = Column(Integer, default=0)
