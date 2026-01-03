from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.exam import Exam
from app.services.question_sampler import get_random_questions

router = APIRouter(
    prefix="/exams",
    tags=["Exams"],
)


@router.post("/start", status_code=status.HTTP_201_CREATED)
def start_exam(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Start a new exam and return random questions.
    """
    exam = Exam(user_id=current_user.id)
    db.add(exam)
    db.commit()
    db.refresh(exam)

    questions = get_random_questions(db, limit=20)

    return {
        "exam_id": exam.id,
        "questions": [
            {
                "id": q.id,
                "text": q.text,
                "options": {
                    "A": q.option_a,
                    "B": q.option_b,
                    "C": q.option_c,
                    "D": q.option_d,
                },
            }
            for q in questions
        ],
    }
