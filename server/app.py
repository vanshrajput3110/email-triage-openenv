from fastapi import FastAPI
import uvicorn
from env import EmailEnv, Action
from pydantic import BaseModel

app = FastAPI()
env = EmailEnv()

class ActionInput(BaseModel):
    label: str

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"email": obs.email}

@app.post("/step")
def step(action: ActionInput):
    act = Action(label=action.label)
    obs, reward, done, info = env.step(act)

    return {
        "observation": None if obs is None else obs.email,
        "reward": reward.value,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()

@app.get("/")
def root():
    return {"status": "running"}

# ===== REQUIRED MAIN FUNCTION =====
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ===== REQUIRED ENTRY POINT =====
if __name__ == "__main__":
    main()
