from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

latest_command = ""  # temporary memory

class CommandRequest(BaseModel):
    command: str
    key: str

API_KEY = "hawkeyeban"  # CHANGE THIS!!!

@app.post("/run")
def run_command(cmd: CommandRequest):
    global latest_command
    if cmd.key != API_KEY:
        return {"status": "unauthorized"}

    latest_command = cmd.command
    return {"status": "ok"}

@app.get("/poll")
def poll():
    global latest_command
    cmd = latest_command
    latest_command = ""
    return {"command": cmd}

