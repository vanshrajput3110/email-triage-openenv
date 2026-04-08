import os
from openai import OpenAI
from env import EmailEnv, Action

client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=os.environ["API_BASE_URL"]
)

MODEL = os.environ.get("MODEL_NAME", "gpt-4o-mini")

env = EmailEnv()

print("[START]")

obs = env.reset()
total_reward = 0

for step in range(5):
    prompt = f"Classify this email into spam, important, or normal:\n{obs.email}"

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content.lower()

    # simple extraction
    if "spam" in output:
        label = "spam"
    elif "important" in output:
        label = "important"
    else:
        label = "normal"

    action = Action(label=label)
    obs, reward, done, info = env.step(action)

    total_reward += reward.value
    print(f"[STEP] step={step} reward={reward.value}")

print(f"[END] total_reward={total_reward}")
