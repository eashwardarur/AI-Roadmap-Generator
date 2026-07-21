from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="""
    Create a 6-month roadmap for becoming an AI Engineer.
    Include:
    - Monthly goals
    - Weekly plan
    - Resources
    - Projects
    """
)

print(response.text)