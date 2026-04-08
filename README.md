# Email Triage OpenEnv

## Overview
This project implements an OpenEnv-compatible environment that simulates real-world email triage tasks.

The agent must classify emails and take appropriate actions similar to how humans manage inboxes.

## Tasks
- Easy: Classify email as spam or normal
- Medium: Classify email as important or normal
- Hard: Generate appropriate response (simulated)

## Observation Space
- Email text (string)

## Action Space
- Label: spam / normal / important

## Reward System
- Correct classification: +1
- Incorrect classification: -0.5

## How to Run
```bash
python inference.py

## Output
[START]
[STEP] step=0 reward=...
[END] total_reward=...
