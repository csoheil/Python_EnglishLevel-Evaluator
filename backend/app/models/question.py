from sqlalchemy import Column, Integer, String, Index
from app.models.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)

    text = Column(String, nullable=False)

    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)

    correct_option = Column(String(1), nullable=False)

    # Optional difficulty for future scaling (A1–C2)
    difficulty = Column(String(2), nullable=True)


# Performance indexes (VERY IMPORTANT for large datasets)
Index("ix_questions_id", Question.id)
Index("ix_questions_difficulty", Question.difficulty)
