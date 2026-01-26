from app.db.session import engine
from app.models.base import Base

# import models so SQLAlchemy knows them
from app.models.user import User
from app.models.question import Question
from app.models.exam import Exam

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created  successfully")

if __name__ == "__main__":
    create_tables()
