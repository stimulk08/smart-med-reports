from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from . import patients_repository
from app.models.schemas import PatientCreate

router = APIRouter()


@router.get('/')
def get_all_patients(db: Session = Depends(get_db)):
    return patients_repository.get_all_patients(db)


@router.get('/{id}')
def get_patient(id: int):
    return {id}


@router.get('/{id}/doctors')
def get_patients_doctors(id: int, limit: int):
    return [i for i in range(limit)]


@router.delete('/{id}')
def delete_patient(id: int):
    return {id}


@router.patch('/{id}')
def update_patient(id: int, update_dto: object):
    return {id, *update_dto}


# @router.post('/create', response_model=PatientCreate)
@router.post('/create')
def make_patient(dto: PatientCreate, db: Session = Depends(get_db)):
    return patients_repository.create_patient(db, dto)
