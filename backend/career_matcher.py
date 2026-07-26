from careers import CAREER_ROADMAPS


CAREER_SKILLS = {

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Tensorflow",
        "Pytorch",
        "SQL",
        "NLP",
        "Computer Vision",
        "AWS",
        "Docker",
        "Langchain",
        "Fastapi"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Scikit-Learn",
        "Tensorflow",
        "Pytorch",
        "Docker",
        "AWS",
        "SQL"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Pandas",
        "Numpy",
        "Machine Learning",
        "Statistics",
        "Power BI",
        "Tableau"
    ],

    "Backend Developer": [
        "Python",
        "Fastapi",
        "Flask",
        "Django",
        "SQL",
        "MongoDB",
        "Git"
    ],

    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ],

    "Cloud Engineer": [
        "AWS",
        "Docker",
        "Linux",
        "Git",
        "Kubernetes"
    ],

    "DevOps Engineer": [
        "Linux",
        "Docker",
        "AWS",
        "Git",
        "Jenkins",
        "Kubernetes"
    ]
}


def recommend_careers(user_skills):

    recommendations = []

    user_skills = set(user_skills)

    for career, required_skills in CAREER_SKILLS.items():

        matched = user_skills.intersection(required_skills)

        percentage = round(
            (len(matched) / len(required_skills)) * 100
        )

        recommendations.append({

            "career": career,

            "match_percentage": percentage,

            "matched_skills": list(matched),

            "missing_skills": list(
                set(required_skills) - matched
            )

        })

    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations[:5]