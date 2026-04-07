from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RL Environment is Active", "status": "Running"}

@app.get("/state")
def get_state():
    return {"val": 0}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
