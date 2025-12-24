from pydantic import BaseModel
from typing import Dict


class AdminAnalyticsResponse(BaseModel):
    total_exams: int
    average_score: float
    cefr_distribution: Dict[str, int]
