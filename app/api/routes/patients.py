from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.config import get_db
from app.db.user_repository import create_user

from app.models.schemas import PatientCreate

router = APIRouter()


@router.get('/')
def get_all_patients():
    pass


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


@router.post('')
def delete_patient(dto):
    return {id, *dto}


@router.post('')
def make_patient(dto: PatientCreate, db: Session = Depends(get_db)):
    return create_user(db, dto)
