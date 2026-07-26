import re


def detect_experience_level(resume_text, skills):

    resume_text = resume_text.lower()

    # Keywords indicating experience
    beginner_keywords = [
        "student",
        "fresher",
        "intern",
        "internship",
        "college",
        "university",
        "bachelor",
        "undergraduate"
    ]

    intermediate_keywords = [
        "software engineer",
        "developer",
        "analyst",
        "associate",
        "1 year",
        "2 years",
        "3 years",
        "worked",
        "employee"
    ]

    experienced_keywords = [
        "senior",
        "lead",
        "manager",
        "architect",
        "5 years",
        "6 years",
        "7 years",
        "8 years",
        "team lead"
    ]

    skill_count = len(skills)

    beginner_score = 0
    intermediate_score = 0
    experienced_score = 0

    # Skill-based scoring
    if skill_count <= 8:
        beginner_score += 3
    elif skill_count <= 15:
        intermediate_score += 3
    else:
        experienced_score += 3

    # Resume keyword scoring
    for word in beginner_keywords:
        if word in resume_text:
            beginner_score += 1

    for word in intermediate_keywords:
        if word in resume_text:
            intermediate_score += 1

    for word in experienced_keywords:
        if word in resume_text:
            experienced_score += 1

    scores = {
        "Beginner": beginner_score,
        "Intermediate": intermediate_score,
        "Experienced": experienced_score
    }

    level = max(scores, key=scores.get)

    return {
        "experience_level": level,
        "scores": scores
    }