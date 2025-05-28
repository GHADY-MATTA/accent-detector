import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from datetime import datetime

# Load .env and API key
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

# Initialize Gemini chat model
chat = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.5,
    top_k=40,
    top_p=0.95,
    google_api_key=google_api_key,
    # api_version="v1beta"
)

LOG_RESPONSE_FILE = "logs/gemini_responses.txt"
os.makedirs("logs", exist_ok=True)

def clean_gemini_response(raw_response: str) -> str:
    cleaned = raw_response.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[len("```json"):].strip()
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3].strip()
    return cleaned

def analyze_accent(transcript: str) -> dict:
    prompt = f"""
You are an expert in accent detection. Based on the transcript below, classify the speaker's English accent.

Instructions:
- Only choose from: American, British, Australian, Indian, African, Canadian
- Provide a confidence score (0–100)
- Write a 1-sentence explanation

Transcript:
\"\"\"
{transcript}
\"\"\"

Respond in this exact JSON format:
{{
  "accent": "...",
  "confidence": ...,
  "summary": "..."
}}
"""

    response = chat.invoke([HumanMessage(content=prompt)])

    # Log raw Gemini response with timestamp
    with open(LOG_RESPONSE_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- Gemini Response @ {datetime.now()} ---\n")
        f.write(response.content + "\n")
        f.write("--- End of Response ---\n")

    try:
        cleaned_content = clean_gemini_response(response.content)
        parsed = json.loads(cleaned_content)
        return parsed
    except json.JSONDecodeError as e:
        return {
            "accent": "unknown",
            "confidence": 0,
            "summary": f"Failed to parse Gemini response: {e}"
        }
