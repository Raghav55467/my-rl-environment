from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/reset")
def reset():
    return {"state": {"val": 0}}

@app.post("/step")
def step(action: dict):
    return {"state": {"val": 1}, "reward": 1.0, "done": False}

@app.get("/")
def home():
    return {"status": "ok"}

# This fixes the "Server entry point should reference main function" error
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
