from sqlalchemy import Column, Integer, ForeignKey, String
from app.models.base import Base



class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    score = Column(Integer, nullable=True)
    cefr_level = Column(String(2), nullable=True)
