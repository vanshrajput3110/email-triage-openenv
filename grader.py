def grade_easy(pred, actual):
    return 0.9 if pred == actual else 0.2

def grade_medium(pred, actual):
    return 0.85 if pred == actual else 0.3

def grade_hard(pred, expected_keywords):
    return 0.6
