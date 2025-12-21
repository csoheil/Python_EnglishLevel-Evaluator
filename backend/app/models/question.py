# backend/app/models/question.py

from sqlalchemy import Column, Integer, String, Index
from app.db.base import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)

    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)

    correct_option = Column(String(1), nullable=False)  # A, B, C, D
    level = Column(String(2), nullable=False)  # A1, A2, B1, B2, C1, C2

Index("idx_questions_id", Question.id)
