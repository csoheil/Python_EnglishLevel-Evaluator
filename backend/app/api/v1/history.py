from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.exam import Exam
from app.api.deps import get_current_user
from app.services.pagination import paginate

router = APIRouter(
    prefix="/history",
    tags=["History"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/")
def get_exam_history(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    query = (
        db.query(Exam)
        .filter(Exam.user_id == current_user.id)
        .order_by(Exam.id.desc())
    )

    exams, total = paginate(query, page, page_size)

    return {
        "data": exams,
        "meta": {
            "page": page,
            "page_size": page_size,
            "total": total,
        },
    }
