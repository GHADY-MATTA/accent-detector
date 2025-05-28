import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

chat = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.5,
    top_k=40,
    top_p=0.95,
    google_api_key=google_api_key
)

prompt = "Say hello from Gemini AI."

response = chat.invoke([HumanMessage(content=prompt)])

print("Gemini response:", response.content)
