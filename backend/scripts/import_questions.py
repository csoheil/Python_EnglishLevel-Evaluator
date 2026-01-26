import csv
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.question import Question


def import_questions_from_csv(file_path: str):
    """
    Import questions from a CSV file.
    CSV columns:
    text, option_a, option_b, option_c, option_d, correct_option, difficulty
    """
    db: Session = SessionLocal()

    try:
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            questions = []

            for row in reader:
                question = Question(
                    text=row["text"],
                    option_a=row["option_a"],
                    option_b=row["option_b"],
                    option_c=row["option_c"],
                    option_d=row["option_d"],
                    correct_option=row["correct_option"],
                    difficulty=row.get("difficulty"),
                )
                questions.append(question)

                # Bulk insert every 1000 rows (important for performance)
                if len(questions) >= 1000:
                    db.bulk_save_objects(questions)
                    db.commit()
                    questions.clear()

            if questions:
                db.bulk_save_objects(questions)
                db.commit()

        print("Quaestions imported successfully")

    except Exception as e:
        db.rollback()
        print(f" Import failed: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    import_questions_from_csv("questions.csv")
