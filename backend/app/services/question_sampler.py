# backend/app/services/question_sampler.py

import random
from sqlalchemy.orm import Session
from app.models.question import Question


def sample_questions(db: Session, limit: int = 20):
    bucket = random.randint(1, 1000)

    questions = (
        db.query(Question)
        .filter(Question.random_bucket == bucket)
        .limit(limit)
        .all()
    )

    # fallback if bucket is small
    if len(questions) < limit:
        questions = (
            db.query(Question)
            .order_by(Question.id)
            .limit(limit)
            .all()
        )

    return questions
