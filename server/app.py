from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv, Action

app = FastAPI()

env = EmailEnv()

# ===== Models =====
class ActionInput(BaseModel):
    label: str

# ===== RESET =====
@app.post("/reset")
def reset():
    obs = env.reset()
    return {"email": obs.email}

# ===== STEP =====
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

# ===== STATE =====
@app.get("/state")
def state():
    return env.state()

# ===== ROOT =====
@app.get("/")
def root():
    return {"status": "running"}
