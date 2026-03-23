from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()

class Problem(BaseModel):
    description: str

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


@app.get("/")
def home():
    return {"message": "QuickFix API Running 🚀"}

