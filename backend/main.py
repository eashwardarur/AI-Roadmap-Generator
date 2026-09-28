from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil
import os
from roadmap import generate_roadmap
from resume_parser import extract_text
from skill_matcher import extract_skills
from recommendation import build_report

# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="AI Career Advisor API",
    description="AI-powered career recommendation and roadmap API",
    version="1.0.0"
)


# ============================================================
# UPLOAD CONFIGURATION
# ============================================================

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ============================================================
# REQUEST MODEL
# ============================================================

class RoadmapRequest(BaseModel):
    goal: str


# ============================================================
# HOME / HEALTH CHECK
# ============================================================

@app.get("/")
def home():

    return {
        "message": "AI Career Recommendation API is Running!",
        "status": "success"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "AI Career Advisor API"
    }


# ============================================================
# GENERATE ROADMAP
# ============================================================

@app.post("/generate-roadmap")
def create_roadmap(request: RoadmapRequest):

    try:

        if not request.goal.strip():

            raise HTTPException(
                status_code=400,
                detail="Career goal cannot be empty."
            )

        roadmap = generate_roadmap(
            request.goal
        )

        return {
            "status": "success",
            "goal": request.goal,
            "roadmap": roadmap
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Roadmap generation failed: {str(e)}"
        )


# ============================================================
# UPLOAD AND ANALYZE RESUME
# ============================================================

@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    # --------------------------------------------------------
    # Validate file
    # --------------------------------------------------------

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )


    # --------------------------------------------------------
    # Validate extension
    # --------------------------------------------------------

    allowed_extensions = [
        ".pdf",
        ".docx"
    ]

    file_extension = os.path.splitext(
        file.filename
    )[1].lower()

    if file_extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )


    # --------------------------------------------------------
    # Save file
    # --------------------------------------------------------

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    try:

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        # ----------------------------------------------------
        # Extract resume text
        # ----------------------------------------------------

        resume_text = extract_text(
            file_path
        )

        if not resume_text:

            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the resume."
            )


        # ----------------------------------------------------
        # Extract skills
        # ----------------------------------------------------

        skills = extract_skills(
            resume_text
        )


        # ----------------------------------------------------
        # Generate career report
        # ----------------------------------------------------

        report = build_report(
            resume_text,
            skills
        )


        # ----------------------------------------------------
        # Return response
        # ----------------------------------------------------

        return {

            "status": "success",

            "filename": file.filename,

            "skills": skills,

            "experience_level":
                report["experience"]["experience_level"],

            "career_matches":
                report["career_matches"],

            "recommended_role":
                report["recommended_role"],

            "learning_plan":
                report["learning_plan"]

        }


    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Resume analysis failed: {str(e)}"
        )


# ============================================================
# RUN DIRECTLY
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )