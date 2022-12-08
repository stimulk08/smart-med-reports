from fastapi import APIRouter, Depends

from app.api.doctors import doctors_repository
from app.api.doctors.dto.create_doctor import DoctorCreateDto
from app.api.patients.dto.create_patient import PatientCreateDto
from app.db.database import get_db

from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/')
def get_all_doctors():
    pass


@router.get('/{id}')
def get_doctor(id: int):
    return {id}


@router.get('/{id}/patients')
def get_doctors_patients(limit: int):
    return [i for i in range(limit)]


@router.delete('/{id}')
def delete_doctor(id: int):
    return {id}


@router.patch('/{id}')
def update_doctor(id: int, update_dto: object):
    return {id, *update_dto}


@router.post('/')
def create_doctor(dto: DoctorCreateDto, db: Session = Depends(get_db)):
    return doctors_repository.create_doctor(db, dto)


@router.patch('/{id}/assign/patients/{patient_id}')
def assign_patient(id: int, patient_id: int, db: Session = Depends(get_db)):
    return doctors_repository.assign_patient(id, patient_id, db)
