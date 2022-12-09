from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from . import tags
from .dto.create_tag import TagCreateDto

router = APIRouter()


@router.get('/')
def get_all_tags(db: Session = Depends(get_db)):
    return tags.get_all_tags(db)


@router.get('/{id}')
def get_tag(id: int, db: Session = Depends(get_db)):
    return tags.get_tag_by_id(db, id)



@router.delete('/{id}')
def delete_tag(id: int, db: Session = Depends(get_db)):
    return tags.delete_tag(db, id)


@router.put('/{id}')
def update_tag(id: int, dto: TagCreateDto, db: Session = Depends(get_db)):
    return tags.update_tag(db, id, dto)


@router.post('')
def make_tag(dto: TagCreateDto, db: Session = Depends(get_db)):
    return tags.create_tag(db, dto)
