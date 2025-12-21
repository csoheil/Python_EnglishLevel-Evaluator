# backend/app/api/v1/results.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict
from pydantic import BaseModel

from app.db.session import get_db
from app.models.exam import Exam
from app.models.question import Question
from app.api.deps import get_current_user  # JWT dependency

router = APIRouter(
    prefix="/results",
    tags=["Results"],
    dependencies=[Depends(get_current_user)],
)


class SubmitAnswersRequest(BaseModel):
    exam_id: int
    answers: Dict[int, str]  # question_id -> selected option ("A", "B", "C", "D")


class ResultResponse(BaseModel):
    score: int
    total: int
    cefr_level: str


@router.post("/submit", response_model=ResultResponse, status_code=status.HTTP_200_OK)
def submit_exam_answers(
    payload: SubmitAnswersRequest,
    db: Session = Depends(get_db),
    # current_user = Depends(get_current_user)  # Uncomment after auth is ready
):
    """
    Submit answers for an exam, calculate the score, determine CEFR level,
    and update the Exam record with the final score.
    """
    exam = db.query(Exam).filter(Exam.id == payload.exam_id).first()
    if not exam:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exam not found"
        )

    if exam.score is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Exam has already been submitted"
        )

    question_ids = list(payload.answers.keys())
    if not question_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No answers submitted"
        )

    questions = db.query(Question).filter(Question.id.in_(question_ids)).all()
    if len(questions) != len(question_ids):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="One or more question IDs are invalid"
        )

    score = 0
    for question in questions:
        submitted = payload.answers.get(question.id)
        if submitted and submitted.upper() == question.correct_option.upper():
            score += 1

    total = len(question_ids)

    # CEFR mapping
    if score <= 4:
        cefr_level = "A1"
    elif score <= 7:
        cefr_level = "A2"
    elif score <= 10:
        cefr_level = "B1"
    elif score <= 14:
        cefr_level = "B2"
    elif score <= 17:
        cefr_level = "C1"
    else:
        cefr_level = "C2"

    exam.score = score
    exam.cefr_level = cefr_level
    db.commit()

    return ResultResponse(score=score, total=total, cefr_level=cefr_level)
