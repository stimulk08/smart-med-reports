from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import user_repository
from app.core.config import get_db, Database, engine
from app.db.user_repository import create_user

from app.models.schemas import Patient

router = APIRouter()
Database.metadata.create_all(engine)

@router.get('/')
def get_all_patients(db: Session = Depends(get_db)):
    return user_repository.get_all_patients(db)


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
def make_patient(dto: Patient, db: Session = Depends(get_db)):
    return create_user(db, dto)
