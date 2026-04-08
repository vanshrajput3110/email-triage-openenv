from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Email Triage Env</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>📧 Email Triage Environment</h1>
            <p>Status: Running ✅</p>
            <p>This environment evaluates AI on email classification tasks.</p>
        </body>
    </html>
    """
