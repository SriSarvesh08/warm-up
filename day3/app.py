
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My First API")


@app.get("/")
def home():
    return {"message": "Welcome to my first API!"}


@app.get("/about")
def about():
    return {
        "project": "Python API Practice",
        "task": "T14",
        "developer": "Sri Sarvesh"
    }


class Student(BaseModel):
    name: str
    skill: str


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student data received successfully",
        "student": {
            "name": student.name,
            "skill": student.skill
        }
    }
