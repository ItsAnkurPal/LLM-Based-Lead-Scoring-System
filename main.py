from fastapi import FastAPI
from pydantic import BaseModel
from scoring import get_lead_score
app = FastAPI(title="LLM Lead Scoring API")

# Defining the base model
class Lead(BaseModel):
    name: str
    email: str
    company: str
    title: str
    inquiry: str
    source: str
    industry: str
    location: str

@app.post("/score")
def score_lead(lead: Lead):
    result = get_lead_score(lead.model_dump())
    return {
        "lead": lead.model_dump(),
        "score": result["score"],
        "category": result["category"],
        "explanation": result["explanation"]
    }
