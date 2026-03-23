from main import Problem, app


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