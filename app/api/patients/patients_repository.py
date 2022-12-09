from fastapi import HTTPException
from starlette import status

from app.api.patients.dto.create_patient import PatientCreateDto
from app.db.database import Database

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Session, relationship

from app.models.user import association_table, association_table_2


class Patient(Database):
    __tablename__ = "patient"
    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    reports = relationship("Quizzes", secondary=association_table_2, back_populates="doctors")
    # illness = relationship("Illness", secondary=association_table, back_populates='patients')
    doctors = relationship("Doctor", secondary=association_table, back_populates='patients')
    # visits = relationship("Visit", secondary=association_table, back_populates='patients')


def create_patient(db: Session, dto: PatientCreateDto):
    db_user = Patient(**dto.__dict__)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_patients(db: Session):
    return db.query(Patient).all()


def delete_patient(db: Session, _id: int):
    patient_delete = db.query(Patient).filter(Patient.id == _id).delete()
    if patient_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id {_id} not found")
    db.commit()
    return "Done"


def get_patient_by_id(db: Session, _id: int):
    patient = db.query(Patient).get(_id)
    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id {_id} not found")

    return patient


def update_patient(db: Session, _id: int, dto: PatientCreateDto):
    patient = db.query(Patient).filter(Patient.id == _id)
    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id {_id} not found")
    patient.update(dto.dict())
    db.commit()
    return "done"

