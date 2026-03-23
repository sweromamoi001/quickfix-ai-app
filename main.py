from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()

class Problem(BaseModel):
    description: str

@app.get("/")
def home():
    return {"message": "QuickFix API Running 🚀"}

{
  "description": "My sink is leaking"
}     # type: ignore