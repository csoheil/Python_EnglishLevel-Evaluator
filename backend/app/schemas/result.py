from pydantic import BaseModel


class ResultResponse(BaseModel):
    score: int
    total: int
    cefr_level: str
