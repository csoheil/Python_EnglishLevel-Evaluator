from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.exam import Exam
from app.api.deps import get_current_user

router = APIRouter(
    prefix="/history",
    tags=["History"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/")
def get_exam_history(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    exams = (
        db.query(Exam)
        .filter(Exam.user_id == current_user.id)
        .order_by(Exam.id.desc())
        .all()
    )

    return exams
