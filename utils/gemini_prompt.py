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
You are an expert in phonetics and English accents. Your task is to classify a speaker’s English accent based on their speech transcript. Only respond if you are confident based on clear accent patterns in word choice, grammar, or syntax.

Instructions:
- Guidelines:
- Base your classification on vocabulary, phrasing, grammatical structure, idioms, and known regional variations.
- Respond using a realistic and geographically relevant label (e.g., "Indian", "Nigerian", "British", "American", "Filipino", "Kenyan", "South African", "Middle Eastern", "Caribbean", etc.)
- You may also use broader regional labels when specificity is not possible (e.g., "West African", "Southeast Asian", "European (non-UK)", "Latin American").
- If the transcript does not provide enough evidence to confidently classify the accent, respond with "Unknown".
- Confidence should be a number from 0 to 100, where:
  - 90+ = Accent is very clear and distinctive
  - 70–89 = Likely, but not guaranteed
  - 40–69 = Uncertain, weak indicators
  - <40 = Most likely unknown
- Provide a realistic confidence score from 0 to 100 (not always high)
- Explain your decision in one short sentence using accent-specific traits (e.g., vocabulary, pronunciation, sentence structure)

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
