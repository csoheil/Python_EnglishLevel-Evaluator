from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.result import Result

router = APIRouter(
    prefix="/progress",
    tags=["Progress"],
)


@router.get("/")
def get_user_progress(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Return user's exam progress over time.
    """
    results = (
        db.query(Result)
        .filter(Result.user_id == current_user.id)
        .order_by(Result.created_at.asc())
        .all()
    )

    return [
        {
            "date": r.created_at,
            "score": r.score,
            "total": r.total,
            "cefr_level": r.cefr_level,
        }
        for r in results
    ]
