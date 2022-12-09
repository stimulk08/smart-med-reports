from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.api.tags.dto.create_tag import TagCreateDto
from app.db.tag_patient import Tag


def create_tag(db: Session, dto: TagCreateDto):
    db_tag = Tag(**dto.__dict__)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_all_tags(db: Session):
    return db.query(Tag).all()


def delete_tag(db: Session, _id: int):
    tag = db.query(Tag).get(_id)
    tag.delete()
    db.commit()

    return "Done"


def get_tag_by_id(db: Session, _id: int):
    tag = db.query(Tag).get(_id)

    if tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tag with id {_id} not found")

    return tag


def update_tag(db: Session, _id: int, dto: TagCreateDto):
    tag = get_tag_by_id(db, _id)
    tag.update(dto.dict())
    db.commit()

    return "done"
