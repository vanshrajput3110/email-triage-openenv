from pydantic import BaseModel
class Observation(BaseModel):
    email: str
class Action(BaseModel):
    label: str  # spam / normal / important / response text
class Reward(BaseModel):
    value: float
class EmailEnv:
    def __init__(self):
        self.data = [
            {"email": "Win ₹1 lakh now!!!", "label": "spam"},
            {"email": "Meeting at 5 PM", "label": "important"},
            {"email": "Hello, how are you?", "label": "normal"},
            {"email": "Limited time offer!!!", "label": "spam"},
            {"email": "Please send the report", "label": "important"},
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        return Observation(email=self.data[self.index]["email"])

    def step(self, action: Action):
        current = self.data[self.index]
        correct_label = current["label"]

        if action.label == correct_label:
            reward = Reward(value=1.0)
        else:
            reward = Reward(value=-0.5)
        self.index += 1
        done = self.index >= len(self.data)

        if not done:
            next_obs = Observation(email=self.data[self.index]["email"])
        else:
            next_obs = None

        return next_obs, reward, done, {"correct": correct_label}

    def state(self):
        return {"current_index": self.index}
    

