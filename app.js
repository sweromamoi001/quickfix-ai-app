async function sendProblem() {
    const problem = document.getElementById("problem").value;

    const response = await fetch("http://127.0.0.1:8000/diagnose", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ description: problem })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        `Problem: ${data.problem}
Solution: ${data.solution.join(", ")}
Warning: ${data.warning}`;
} 
 

 {
  "description"; "My sink is leaking"
}

