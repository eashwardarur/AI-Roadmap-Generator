from experience_detector import detect_experience_level
from career_matcher import recommend_careers
from learning_plan import generate_learning_plan


def build_report(resume_text, skills):

    experience = detect_experience_level(
        resume_text,
        skills
    )

    careers = recommend_careers(
        skills
    )

    best = careers[0]

    roadmap = generate_learning_plan(
        best["missing_skills"]
    )

    return {

        "experience": experience,

        "recommended_role": best["career"],

        "career_matches": careers,

        "learning_plan": roadmap

    }