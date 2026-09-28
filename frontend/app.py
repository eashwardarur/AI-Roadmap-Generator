import streamlit as st
import requests
# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="CareerAI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
/* Main text */
.stApp {
    background-color: #f5f7fb;
    color: #111827;
}

/* All normal text */
.stMarkdown,
.stCaption,
p,
label {
    color: #111827;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #111827 !important;
}

/* Hero text */
.hero-box h1 {
    color: white !important;
}

.hero-box p {
    color: white !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] * {
    color: #f9fafb;
}

/* Captions */
.stCaption {
    color: #6b7280 !important;
}

/* File uploader text */
[data-testid="stFileUploader"] {
    color: #111827;
}

[data-testid="stFileUploader"] label {
    color: #111827 !important;
}

/* Selectbox text */
[data-baseweb="select"] * {
    color: #111827 !important;
}

/* Input text */
input {
    color: #111827 !important;
}

/* Info / success messages */
.stAlert p {
    color: #111827 !important;
}
   
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<p class="sidebar-title">🚀 Career<span>AI</span></p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sidebar-text">Your personal AI career advisor</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### Navigation")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Career Roadmap",
            "Skills Analysis",
            "Job Recommendations",
            "Learning Plan"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### 🎯 Career Goal")

    target_role = st.selectbox(
        "Select your target role",
        [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Backend Developer",
            "Frontend Developer",
            "Cloud Engineer",
            "DevOps Engineer"
        ]
    )

    st.markdown("---")

    st.caption("CareerAI v1.0")
    st.caption("Powered by AI 🤖")


# ============================================================
# HERO
# ============================================================

if page == "Dashboard":

    st.markdown(
        """
        <div class="hero-box">
        """,
        unsafe_allow_html=True
    )

    st.markdown("# 🚀 Build Your Future with AI")

    st.markdown(
        """
        Upload your resume, discover your strongest career
        matches, identify skill gaps, and get a personalized
        learning roadmap.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.markdown("## 📄 Analyze Your Resume")

    st.caption(
        "Upload your resume and let AI analyze your skills, "
        "experience and career opportunities."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.info(
            f"📄 Selected file: {uploaded_file.name}"
        )

        if st.button(
            "🔍 Analyze Resume",
            use_container_width=True
        ):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue()
                )
            }

            try:

                with st.spinner(
                    "🤖 AI is analyzing your resume..."
                ):

                    response = requests.post(
                        "http://127.0.0.1:8000/upload-resume",
                        files=files,
                        timeout=120
                    )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        "✅ Resume analyzed successfully!"
                    )

                    # ====================================================
                    # OVERVIEW
                    # ====================================================

                    st.markdown("## 📊 Resume Overview")

                    career_matches = data.get(
                        "career_matches",
                        []
                    )

                    best_match = 0

                    if career_matches:

                        best_match = max(
                            career.get(
                                "match_percentage",
                                0
                            )
                            for career in career_matches
                        )

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:

                        st.markdown(
                            """
                            <div class="metric-box">
                            """,
                            unsafe_allow_html=True
                        )

                        st.markdown("👤")

                        st.markdown(
                            '<p class="metric-label">Experience Level</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            f'<p class="metric-number">{data.get("experience_level", "N/A")}</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown("</div>", unsafe_allow_html=True)

                    with col2:

                        st.markdown(
                            """
                            <div class="metric-box">
                            """,
                            unsafe_allow_html=True
                        )

                        st.markdown("💼")

                        st.markdown(
                            '<p class="metric-label">Recommended Role</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            f'<p class="metric-number">{data.get("recommended_role", "N/A")}</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown("</div>", unsafe_allow_html=True)

                    with col3:

                        st.markdown(
                            """
                            <div class="metric-box">
                            """,
                            unsafe_allow_html=True
                        )

                        st.markdown("💻")

                        st.markdown(
                            '<p class="metric-label">Skills Detected</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            f'<p class="metric-number">{len(data.get("skills", []))}</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown("</div>", unsafe_allow_html=True)

                    with col4:

                        st.markdown(
                            """
                            <div class="metric-box">
                            """,
                            unsafe_allow_html=True
                        )

                        st.markdown("📈")

                        st.markdown(
                            '<p class="metric-label">Best Career Match</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            f'<p class="metric-number">{best_match}%</p>',
                            unsafe_allow_html=True
                        )

                        st.markdown("</div>", unsafe_allow_html=True)


                    # ====================================================
                    # SKILLS + RECOMMENDED CAREER
                    # ====================================================

                    st.markdown("")

                    left, right = st.columns(2)

                    # ----------------------------------------------------
                    # SKILLS
                    # ----------------------------------------------------

                    with left:

                        st.markdown("### 💡 Detected Skills")

                        st.caption(
                            "Skills extracted from your resume"
                        )

                        skills = data.get(
                            "skills",
                            []
                        )

                        if skills:

                            for skill in skills:

                                st.markdown(
                                    f"""
                                    <span class="skill-badge">
                                        {skill}
                                    </span>
                                    """,
                                    unsafe_allow_html=True
                                )

                        else:

                            st.info(
                                "No skills detected."
                            )


                    # ----------------------------------------------------
                    # RECOMMENDED CAREER
                    # ----------------------------------------------------

                    with right:

                        st.markdown(
                            "### 🎯 Recommended Career"
                        )

                        st.caption(
                            "Based on your resume analysis"
                        )

                        role = data.get(
                            "recommended_role",
                            "Not available"
                        )

                        st.success(
                            f"🏆 {role}"
                        )

                        st.write(
                            "This role appears to be your strongest "
                            "career direction based on your current skills."
                        )


                    # ====================================================
                    # CAREER MATCH ANALYSIS
                    # ====================================================

                    st.markdown(
                        "## 🏆 Career Match Analysis"
                    )

                    st.caption(
                        "See how well your profile matches different career roles."
                    )

                    for career in career_matches:

                        career_name = career.get(
                            "career",
                            "Unknown"
                        )

                        percentage = career.get(
                            "match_percentage",
                            0
                        )

                        st.markdown(
                            f"### {career_name}   `{percentage}% Match`"
                        )

                        st.progress(
                            min(
                                percentage,
                                100
                            ) / 100
                        )

                        col1, col2 = st.columns(2)

                        with col1:

                            st.markdown(
                                "**✅ Matching Skills**"
                            )

                            matched = career.get(
                                "matched_skills",
                                []
                            )

                            if matched:

                                for skill in matched:

                                    st.markdown(
                                        f"""
                                        <span class="skill-badge">
                                            {skill}
                                        </span>
                                        """,
                                        unsafe_allow_html=True
                                    )

                            else:

                                st.caption(
                                    "No matching skills."
                                )

                        with col2:

                            st.markdown(
                                "**📌 Skills to Learn**"
                            )

                            missing = career.get(
                                "missing_skills",
                                []
                            )

                            if missing:

                                for skill in missing:

                                    st.markdown(
                                        f"""
                                        <span class="missing-badge">
                                            {skill}
                                        </span>
                                        """,
                                        unsafe_allow_html=True
                                    )

                            else:

                                st.success(
                                    "No major skill gaps!"
                                )


                    # ====================================================
                    # LEARNING ROADMAP
                    # ====================================================

                    st.markdown(
                        "## 📚 Your Learning Roadmap"
                    )

                    st.caption(
                        "Personalized learning plan based on your career goal."
                    )

                    learning_plan = data.get(
                        "learning_plan",
                        []
                    )

                    for week in learning_plan:

                        st.markdown(
                            f"""
                            <div class="roadmap-box">
                                <p class="roadmap-week">
                                    Week {week.get("week", "")}
                                </p>

                                <p class="roadmap-topic">
                                    📘 {week.get("learn", "")}
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


                    # ====================================================
                    # JOB RECOMMENDATIONS
                    # ====================================================

                    st.markdown(
                        "## 💼 Suggested Jobs"
                    )

                    jobs = {

                        "AI Engineer": [
                            "AI Engineer Intern",
                            "Junior AI Engineer",
                            "ML Engineer Intern"
                        ],

                        "Data Scientist": [
                            "Data Analyst",
                            "Junior Data Scientist",
                            "Business Analyst"
                        ],

                        "Backend Developer": [
                            "Python Developer",
                            "Backend Developer",
                            "API Developer"
                        ],

                        "Machine Learning Engineer": [
                            "ML Engineer",
                            "AI Developer",
                            "Data Scientist"
                        ],

                        "Frontend Developer": [
                            "Frontend Developer",
                            "React Developer",
                            "UI Developer"
                        ],

                        "Cloud Engineer": [
                            "Cloud Engineer",
                            "AWS Engineer",
                            "DevOps Associate"
                        ],

                        "DevOps Engineer": [
                            "DevOps Engineer",
                            "Cloud DevOps",
                            "Site Reliability Engineer"
                        ]
                    }

                    role = data.get(
                        "recommended_role",
                        ""
                    )

                    job_list = jobs.get(
                        role,
                        []
                    )

                    job_columns = st.columns(3)

                    for index, job in enumerate(job_list):

                        with job_columns[index % 3]:

                            st.markdown(
                                f"""
                                <div class="job-box">

                                <h4>
                                    💼 {job}
                                </h4>

                                <p>
                                    Recommended based on your
                                    career profile.
                                </p>

                                </div>
                                """,
                                unsafe_allow_html=True
                            )


                else:

                    st.error(
                        f"Backend Error: {response.status_code}"
                    )

                    try:

                        error = response.json()

                        st.error(
                            error.get(
                                "detail",
                                "Unknown backend error"
                            )
                        )

                    except Exception:
                        pass


            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Cannot connect to FastAPI backend."
                )

                st.info(
                    "Run: uvicorn backend.main:app --reload"
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏳ Resume analysis took too long. "
                    "Please try again."
                )

            except Exception as e:

                st.error(
                    f"❌ Error: {str(e)}"
                )


# ============================================================
# CAREER ROADMAP PAGE
# ============================================================

elif page == "Career Roadmap":

    st.title("🗺️ Career Roadmap")

    st.info(
        "Upload and analyze your resume from the Dashboard "
        "to generate your personalized roadmap."
    )


# ============================================================
# SKILLS ANALYSIS PAGE
# ============================================================

elif page == "Skills Analysis":

    st.title("🧠 Skills Analysis")

    st.info(
        "Upload and analyze your resume from the Dashboard "
        "to see your skill analysis."
    )


# ============================================================
# JOB RECOMMENDATIONS PAGE
# ============================================================

elif page == "Job Recommendations":

    st.title("💼 Job Recommendations")

    st.info(
        "Upload and analyze your resume from the Dashboard "
        "to get personalized job recommendations."
    )


# ============================================================
# LEARNING PLAN PAGE
# ============================================================

elif page == "Learning Plan":

    st.title("📚 Learning Plan")

    st.info(
        "Upload and analyze your resume from the Dashboard "
        "to generate your learning plan."
    )