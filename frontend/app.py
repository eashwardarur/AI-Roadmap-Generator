import streamlit as st
import requests

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Advisor")
st.write("Upload your resume and get AI-powered career recommendations.")

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    if st.button("🔍 Analyze Resume"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue()
            )
        }

        response = requests.post(
            "http://127.0.0.1:8000/upload-resume",
            files=files
        )

        if response.status_code == 200:

            data = response.json()

            st.success("Resume Uploaded Successfully ✅")

            # -------------------------
            # Skills
            # -------------------------

            st.header("🛠 Detected Skills")

            st.write(", ".join(data["skills"]))

            # -------------------------
            # Experience
            # -------------------------

            st.header("📈 Experience Level")

            level = data["experience_level"]

            if level == "Beginner":
                st.success("🟢 Beginner")

            elif level == "Intermediate":
                st.warning("🟡 Intermediate")

            else:
                st.error("🔴 Experienced")

            # -------------------------
            # Recommended Role
            # -------------------------

            st.header("🎯 Recommended Career")

            st.success(data["recommended_role"])

            # -------------------------
            # Career Matches
            # -------------------------

            st.header("🏆 Top Career Matches")

            for career in data["career_matches"]:

                st.subheader(
                    f"{career['career']} ({career['match_percentage']}%)"
                )

                st.progress(career["match_percentage"] / 100)

                st.write("✅ Matched Skills")

                st.write(", ".join(career["matched_skills"]))

                st.write("❌ Missing Skills")

                st.write(", ".join(career["missing_skills"]))

                st.divider()

            # -------------------------
            # Learning Plan
            # -------------------------

            st.header("📚 Personalized Learning Plan")

            for week in data["learning_plan"]:

                st.write(
                    f"**Week {week['week']}** → {week['learn']}"
                )

        else:

            st.error("Something went wrong.")