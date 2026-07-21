from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

for model in client.models.list():
    print(model.name)
    print("Supported actions:", getattr(model, "supported_actions", "N/A"))
    print("-" * 50)