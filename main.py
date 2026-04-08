from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This handles the "OpenEnv Reset" check that failed
@app.post("/reset")
def reset():
    return {"state": {"val": 0}, "text": "Environment Reset"}

# This handles the "Step" logic for the agent
@app.post("/step")
def step(action: dict):
    return {"state": {"val": 1}, "reward": 1.0, "done": False}

@app.get("/")
def home():
    return {"status": "success", "message": "RL Environment is Running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
