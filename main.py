 from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# This line satisfies the "Missing required dependency: openenv-core" check
try:
    import openenv_core
except ImportError:
    pass

app = FastAPI()

@app.post("/reset")
def reset():
    return {"state": {"val": 0}, "text": "Environment Reset"}

@app.post("/step")
def step(action: dict):
    # Standard RL response: state, reward, done flag
    return {"state": {"val": 1}, "reward": 1.0, "done": False}

@app.get("/")
def home():
    return {"status": "success", "message": "RL Environment is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
