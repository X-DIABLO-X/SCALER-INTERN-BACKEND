from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from db import get_connection

app = FastAPI(title="Student Registration API")


class Student(BaseModel):
    student_name: str
    email: EmailStr
    year: int
    department: str


@app.post("/register-student")
def register_student(student: Student):
    if student.year < 1 or student.year > 5:
        raise HTTPException(status_code=400, detail="Invalid year")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO student (name, email, year, department)
            VALUES (%s,%s,%s,%s)
            ON CONFLICT (email) DO NOTHING
        """, (
            student.student_name,
            student.email,
            student.year,
            student.department
        ))

        conn.commit()
        return {"status": "success"}

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()
