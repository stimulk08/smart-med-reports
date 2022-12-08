from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from . import patients_repository
from .dto.create_patient import PatientCreateDto
from .patients_repository import Patient

router = APIRouter()


@router.get('/')
def get_all_patients(db: Session = Depends(get_db)):
    return patients_repository.get_all_patients(db)


@router.get('/{id}')
def get_patient(id: int, db: Session = Depends(get_db)):
    return patients_repository.get_patient_by_id(db, id)


@router.get('/{id}/doctors')
def get_patients_doctors(id: int, limit: int):
    return [i for i in range(limit)]


@router.delete('/{id}')
def delete_patient(id: int, db: Session = Depends(get_db)):
    return patients_repository.delete_patient(db, id)


@router.put('/{id}')
def update_patient(id: int, dto: PatientCreateDto, db: Session = Depends(get_db)):
    return patients_repository.update_patient(db, id, dto)


@router.post('')
def make_patient(dto: PatientCreateDto, db: Session = Depends(get_db)):
    return patients_repository.create_patient(db, dto)
