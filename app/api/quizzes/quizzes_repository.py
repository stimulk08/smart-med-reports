from fastapi import HTTPException
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
from starlette import status

from app.api.doctors.doctors_repository import get_doctor
from app.api.quizzes.dto.create_quiz import QuizzesCreateDto
from app.api.quizzes.field.field_repository import TextField, NumberField, ChoiceField
from app.db.database import Database
from app.db.doctor_quiz import Quiz

field_to_model = {
    "text": lambda f, arr: arr.append(TextField(f.value)),
    "number": lambda f, arr: arr.append(NumberField(f.value)),
    "choices": lambda f, arr: arr.append(ChoiceField(f.value))
}


def create_quiz(db: Session, dto: QuizzesCreateDto):
    text_fields = []
    num_fields = []
    choice_fields = []

    for field in dto.fields:
        if field.type == "text":
            text_fields.append(TextField(field.value))
        elif field.type == "number":
            num_fields.append(NumberField(field.value))
        elif field.type == "choices":
            choice_fields.append(ChoiceField(field.value))
        else:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail=f"Unprocessable field type {field.type}")

    doctor = get_doctor(db, dto.doctor_id)

    db.add_all(text_fields)
    db.add_all(num_fields)
    db.add_all(choice_fields)

    quiz = Quiz(
        text_fields=text_fields,
        number_fields=num_fields,
        choice_fields=choice_fields,
        doctors=[doctor]
    )
    db.commit()
    db.refresh(quiz)
    return quiz


def get_quizzes(db: Session):
    return db.query(Quiz).all()


def get_quiz(db: Session, _id: int):
    quiz = db.query(Quiz).get(_id)

    if quiz is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id {_id} not found")

    return quiz


def delete_quiz(db: Session, _id: int):
    doctor = get_quiz(db, _id)
    doctor.delete()
    db.commit()
    return "Done"


def update_quiz(db: Session, _id: int, dto: QuizzesCreateDto):
    quiz = get_quiz(db, _id)

    quiz.update(dto.dict())
    db.commit()

    return "Done"
