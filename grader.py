def grade_easy(pred, actual):
    if pred == actual:
        return 0.9
    else:
        return 0.2


def grade_medium(pred, actual):
    if pred == actual:
        return 0.85
    else:
        return 0.3


def grade_hard(pred, expected_keywords):
    score = 0
    for word in expected_keywords:
        if word in pred.lower():
            score += 1

    if len(expected_keywords) == 0:
        return 0.5

    ratio = score / len(expected_keywords)

    # ensure strictly between 0 and 1
    return max(0.1, min(0.9, ratio))
