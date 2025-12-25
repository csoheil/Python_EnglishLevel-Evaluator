from app.services.scoring import calculate_score, map_score_to_cefr


class MockQuestion:
    def __init__(self, qid, correct_option):
        self.id = qid
        self.correct_option = correct_option


def test_calculate_score_all_correct():
    questions = [
        MockQuestion(1, "A"),
        MockQuestion(2, "B"),
        MockQuestion(3, "C"),
    ]

    answers = {
        1: "A",
        2: "B",
        3: "C",
    }

    score = calculate_score(questions, answers)
    assert score == 3


def test_calculate_score_partial_correct():
    questions = [
        MockQuestion(1, "A"),
        MockQuestion(2, "B"),
        MockQuestion(3, "C"),
    ]

    answers = {
        1: "A",
        2: "D",
        3: "C",
    }

    score = calculate_score(questions, answers)
    assert score == 2


def test_map_score_to_cefr():
    assert map_score_to_cefr(2) == "A1"
    assert map_score_to_cefr(6) == "A2"
    assert map_score_to_cefr(9) == "B1"
    assert map_score_to_cefr(13) == "B2"
    assert map_score_to_cefr(16) == "C1"
    assert map_score_to_cefr(19) == "C2"
