from grader import grade_easy, grade_medium, grade_hard

...

obs = env.reset()
total_reward = 0

for step in range(5):
    prompt = f"Classify this email into spam, important, or normal:\n{obs.email}"

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        output = response.choices[0].message.content.lower()
    except Exception:
        output = "normal"

    # prediction
    if "spam" in output:
        label = "spam"
    elif "important" in output:
        label = "important"
    else:
        label = "normal"

    action = Action(label=label)

    # 👉 GET CORRECT ANSWER
    correct = env.data[env.index]["label"]

    # 👉 APPLY DIFFERENT GRADERS
    if step == 0:
        score = grade_easy(label, correct)
    elif step == 1:
        score = grade_medium(label, correct)
    else:
        score = grade_hard(label, ["response"])

    obs, reward, done, info = env.step(action)

    total_reward += score  # use grader score

    print(f"[STEP] step={step} reward={score}")

print(f"[END] total_reward={total_reward}")
