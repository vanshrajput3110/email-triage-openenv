def grade_easy(pred, actual):
    return 1.0 if pred == actual else 0.0


def grade_medium(pred, actual):
    return 1.0 if pred == actual else 0.0


def grade_hard(pred, expected_keywords):
    score = 0
    for word in expected_keywords:
        if word in pred.lower():
            score += 1
    return score / len(expected_keywords)