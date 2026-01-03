import random
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models.question import Question


def get_random_questions(db: Session, limit: int = 20):
    """
    Efficient random sampling using database-level random ordering.
    """
    return (
        db.query(Question)
        .order_by(func.random())
        .limit(limit)
        .all()
    )
