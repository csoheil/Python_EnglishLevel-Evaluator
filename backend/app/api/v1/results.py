from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.result import SubmitAnswersRequest, ResultResponse
from app.services.scoring import calculate_score, map_score_to_cefr
from app.api.deps import get_current_user

router = APIRouter(
    prefix="/results",
    tags=["Results"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/submit", response_model=ResultResponse)
def submit_exam_answers(
    payload: SubmitAnswersRequest,
    db: Session = Depends(get_db),
):
    exam = db.query(Exam).filter(Exam.id == payload.exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    if exam.score is not None:
        raise HTTPException(status_code=400, detail="Exam already submitted")

    question_ids = list(payload.answers.keys())
    questions = db.query(Question).filter(Question.id.in_(question_ids)).all()

    if len(questions) != len(question_ids):
        raise HTTPException(status_code=400, detail="Invalid question IDs")

    score = calculate_score(questions, payload.answers)
    cefr_level = map_score_to_cefr(score)

    exam.score = score
    exam.cefr_level = cefr_level
    db.commit()

    return ResultResponse(
        score=score,
        total=len(question_ids),
        cefr_level=cefr_level,
    )
