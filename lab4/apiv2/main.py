from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from fastapi.security.api_key import APIKeyHeader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("nikki_key")  # Match environment variable name with the one in .env
API_KEY_NAME = "nikki_key"  # Header name expected to pass the API key
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# App initialization
app = FastAPI()

# Database
task_db = [
    {"id": 1, "name": "Laboratory Activity", "des": "Create Lab Act 1", "is_finished": False},
    {"id": 2, "name": "Laboratory Activity", "des": "Create Lab Act 2", "is_finished": False},
    {"id": 3, "name": "Laboratory Activity", "des": "Create Lab Act 3", "is_finished": False}
]

# Task model
class Task(BaseModel):
    id: int
    name: str
    des: str
    is_finished: bool

# Dependency: API key validation
def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
    return api_key

# Endpoints

@app.get("/tasks/{id}")
def get_task(id: int, api_key: str = Depends(get_api_key)):
    if not task_db:
        raise HTTPException(status_code=404, detail="No tasks available")
    for task in task_db:
        if task["id"] == id:
            return {"status": "ok", "result": task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", status_code=201)
def create_task(task: Task, api_key: str = Depends(get_api_key)):
    if any(t["id"] == task.id for t in task_db):
        raise HTTPException(status_code=400, detail="Task ID already exists")
    task_db.append(task.dict())
    return {"status": "ok"}

@app.patch("/tasks/{id}", status_code=204)
def update_task(id: int, task: Task, api_key: str = Depends(get_api_key)):
    for idx, t in enumerate(task_db):
        if t["id"] == id:
            task_db[idx].update(task.dict())  # Update only specific fields in the task
            return
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int, api_key: str = Depends(get_api_key)):
    for task in task_db:
        if task["id"] == id:
            task_db.remove(task)
            return
    raise HTTPException(status_code=404, detail="Task not found")
