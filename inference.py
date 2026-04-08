from env import EmailEnv, Action

# ===== Initialize environment =====
env = EmailEnv()

print("[START]")

obs = env.reset()
total_reward = 0
step_count = 0

while True:
    email = obs.email.lower()

    # ===== Dummy classification logic (no API needed) =====
    if "win" in email or "offer" in email:
        label = "spam"
    elif "meeting" in email or "report" in email:
        label = "important"
    else:
        label = "normal"

    action = Action(label=label)

    obs, reward, done, info = env.step(action)

    print(f"[STEP] step={step_count} reward={reward.value}")

    total_reward += reward.value
    step_count += 1

    if done:
        break

print(f"[END] total_reward={total_reward}")