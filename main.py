from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Problem(BaseModel):
    description: str

@app.get("/")
def home():
    return {"message": "QuickFix API Running 🚀"}

@app.post("/diagnose")
def diagnose(problem: Problem):
    issue = problem.description.lower()

    if "sink" in issue:
        return {
            "problem": "Possible leak",
            "solution": [
                "Check pipe connections",
                "Tighten loose fittings"
            ],
            "warning": "Turn off water before fixing"
        }

    return {
        "problem": "Unknown issue",
        "solution": ["Try basic troubleshooting"],
        "warning": "Consult technician if unsure"
    }
    