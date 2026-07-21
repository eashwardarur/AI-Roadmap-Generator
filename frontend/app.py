import streamlit as st
import requests


st.title("🚀 AI Career Roadmap Generator")


roles = [
    "AI Engineer",
    "Machine Learning Engineer",
    "Data Scientist",
    "Data Analyst",
    "Software Developer",
    "Frontend Developer",
    "Backend Developer",
    "DevOps Engineer",
    "Cloud Engineer",
    "Cyber Security Analyst",
    "Digital Marketing Specialist",
    "Financial Analyst",
    "HR Manager",
    "Business Analyst",
    "UI/UX Designer"
]


goal = st.selectbox(
    "Choose Career Goal",
    roles
)


if st.button("Generate Roadmap"):

    response = requests.post(
        "http://127.0.0.1:8000/generate-roadmap",
        json={
            "goal": goal
        }
    )


    if response.status_code == 200:

        data = response.json()

        st.subheader(
            f"Roadmap for {goal}"
        )

        st.write(
            data["roadmap"]
        )

    else:
        st.error("Backend Error")