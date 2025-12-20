# backend/app/schemas/question.py

from pydantic import BaseModel


class QuestionResponse(BaseModel):
    id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str

    class Config:
        from_attributes = True
