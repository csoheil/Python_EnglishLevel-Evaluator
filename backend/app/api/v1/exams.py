# backend/app/api/v1/exams.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.sampling import get_random_questions
from app.schemas.exam import ExamStartResponse
from app.schemas.question import QuestionOut

router = APIRouter(prefix="/exams", tags=["Exams"])

@router.post("/start", response_model=ExamStartResponse)
def start_exam(db: Session = Depends(get_db)):
    questions = get_random_questions(db)

    return {
        "exam_id": 1,
        "questions": [QuestionOut.model_validate(q) for q in questions]
    }
