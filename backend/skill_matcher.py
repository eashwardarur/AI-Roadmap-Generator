import re

KNOWN_SKILLS = [

    # Programming
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",

    # Frontend
    "html",
    "css",
    "react",
    "angular",
    "vue",

    # Backend
    "node.js",
    "express",
    "django",
    "flask",
    "fastapi",
    "spring boot",

    # Database
    "sql",
    "mysql",
    "oracle",
    "postgresql",
    "mongodb",
    "redis",

    # Data Science
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scikit-learn",

    # AI
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "nlp",
    "computer vision",
    "llm",
    "langchain",
    "rag",

    # Cloud
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "jenkins",

    # Others
    "git",
    "linux",
    "power bi",
    "tableau",
    "excel"

]


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in KNOWN_SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found.append(skill.title())

    return sorted(list(set(found)))