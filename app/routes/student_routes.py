from fastapi import APIRouter, Depends, HTTPException
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.schemas import student_schema
from app.services import student_service


userrouter = APIRouter(
    prefix= "/user",
    tags=["UserRoutes"]
)


@userrouter.post("/add", response_model= student_schema.StudentResponse)
def CreateStudent(
    data: student_schema.StudentCreate,
    db: Session = Depends(get_db),
):
    return student_service.create_student(db, data)


@userrouter.get("/getall", response_model=list[student_schema.StudentResponse])
def GetAllStudent(
    db: Session = Depends(get_db)
):
    return student_service.getAllStudents(db)