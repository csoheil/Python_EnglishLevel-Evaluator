def calculate_score(questions, answers: dict) -> int:
    score = 0
    for question in questions:
        submitted = answers.get(question.id)
        if submitted and submitted.upper() == question.correct_option.upper():
            score += 1
    return score


def map_score_to_cefr(score: int) -> str:
    if score <= 4:
        return "A1"
    if score <= 7:
        return "A2"
    if score <= 10:
        return "B1"
    if score <= 14:
        return "B2"
    if score <= 17:
        return "C1"
    return "C2"
