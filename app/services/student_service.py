from app.models.student_model import Student
from sqlalchemy.orm import Session

def create_student(db: Session, student_data):
    new_student = Student(
        name=student_data.name,
        age=student_data.age,
        course=student_data.course
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

def getAllStudents(db: Session):
    return db.query(Student).all()