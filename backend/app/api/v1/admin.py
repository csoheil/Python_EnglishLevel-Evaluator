from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.session import get_db
from app.models.exam import Exam
from app.api.deps import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/analytics")
def get_exam_analytics(db: Session = Depends(get_db)):
    """
    Return global analytics for admin dashboard.
    """

    total_exams = db.query(func.count(Exam.id)).scalar()
    average_score = db.query(func.avg(Exam.score)).scalar()

    cefr_stats = (
        db.query(Exam.cefr_level, func.count(Exam.id))
        .group_by(Exam.cefr_level)
        .all()
    )

    return {
        "total_exams": total_exams,
        "average_score": round(average_score or 0, 2),
        "cefr_distribution": {
            level: count for level, count in cefr_stats
        },
    }
