from fastapi import FastAPI
from pydantic import BaseModel

from backend.roadmap import generate_roadmap


app = FastAPI()


class RoadmapRequest(BaseModel):
    goal: str


@app.get("/")
def home():
    return {
        "message": "AI Roadmap Generator API"
    }


@app.post("/generate-roadmap")
def create_roadmap(request: RoadmapRequest):

    roadmap = generate_roadmap(request.goal)

    return {
        "roadmap": roadmap
    }