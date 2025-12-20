# backend/app/models/question.py

from sqlalchemy import Column, Integer, Text, String
from app.models.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

    option_a = Column(Text, nullable=False)
    option_b = Column(Text, nullable=False)
    option_c = Column(Text, nullable=False)
    option_d = Column(Text, nullable=False)

    correct_option = Column(String(1), nullable=False)
    difficulty_level = Column(String(2), index=True)
    random_bucket = Column(Integer, index=True)
