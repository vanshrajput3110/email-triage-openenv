from grader import grade_easy, grade_medium, grade_hard

tasks = [
    {
        "name": "easy",
        "description": "Spam classification",
        "grader": grade_easy
    },
    {
        "name": "medium",
        "description": "Priority classification",
        "grader": grade_medium
    },
    {
        "name": "hard",
        "description": "Response generation",
        "grader": grade_hard
    }
]
