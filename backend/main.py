from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from roadmap import generate_roadmap
from resume_parser import extract_text
from skill_matcher import extract_skills
from recommendation import build_report

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class RoadmapRequest(BaseModel):
    goal: str


@app.get("/")
def home():
    return {
        "message": "AI Career Recommendation API is Running!"
    }


# ----------------------------
# Generate Roadmap
# ----------------------------
@app.post("/generate-roadmap")
def create_roadmap(request: RoadmapRequest):

    roadmap = generate_roadmap(request.goal)

    return {
        "roadmap": roadmap
    }


# ----------------------------
# Upload Resume
# ----------------------------
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text(file_path)

    skills = extract_skills(resume_text)

    report = build_report(
        resume_text,
        skills
    )

    return {

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