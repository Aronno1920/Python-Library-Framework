# main.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Sample student data
students = {
    1: {"name": "Selim Ahmed", "regID": "202501", "department": "Computer Science"},
    2: {"name": "Fatima Noor", "regID": "202502", "department": "Electrical Engineering"},
    3: {"name": "Imran Khan", "regID": "202503", "department": "Mechanical Engineering"}
}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# 🔍 New GET Method: Get student details by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")
