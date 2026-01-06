from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func

from app.models.base import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)

    score = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    cefr_level = Column(String(2), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
