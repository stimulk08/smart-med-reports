from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import quizzes_repository
from app.api.quizzes.dto.create_quiz import QuizzesCreateDto
from app.db.database import get_db

router = APIRouter(prefix="/quizzes")


@router.get('/')
def get_all_quizzes(db: Session = Depends(get_db)):
    return quizzes_repository.get_quizzes(db)


@router.get('/{id}')
def get_quiz(_id: int, db: Session = Depends(get_db)):
    return quizzes_repository.get_quiz(db, _id)


@router.delete('/{id}')
def delete_quiz(_id: int, db: Session = Depends(get_db)):
    return quizzes_repository.delete_quiz(db, _id)


@router.put('/{id}')
def update_quiz(_id: int, dto: QuizzesCreateDto, db: Session = Depends(get_db)):
    return quizzes_repository.update_quiz(db, _id, dto)


@router.post('/')
def create_quiz(dto: QuizzesCreateDto, db: Session = Depends(get_db)):
    return quizzes_repository.create_quiz(db, dto)
