import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY", "")
if not API_KEY:
    raise ValueError("❌ Please set GEMINI_API_KEY environment variable.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
