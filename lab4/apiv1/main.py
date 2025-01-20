 
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Instantiates the FastAPI class
app = FastAPI()

# Handles the format of the object instantiated by the User class
# This extends the BaseModel to ensure proper mapping of the FastAPI to the
# User class
class Task(BaseModel):
    id: int
    name: str
    des: str
    is_finished: bool

# datas
task_db = [
    {"id": 1, "name": "Laboratory Activity", "des": "Create Lab Act 1", "is_finished": False},
    {"id": 2, "name": "Laboratory Activity", "des": "Create Lab Act 2", "is_finished": False},
    {"id": 3, "name": "Laboratory Activity", "des": "Create Lab Act 3", "is_finished": False}
]

# get
@app.get("/tasks/{id}") 
def read_users(task_no: Optional[int] = None):
    # Check if the task_id is provided
    if task_no is not None:        
        # Find user by task_id
        if task_no < 1:
                return {"error": "task Id should not be lower than 1!"}
        
        for u in task_db:
            # If the task_id matches the value in the task_db
            # Return value of task
            if u["id"] == task_no:
                return {"status": "ok", "result" : u}
     
        # Return value if task is not found
        return{"error": "The task id cannot found in the database!"}

    return {"error": "You need to provide the task id to view the data from"}

# post
@app.post("/tasks") 
def create_task(task: Task): 
    # Check of task ID is available in the task_db list
    # IF already existing, return error
    if any(u['id'] == task.id for u in task_db):
        return {"error": "Task Id is already existing"}
    
    # If task_id is not yet existing, we append the passed Task object to the task_db list
    # Take note that we are casting the task object to dict so that it matches the data type
    # Of the contents of task_db
    task_db.append(dict(task))
    return {"status": "ok"}

# patch
@app.patch("/tasks/{id}")
def update_task(id: int, task: Task):  
     # Check if the Task_id is provided
    if id:
        # Find task by task_id
        for idx, u in enumerate(task_db):
            # If the task_id in the task_db matches the inputted task_id from the parameter
            # Update the values of the keys in task_db
            # Then return a status "ok" and show the updated data
            if u["id"] == id:
                task_db[idx]['id'] = task.id 
                task_db[idx]['name'] = task.name
                task_db[idx]['des'] = task.des
                task_db[idx]['is_finished'] = task.is_finished

                return {"status": "ok", "updated_data": task_db[idx]}
    
    return {"error": "Task not found in the database. Cannot update data"}

# delete
@app.delete("/tasks/{id}")
def delete_task(id: int): # Takes a path parameter task_id that can take integer values
     # Check if the task_id is provided
    if id:
        # Find task by task_id
        for idx, u in enumerate(task_db):
            # If the task_id in the task_db matches the inputted task_id from the parameter
            # Remove the task object in task_db
            # Then return a status "ok" and show the removed data
            if u["id"] == id:
                task_db.remove(u)
                return {"status": "ok", "removed_data": u}
    
    # Return an error message if there is no task found
    return {"error": "Task Id not found in the database. Cannot delete the data"}