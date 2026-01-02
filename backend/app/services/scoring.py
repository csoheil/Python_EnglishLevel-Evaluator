def calculate_cefr_level(score: int) -> str:
    """
    Map score to CEFR level using fixed thresholds.
    """
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
