# backend/app/schemas/exam.py

from pydantic import BaseModel
from typing import List
from app.schemas.question import QuestionResponse


class ExamStartResponse(BaseModel):
    exam_id: int
    questions: List[QuestionResponse]


class ExamResultResponse(BaseModel):
    score: int
    cefr_level: str
