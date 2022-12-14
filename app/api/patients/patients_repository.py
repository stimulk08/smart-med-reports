from fastapi import HTTPException
from starlette import status

from app.api.patients.dto.create_patient import PatientCreateDto
from app.db.patient_doctor import Patient

from sqlalchemy.orm import Session



def create_patient(db: Session, dto: PatientCreateDto):
    db_user = Patient(**dto.__dict__)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_patients(db: Session):
    return db.query(Patient).all()


def delete_patient(db: Session, _id: int):
    patient = db.query(Patient).get(_id)
    patient.delete()
    db.commit()

    return "Done"


def get_patient_by_id(db: Session, _id: int):
    patient = db.query(Patient).get(_id)

    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id {_id} not found")

    return patient


def update_patient(db: Session, _id: int, dto: PatientCreateDto):
    patient = get_patient_by_id(db, _id)
    patient.update(dto.dict())
    db.commit()

    return "done"

