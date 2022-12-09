from fastapi import HTTPException, APIRouter, Depends
from starlette import status

from app.api.doctors import doctors_repository
from app.api.doctors.dto.create_doctor import DoctorCreateDto
from app.api.patients.dto.create_patient import PatientCreateDto
# from app.api.doctors.dto.create_doctor DoctorCreateDto
from app.db.database import Database, get_db

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session, relationship

from app.models.user import patient_doctor_table

router = APIRouter()


@router.get('/')
def get_all_doctors(db: Session = Depends(get_db)):
    return doctors_repository.get_all_doctors(db)


@router.get('/{id}')
def get_doctor(id: int):
    return {id}


@router.get('/{id}/patients')
def get_doctors_patients(limit: int):
    return [i for i in range(limit)]


@router.delete('/{id}')
def delete_doctor(id: int, db: Session = Depends(get_db)):
    return doctors_repository.delete_doctor(db, id)


@router.patch('/{id}')
def update_doctor(id: int, dto: DoctorCreateDto, db: Session = Depends(get_db)):
    return doctors_repository.update_doctor(db, id, dto)


@router.post('/')
def create_doctor(dto: DoctorCreateDto, db: Session = Depends(get_db)):
    return doctors_repository.create_doctor(db, dto)
