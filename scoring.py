import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=genai.api_key)

# Ensuring the Gemini API key is set
if not genai.api_key:
    raise ValueError("Gemini API key is not set. Please set the GEMINI_API_KEY environment variable.")

# Category labels based on score
def categorize(score):
    if score >= 80:
        return "Hot"
    elif score >= 60:
        return "Warm"
    else:
        return "Cold"

# Build the prompt for LLM
def build_prompt(lead):
    return f"""
You are an expert in lead qualification. Analyze the following lead and assign a score from 0 to 100 based on:
- Buying intent (how interested they seem)
- Company fit (e.g., industry, size)
- Job title relevance (decision-maker or not)
- Source quality 

LEAD DETAILS:
Name: {lead['name']}
Email: {lead['email']}
Company: {lead['company']}
Title: {lead['title']}
Industry: {lead['industry']}
Location: {lead['location']}
Source: {lead['source']}
Inquiry Message: "{lead['inquiry']}"

Respond in this format (JSON only, no markdown or extra text):
{{
  "score": 85,
  "explanation": "Strong buying intent, relevant title, came via demo request."
}}
"""

# Sending Data to LLM(gemini) and parse response
def get_lead_score(lead):
    prompt = build_prompt(lead)

    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)

    try:
        result_raw = response.text.strip()

        # Remove markdown formatting if present
        if result_raw.startswith("```"):
            result_raw = result_raw.strip("```json").strip("` \n")

        # Convert string to dict
        result = json.loads(result_raw)

        score = int(result["score"])
        explanation = result["explanation"]

        return {
            "score": score,
            "category": categorize(score),
            "explanation": explanation
        }

    except Exception as e:
        print(" Error parsing LLM output:", e)
        print(" Raw response was:", response.text)
        return {
            "score": 0,
            "category": "Cold",
            "explanation": "LLM parsing failed."
        }
