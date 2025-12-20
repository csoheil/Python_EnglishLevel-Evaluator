# backend/app/api/v1/exams.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.exam import Exam
from app.services.question_sampler import sample_questions
from app.schemas.exam import ExamStartResponse

router = APIRouter(prefix="/exams", tags=["Exams"])


@router.post("/start", response_model=ExamStartResponse)
def start_exam(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    exam = Exam(user_id=user.id)
    db.add(exam)
    db.commit()
    db.refresh(exam)

    questions = sample_questions(db)

    return {
        "exam_id": exam.id,
        "questions": questions
    }
