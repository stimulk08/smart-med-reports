from fastapi import HTTPException
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
from starlette import status

from app.api.doctors.dto.create_doctor import DoctorCreateDto
from app.api.patients.patients_repository import get_patient_by_id
from app.db.database import Database
from app.models.user import association_table


class Doctor(Database):
    __tablename__ = "doctor"

    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    patients = relationship("Patient", secondary=association_table, back_populates="doctors")
    report_id = Column(ForeignKey("quizzes_table.id"))
    reports = relationship("Quizzes", back_populates="doctors")
    # specialization = relationship("Specialization", secondary=association_table, back_populates="doctors")


def create_doctor(db: Session, dto: DoctorCreateDto):
    db_user = Doctor(**dto.__dict__)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_doctor(db: Session, _id: int) -> Doctor:
    doctor = db.query(Doctor).get(_id)

    if doctor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Doctor with id {_id} not found")

    return doctor


def assign_patient(_id: int, patient_id: int, db: Session):
    patient = get_patient_by_id(db, patient_id)
    doctor = get_doctor(db, _id)
    doctor.patients.append(patient)
    db.commit()


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def delete_doctor(db: Session, _id: int):
    doctor = get_doctor(db, _id)

    doctor.delete()
    db.commit()
    return "Done"


def update_doctor(db: Session, _id: int, dto: DoctorCreateDto):
    doctor = get_doctor(db, _id)

    doctor.update(dto.dict())
    db.commit()

    return "done"
