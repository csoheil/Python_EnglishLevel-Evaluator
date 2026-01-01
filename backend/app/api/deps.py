# backend/app/api/deps.py

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db


def get_db_session(db: Session = Depends(get_db)) -> Session:
    """
    Shared database session dependency.
    """
    return db
