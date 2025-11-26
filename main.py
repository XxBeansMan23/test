from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

latest_command = ""  # temporary memory

class CommandRequest(BaseModel):
    command: str
    key: str

API_KEY = "https://discord.com/api/webhooks/1382074236751057008/yEP6avmLcMgOYURbbxLazD43ugPuPKjYaTXeJ9XnBZ262ogYXbw1IF4ysYHETPZ6HIxj"  # CHANGE THIS!!!

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
