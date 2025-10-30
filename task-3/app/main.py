from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

# Initialize FastAPI app
app = FastAPI(title="Task Manager API")

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')
TASK_OPERATIONS = Counter('task_operations_total', 'Total task operations', ['operation'])

# Task model
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False

# In-memory database
tasks_db = []
task_id_counter = 1

# Helper function to find task by ID
def find_task(task_id: int):
    return next((task for task in tasks_db if task.id == task_id), None)

@app.get("/health")
async def health_check():
    """Health check endpoint for Kubernetes"""
    return {"status": "healthy"}

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    """Create a new task"""
    global task_id_counter
    start_time = time.time()
    
    REQUEST_COUNT.inc()
    TASK_OPERATIONS.labels(operation='create').inc()
    
    task.id = task_id_counter
    tasks_db.append(task)
    task_id_counter += 1
    
    REQUEST_LATENCY.observe(time.time() - start_time)
    return task

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    """Get all tasks"""
    start_time = time.time()
    REQUEST_COUNT.inc()
    TASK_OPERATIONS.labels(operation='read_all').inc()
    
    REQUEST_LATENCY.observe(time.time() - start_time)
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    """Get a specific task by ID"""
    start_time = time.time()
    REQUEST_COUNT.inc()
    TASK_OPERATIONS.labels(operation='read_one').inc()
    
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    REQUEST_LATENCY.observe(time.time() - start_time)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    """Update a task"""
    start_time = time.time()
    REQUEST_COUNT.inc()
    TASK_OPERATIONS.labels(operation='update').inc()
    
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed
    
    REQUEST_LATENCY.observe(time.time() - start_time)
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task"""
    start_time = time.time()
    REQUEST_COUNT.inc()
    TASK_OPERATIONS.labels(operation='delete').inc()
    
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db.remove(task)
    REQUEST_LATENCY.observe(time.time() - start_time)
    return {"message": "Task deleted"}

@app.get("/load-test")
async def load_test():
    """Endpoint to generate CPU load for testing HPA"""
    start_time = time.time()
    REQUEST_COUNT.inc()
    
    # Simulate CPU-intensive work
    n = 1000000
    [i * i for i in range(n)]
    
    REQUEST_LATENCY.observe(time.time() - start_time)
    return {"message": "Load test completed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
