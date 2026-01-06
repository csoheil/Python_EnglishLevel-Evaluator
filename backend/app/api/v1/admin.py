from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.result import Result

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/cefr-distribution")
def cefr_distribution(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Return CEFR level distribution.
    Admin-only logic can be added later.
    """
    rows = (
        db.query(Result.cefr_level, func.count(Result.id))
        .group_by(Result.cefr_level)
        .all()
    )

    return {level: count for level, count in rows}
